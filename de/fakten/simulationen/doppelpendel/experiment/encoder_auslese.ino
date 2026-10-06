/*
 * encoder_auslese.ino — RT-38 Doppelpendel Winkelauslese
 *
 * Liest zwei AS5600 magnetische 12-bit I²C-Encoder aus (via TCA9548A Multiplexer)
 * und sendet t,theta1,theta2 (Winkel in Rad) über serielle Schnittstelle.
 *
 * Hardware:
 *   - Arduino Nano oder Mega
 *   - 2× AS5600 Breakout Board (I²C, Adresse 0x36)
 *   - 1× TCA9548A I²C-Multiplexer (Adresse 0x70) — PFLICHT bei zwei AS5600
 *   - 2× Neodym-Scheibenmagnet Ø 6mm × 2.5mm auf den Lagerachsen
 *
 * Verdrahtung TCA9548A:
 *   SDA → Arduino SDA (A4 beim Nano)
 *   SCL → Arduino SCL (A5 beim Nano)
 *   VCC → 5V
 *   GND → GND
 *   SD0/SC0 → AS5600 #1 (Encoder Arm 1 / theta1)
 *   SD1/SC1 → AS5600 #2 (Encoder Arm 2 / theta2)
 *
 * Ausgabe (serielle Schnittstelle, 115200 Baud):
 *   t,theta1,theta2\n
 *   0.000000,0.785398,0.523599\n
 *   ...
 *
 * Kalibrierung:
 *   ZERO_OFFSET_1 und ZERO_OFFSET_2 setzen (Rohwert bei Ruhelage / senkrecht hängend)
 *
 * © Dominic-René Schu, 2026 — Resonanzfeldtheorie (RT-38)
 */

#include <Wire.h>

// ---------------------------------------------------------------------------
// Konfiguration
// ---------------------------------------------------------------------------
#define SAMPLE_RATE_HZ      100      // Abtastrate in Hz (10 ms pro Sample)
#define TCA9548A_ADDR       0x70     // I²C-Adresse des Multiplexers
#define AS5600_ADDR         0x36     // Feste I²C-Adresse des AS5600
#define AS5600_REG_RAW_HI   0x0C     // Register: Rohwinkel High-Byte
#define AS5600_REG_STATUS   0x0B     // Register: Statusbyte (Magnet OK = bit 5)

// Rohwert-Offset bei Ruhelage (0 = senkrecht hängend)
// Bestimmen: Pendel senkrecht hängend → Serial Monitor lesen → Wert hier eintragen
#define ZERO_OFFSET_1       0        // Rohwert-Offset Encoder 1 (theta1)
#define ZERO_OFFSET_2       0        // Rohwert-Offset Encoder 2 (theta2)

// Vorzeichen: +1 = Uhrzeigersinn positiv, -1 = Gegenuhrzeigersinn positiv
#define SIGN_THETA1         (+1)
#define SIGN_THETA2         (+1)

// ---------------------------------------------------------------------------
// Globale Variablen
// ---------------------------------------------------------------------------
unsigned long startTime_us = 0;
unsigned long interval_us  = 1000000UL / SAMPLE_RATE_HZ;

// ---------------------------------------------------------------------------
// TCA9548A: Kanal auswählen
// ---------------------------------------------------------------------------
void tca_select(uint8_t channel) {
  if (channel > 7) return;
  Wire.beginTransmission(TCA9548A_ADDR);
  Wire.write(1 << channel);
  Wire.endTransmission();
}

// ---------------------------------------------------------------------------
// AS5600: 12-bit Rohwinkel lesen (0–4095)
// ---------------------------------------------------------------------------
uint16_t as5600_read_raw(void) {
  Wire.beginTransmission(AS5600_ADDR);
  Wire.write(AS5600_REG_RAW_HI);
  Wire.endTransmission(false);
  Wire.requestFrom(AS5600_ADDR, (uint8_t)2);
  if (Wire.available() < 2) return 0xFFFF;  // Fehler
  uint8_t hi = Wire.read();
  uint8_t lo = Wire.read();
  return ((uint16_t)(hi & 0x0F) << 8) | lo;
}

