/*
 * encoder_readout.ino — RT-38 Double Pendulum Angle Readout
 *
 * Reads two AS5600 magnetic 12-bit I²C encoders (via TCA9548A multiplexer)
 * and transmits t,theta1,theta2 (angles in radians) over the serial interface.
 *
 * Hardware:
 *   - Arduino Nano or Mega
 *   - 2× AS5600 breakout board (I²C, address 0x36)
 *   - 1× TCA9548A I²C multiplexer (address 0x70) — REQUIRED for two AS5600 units
 *   - 2× neodymium disc magnet Ø 6 mm × 2.5 mm on the bearing axles
 *
 * TCA9548A wiring:
 *   SDA → Arduino SDA (A4 on Nano)
 *   SCL → Arduino SCL (A5 on Nano)
 *   VCC → 5V
 *   GND → GND
 *   SD0/SC0 → AS5600 #1 (encoder arm 1 / theta1)
 *   SD1/SC1 → AS5600 #2 (encoder arm 2 / theta2)
 *
 * Serial output (115200 baud):
 *   t,theta1,theta2\n
 *   0.000000,0.785398,0.523599\n
 *   ...
 *
 * Calibration:
 *   Set ZERO_OFFSET_1 and ZERO_OFFSET_2 (raw value when pendulum hangs vertically)
 *
 * © Dominic-René Schu, 2026 — Resonance Field Theory (RT-38)
 */

#include <Wire.h>

// ---------------------------------------------------------------------------
// Configuration
// ---------------------------------------------------------------------------
#define SAMPLE_RATE_HZ      100      // Sampling rate in Hz (10 ms per sample)
#define TCA9548A_ADDR       0x70     // I²C address of the multiplexer
#define AS5600_ADDR         0x36     // Fixed I²C address of AS5600
#define AS5600_REG_RAW_HI   0x0C     // Register: raw angle high byte
#define AS5600_REG_STATUS   0x0B     // Register: status byte (magnet OK = bit 5)

// Raw value offset at rest (0 = hanging vertically)
// Determine: hang pendulum vertically → read Serial Monitor → enter value here
#define ZERO_OFFSET_1       0        // Raw offset encoder 1 (theta1)
#define ZERO_OFFSET_2       0        // Raw offset encoder 2 (theta2)

// Sign: +1 = clockwise positive, -1 = counter-clockwise positive
#define SIGN_THETA1         (+1)
#define SIGN_THETA2         (+1)

// ---------------------------------------------------------------------------
// Global variables
// ---------------------------------------------------------------------------
unsigned long startTime_us = 0;
unsigned long interval_us  = 1000000UL / SAMPLE_RATE_HZ;

// ---------------------------------------------------------------------------
// TCA9548A: select channel
// ---------------------------------------------------------------------------
void tca_select(uint8_t channel) {
  if (channel > 7) return;
  Wire.beginTransmission(TCA9548A_ADDR);
  Wire.write(1 << channel);
  Wire.endTransmission();
}

// ---------------------------------------------------------------------------
// AS5600: read 12-bit raw angle (0–4095)
// ---------------------------------------------------------------------------
uint16_t as5600_read_raw(void) {
  Wire.beginTransmission(AS5600_ADDR);
  Wire.write(AS5600_REG_RAW_HI);
  Wire.endTransmission(false);
  Wire.requestFrom(AS5600_ADDR, (uint8_t)2);
  if (Wire.available() < 2) return 0xFFFF;  // error
  uint8_t hi = Wire.read();
  uint8_t lo = Wire.read();
  return ((uint16_t)(hi & 0x0F) << 8) | lo;
}

// ---------------------------------------------------------------------------
// AS5600: check magnet status (bit 5 = magnet detected)
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
// Raw value → angle in radians, normalised to (−π, π]
// ---------------------------------------------------------------------------
float raw_to_rad(uint16_t raw, int16_t zero_offset, int8_t sign) {
  int16_t corrected = (int16_t)raw - zero_offset;
  // Bring into range [0, 4095]
  corrected = ((corrected % 4096) + 4096) % 4096;
  // Scale to (0, 2π]
  float angle = (float)corrected * (2.0f * M_PI / 4096.0f);
  // Normalise to (−π, π]
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

  // Check magnet status
  tca_select(0);
  bool ok1 = as5600_magnet_ok();
  tca_select(1);
  bool ok2 = as5600_magnet_ok();

  if (!ok1 || !ok2) {
    Serial.println("# ERROR: Magnet not detected!");
    Serial.print("# Encoder 1 (theta1): ");
    Serial.println(ok1 ? "OK" : "NO MAGNET");
    Serial.print("# Encoder 2 (theta2): ");
    Serial.println(ok2 ? "OK" : "NO MAGNET");
    Serial.println("# Check magnets and restart sketch.");
    while (true) { delay(1000); }
  }

  Serial.println("# RT-38 Double Pendulum Encoder Readout");
  Serial.print("# Sampling rate: ");
  Serial.print(SAMPLE_RATE_HZ);
  Serial.println(" Hz");
  Serial.println("# Magnet 1: OK  Magnet 2: OK");
  Serial.println("# Format: t,theta1,theta2 (seconds, rad, rad)");
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

  // Read encoder 1 (TCA channel 0)
  tca_select(0);
  uint16_t raw1 = as5600_read_raw();

  // Read encoder 2 (TCA channel 1)
  tca_select(1);
  uint16_t raw2 = as5600_read_raw();

  float t      = (float)(now_us - startTime_us) * 1e-6f;
  float theta1 = raw_to_rad(raw1, ZERO_OFFSET_1, SIGN_THETA1);
  float theta2 = raw_to_rad(raw2, ZERO_OFFSET_2, SIGN_THETA2);

  // Print CSV line (6 decimal places)
  Serial.print(t, 6);
  Serial.print(',');
  Serial.print(theta1, 6);
  Serial.print(',');
  Serial.println(theta2, 6);
}