// ---------------------------------------------------------------------------
// AS5600: Magnetstatus prüfen (Bit 5 = Magnet erkannt)
// ---------------------------------------------------------------------------
bool as5600_magnet_ok(void) {
  Wire.beginTransmission(AS5600_ADDR);
  Wire.write(AS5600_REG_STATUS);
  Wire.endTransmission(false);
  Wire.requestFrom(AS5600_ADDR, (uint8_t)1);
  if (!Wire.available()) return false;
  uint8_t status = Wire.read();
  return (status & 0x20) != 0;
}

// ---------------------------------------------------------------------------
// Rohwert → Winkel in Rad, normiert auf (−π, π]
// ---------------------------------------------------------------------------
float raw_to_rad(uint16_t raw, int16_t zero_offset, int8_t sign) {
  int16_t corrected = (int16_t)raw - zero_offset;
  // In den Bereich [0, 4095] bringen
  corrected = ((corrected % 4096) + 4096) % 4096;
  // Auf (0, 2π] skalieren
  float angle = (float)corrected * (2.0f * M_PI / 4096.0f);
  // Auf (−π, π] normieren
  if (angle > M_PI) angle -= 2.0f * M_PI;
  return sign * angle;
}

// ---------------------------------------------------------------------------
// Setup
// ---------------------------------------------------------------------------
void setup() {
  Serial.begin(115200);
  Wire.begin();
  Wire.setClock(400000UL);  // Fast mode 400 kHz

  // Magnetstatus prüfen
  tca_select(0);
  bool ok1 = as5600_magnet_ok();
  tca_select(1);
  bool ok2 = as5600_magnet_ok();

  if (!ok1 || !ok2) {
    Serial.println("# FEHLER: Magnet nicht erkannt!");
    Serial.print("# Encoder 1 (theta1): ");
    Serial.println(ok1 ? "OK" : "KEIN MAGNET");
    Serial.print("# Encoder 2 (theta2): ");
    Serial.println(ok2 ? "OK" : "KEIN MAGNET");
    Serial.println("# Magnete prüfen und Sketch neu starten.");
    while (true) { delay(1000); }
  }

  Serial.println("# RT-38 Doppelpendel Encoder-Auslese");
  Serial.print("# Abtastrate: ");
  Serial.print(SAMPLE_RATE_HZ);
  Serial.println(" Hz");
  Serial.println("# Magnet 1: OK  Magnet 2: OK");
  Serial.println("# Format: t,theta1,theta2 (Sekunden, Rad, Rad)");
  Serial.println("t,theta1,theta2");

  startTime_us = micros();
}

// ---------------------------------------------------------------------------
// Loop
// ---------------------------------------------------------------------------
void loop() {
  unsigned long now_us = micros();
  static unsigned long next_us = 0;

  if (next_us == 0) next_us = startTime_us + interval_us;
  if ((long)(now_us - next_us) < 0) return;
  next_us += interval_us;

  // Encoder 1 lesen (TCA Kanal 0)
  tca_select(0);
  uint16_t raw1 = as5600_read_raw();

  // Encoder 2 lesen (TCA Kanal 1)
  tca_select(1);
  uint16_t raw2 = as5600_read_raw();

  float t      = (float)(now_us - startTime_us) * 1e-6f;
  float theta1 = raw_to_rad(raw1, ZERO_OFFSET_1, SIGN_THETA1);
  float theta2 = raw_to_rad(raw2, ZERO_OFFSET_2, SIGN_THETA2);

  // CSV-Zeile ausgeben (6 Dezimalstellen)
  Serial.print(t, 6);
  Serial.print(',');
  Serial.print(theta1, 6);
  Serial.print(',');
  Serial.println(theta2, 6);
}
