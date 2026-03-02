# reso_music.py V5.1 — Fließende Harmonics (Mix-Balance)
# © Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie
#
# ResoMusic: Resonanzlogische Musikbegleitung
#
# V5.1: Harmonics dezenter — Begleitung, nicht Konkurrenz.
#       Durchgehender Klangteppich der sich unterordnet.
#
# python reso_music.py song.mp3 [passes] [--reset]

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import json
from scipy.signal import stft, find_peaks
from scipy.io import wavfile

PI = np.pi
ERFAHRUNG_DATEI = "reso_erfahrung.json"

NOTEN_NAMEN = ['C', 'C#', 'D', 'D#', 'E', 'F',
               'F#', 'G', 'G#', 'A', 'A#', 'B']

KONSONANZ = {
    0: 1.0, 1: 0.15, 2: 0.3, 3: 0.75, 4: 0.8, 5: 0.85,
    6: 0.2, 7: 0.95, 8: 0.6, 9: 0.7, 10: 0.4, 11: 0.35,
}


def kopplungseffizienz(delta_phi):
    return np.cos(delta_phi / 2.0) ** 2


def note_zu_freq(note_idx, oktave=3):
    midi = 12 * (oktave + 1) + note_idx
    return 440.0 * 2 ** ((midi - 69) / 12.0)


# ============================================================
# SYNTHESIZER
# ============================================================

class KlangErzeuger:

    def __init__(self, sr=22050):
        self.sr = sr

    def erzeuge_strom(self, events, n_samples):
        if not events:
            return np.zeros(n_samples)

        out = np.zeros(n_samples)
        t = np.arange(n_samples) / self.sr

        positionen = [e['start'] for e in events]
        freqs1 = [e['freq'] for e in events]
        freqs2 = [e.get('freq2', e['freq']) for e in events]
        freqs3 = [e.get('freq3', e['freq']) for e in events]
        vols = [e['vol'] for e in events]
        wärmen = [e.get('wärme', 0.4) for e in events]

        if positionen[0] > 0:
            positionen.insert(0, 0)
            freqs1.insert(0, freqs1[0])
            freqs2.insert(0, freqs2[0])
            freqs3.insert(0, freqs3[0])
            vols.insert(0, vols[0] * 0.2)
            wärmen.insert(0, wärmen[0])

        if positionen[-1] < n_samples - 1:
            positionen.append(n_samples - 1)
            freqs1.append(freqs1[-1])
            freqs2.append(freqs2[-1])
            freqs3.append(freqs3[-1])
            vols.append(vols[-1] * 0.2)
            wärmen.append(wärmen[-1])

        pos = np.array(positionen, dtype=float)
        samples = np.arange(n_samples, dtype=float)

        freq1_kurve = np.interp(samples, pos, freqs1)
        freq2_kurve = np.interp(samples, pos, freqs2)
        freq3_kurve = np.interp(samples, pos, freqs3)
        vol_kurve = np.interp(samples, pos, vols)
        wärme_kurve = np.interp(samples, pos, wärmen)

        # Lautstärke glätten (längerer Kern = sanftere Übergänge)
        glättung = min(int(0.5 * self.sr), n_samples // 4)
        if glättung > 1:
            kernel = np.ones(glättung) / glättung
            vol_kurve = np.convolve(vol_kurve, kernel, mode='same')

        # Phasen kumulativ
        phase1 = np.cumsum(2 * PI * freq1_kurve / self.sr)
        phase2 = np.cumsum(2 * PI * freq2_kurve / self.sr)
        phase3 = np.cumsum(2 * PI * freq3_kurve / self.sr)

        # Grundton
        out += np.sin(phase1) * vol_kurve

        # Chorus (dezenter)
        d1 = 1.0 + 0.0015 * np.sin(2 * PI * 0.25 * t)
        d2 = 1.0 - 0.0015 * np.sin(2 * PI * 0.32 * t)
        pd1 = np.cumsum(2 * PI * freq1_kurve * d1 / self.sr)
        pd2 = np.cumsum(2 * PI * freq1_kurve * d2 / self.sr)
        out += 0.10 * np.sin(pd1) * vol_kurve
        out += 0.10 * np.sin(pd2) * vol_kurve

        # Obertöne
        for h in range(2, 5):
            amp = wärme_kurve / (h ** 2.0)
            vib = 1.0 + 0.0008 * np.sin(2 * PI * (3.5 + h * 0.3) * t)
            ph = np.cumsum(2 * PI * freq1_kurve * h * vib / self.sr)
            out += amp * np.sin(ph) * vol_kurve

        # Zweite Stimme (leiser)
        s2_vol = vol_kurve * 0.20
        out += np.sin(phase2) * s2_vol
        pd2s = np.cumsum(2 * PI * freq2_kurve * d1 / self.sr)
        out += 0.05 * np.sin(pd2s) * s2_vol

        # Dritte Stimme (sehr leise)
        s3_vol = vol_kurve * 0.08 * wärme_kurve
        out += np.sin(phase3) * s3_vol

        # Vibrato
        out *= 1.0 + 0.002 * np.sin(2 * PI * 3.8 * t)

        # Ein-/Ausblenden
        fade = min(int(1.0 * self.sr), n_samples // 4)
        if fade > 0:
            out[:fade] *= np.linspace(0, 1, fade) ** 2
            out[-fade:] *= np.linspace(1, 0, fade) ** 2

        return out


# ============================================================
# ANALYSE
# ============================================================

class Analysator:

    def __init__(self, sr=22050, hop=512, n_fft=2048):
        self.sr = sr
        self.hop = hop
        self.n_fft = n_fft

    def analysiere(self, audio):
        f, t, Zxx = stft(audio, fs=self.sr, nperseg=self.n_fft,
                         noverlap=self.n_fft - self.hop)
        mag = np.abs(Zxx)

        dc = np.sum(mag ** 2, axis=0)
        dc = dc / (np.max(dc) + 1e-10)

        chroma = np.zeros((12, mag.shape[1]))
        for i, freq in enumerate(f):
            if 30 < freq < 8000:
                midi = 12 * np.log2(freq / 440.0) + 69
                chroma[int(round(midi)) % 12] += mag[i]
        chroma /= (np.max(chroma, axis=0, keepdims=True) + 1e-10)

        kernel = np.ones(5) / 5
        dc_s = np.convolve(dc, kernel, mode='same')
        beats, _ = find_peaks(dc_s, distance=8, height=0.12)

        freq_sw = np.zeros(len(t))
        for i in range(len(t)):
            total = np.sum(mag[:, i])
            if total > 1e-10:
                freq_sw[i] = np.average(f, weights=mag[:, i] + 1e-10)

        return {
            'f': f, 't': t, 'magnitude': mag,
            'dc': dc, 'chroma': chroma, 'beats': beats,
            'freq_schwerpunkt': freq_sw
        }

    def erkenne_phasen(self, analyse):
        dc = analyse['dc']
        chroma = analyse['chroma']
        beats = analyse['beats']
        fsw = analyse['freq_schwerpunkt']
        phasen = []

        for i in range(len(dc)):
            ch = chroma[:, i]
            gi = int(np.argmax(ch))
            gt = ch[(gi + 4) % 12]
            kt = ch[(gi + 3) % 12]
            harm = 'dur' if gt > kt + 0.1 else (
                'moll' if kt > gt + 0.1 else 'neutral')

            if dc[i] < 0.02:
                dyn = 'stille'
            elif i >= 10 and dc[i] - dc[i-10] > 0.03:
                dyn = 'crescendo'
            elif i >= 10 and dc[i] - dc[i-10] < -0.03:
                dyn = 'decrescendo'
            else:
                dyn = 'stabil'

            if len(beats) == 0:
                beat = 'off'
            else:
                md = np.min(np.abs(beats - i))
                beat = 'on' if md <= 1 else (
                    'near' if md <= 4 else 'off')

            phasen.append({
                'grundton_idx': gi,
                'grundton': NOTEN_NAMEN[gi],
                'harmonie': harm,
                'dynamik': dyn,
                'beat': beat,
                'energie': dc[i],
                'chroma': ch.copy(),
                'freq_sw': fsw[i]
            })
        return phasen


# ============================================================
# ERFAHRUNGSSPEICHER
# ============================================================

class Erfahrung:

    def __init__(self, decay=0.95):
        self.noten = {}
        self.decay = decay
        self.generation = 0
        self.songs_gelernt = 0

    def _key(self, phase, intervall):
        return (f"{phase['grundton']},{phase['harmonie']},"
                f"{phase['dynamik']},{intervall}")

    def lerne_note(self, phase, intervall, belohnung):
        key = self._key(phase, intervall)
        old = self.noten.get(key, 0.0)
        self.noten[key] = old * self.decay + belohnung

    def beste_intervalle(self, phase, top_n=4):
        scores = {}
        for iv in range(12):
            scores[iv] = self.noten.get(self._key(phase, iv), 0.0)
        return sorted(scores.items(), key=lambda x: x[1],
                      reverse=True)[:top_n]

    def speichern(self, pfad):
        with open(pfad, 'w') as f:
            json.dump({
                'generation': self.generation,
                'songs_gelernt': self.songs_gelernt,
                'noten': self.noten
            }, f, indent=2)
        print(f"  💾 Gen {self.generation},"
              f" {len(self.noten)} Einträge,"
              f" {self.songs_gelernt} Songs")

    def laden(self, pfad):
        if not os.path.exists(pfad):
            print("  Keine Erfahrung → frisch")
            return
        with open(pfad, 'r') as f:
            data = json.load(f)
        self.generation = data.get('generation', 0)
        self.songs_gelernt = data.get('songs_gelernt', 0)
        self.noten = data.get('noten', {})
        print(f"  ← Gen {self.generation},"
              f" {len(self.noten)} Einträge,"
              f" {self.songs_gelernt} Songs")

    def statistik(self):
        print(f"\n  📊 Gen {self.generation} |"
              f" {len(self.noten)} Noten |"
              f" {self.songs_gelernt} Songs")
        if self.noten:
            top = sorted(self.noten.items(),
                         key=lambda x: x[1], reverse=True)[:6]
            for k, s in top:
                p = k.split(',')
                iv = int(p[-1])
                print(f"     {','.join(p[:-1]):25s}"
                      f" + {NOTEN_NAMEN[iv]:3s} (iv={iv:2d})"
                      f" → {s:+.3f}")


# ============================================================
# RESONANZLOGISCHER AGENT
# ============================================================

class ResoMusik:

    def __init__(self, sr=22050):
        self.sr = sr
        self.analysator = Analysator(sr=sr)
        self.erfahrung = Erfahrung()
        self.klang = KlangErzeuger(sr=sr)

    def analysiere(self, audio):
        analyse = self.analysator.analysiere(audio)
        phasen = self.analysator.erkenne_phasen(analyse)
        return analyse, phasen

    def lerne(self, analyse, phasen):
        chroma = analyse['chroma']
        nf = len(phasen)
        lookahead = min(15, nf // 40)

        for i in range(1, nf - lookahead):
            phase = phasen[i]
            gi = phase['grundton_idx']

            future = np.mean(chroma[:, i+1:i+1+lookahead], axis=1)
            past_start = max(0, i - lookahead)
            past = np.mean(chroma[:, past_start:i], axis=1)

            for iv in range(12):
                zi = (gi + iv) % 12
                konsonanz = KONSONANZ.get(iv, 0.3)
                zukunft = future[zi]
                vergangenheit = past[zi]
                aktuell = phase['chroma'][zi]

                belohnung = (konsonanz
                             * (zukunft * 0.5 + vergangenheit * 0.3
                                + aktuell * 0.2)
                             * (1.0 - aktuell * 0.3))

                if phase['harmonie'] == 'moll' and iv in [3, 7]:
                    belohnung *= 1.4
                if phase['harmonie'] == 'dur' and iv in [4, 7]:
                    belohnung *= 1.4
                if iv == 7:
                    belohnung *= 1.2

                self.erfahrung.lerne_note(phase, iv, belohnung)

    def erzeuge(self, analyse, phasen):
        nf = len(phasen)
        hop = self.analysator.hop
        ns = int(nf * hop)

        events = []
        event_abstand = 12

        # ── Niedrigere Basis-Lautstärke ──
        basis_vol = 0.04  # V5 war 0.08

        letzter_gi = None
        letzter_harm = 'neutral'

        for i in range(0, nf, max(1, event_abstand // 2)):
            phase = phasen[i]
            gi = phase['grundton_idx']

            if phase['beat'] == 'on':
                dp = 0.0
            elif phase['beat'] == 'near':
                dp = PI / 8
            else:
                dp = PI / 5
            eps = kopplungseffizienz(dp)

            if phase['dynamik'] == 'stille':
                if letzter_gi is not None:
                    gi = letzter_gi
                    vol = basis_vol
                else:
                    continue
            else:
                # ── Gedämpftere Lautstärke ──
                vol = max(basis_vol, phase['energie'] * eps * 0.4)
                letzter_gi = gi
                letzter_harm = phase['harmonie']

            if phase['dynamik'] == 'stille':
                lookup = {
                    'grundton': NOTEN_NAMEN[gi],
                    'harmonie': letzter_harm,
                    'dynamik': 'stabil',
                }
            else:
                lookup = phase

            beste = self.erfahrung.beste_intervalle(lookup, top_n=3)
            if beste[0][1] <= 0:
                beste = [(7, 0.5), (0, 0.3), (4, 0.2)]

            okt = 3 if phase['freq_sw'] > 300 else 2

            iv1, _ = beste[0]
            iv2, sc2 = beste[1] if len(beste) > 1 else (iv1, 0)
            iv3, sc3 = beste[2] if len(beste) > 2 else (iv1, 0)

            freq1 = note_zu_freq((gi + iv1) % 12, okt)
            freq2 = (note_zu_freq((gi + iv2) % 12, okt)
                     if sc2 > 0 else freq1)
            freq3 = (note_zu_freq((gi + iv3) % 12, okt)
                     if sc3 > 0 else freq1)

            # Wärme auch gedämpfter
            wärme = 0.15 + phase['energie'] * 0.35

            events.append({
                'start': i * hop,
                'freq': freq1,
                'freq2': freq2,
                'freq3': freq3,
                'vol': vol,
                'wärme': wärme
            })

        erg = self.klang.erzeuge_strom(events, ns)

        peak = np.max(np.abs(erg))
        if peak > 0:
            erg /= peak
            erg = np.tanh(erg * 1.5) / np.tanh(1.5)
            # ── Niedrigerer Master-Pegel ──
            erg *= 0.55  # V5 war 0.85

        return erg


# ============================================================
# AUDIO I/O
# ============================================================

def lade_audio(pfad, sr=22050):
    ext = os.path.splitext(pfad)[1].lower()
    if ext == '.wav':
        sr_f, a = wavfile.read(pfad)
        if a.dtype == np.int16:
            a = a.astype(np.float32) / 32768.0
        elif a.dtype == np.int32:
            a = a.astype(np.float32) / 2147483648.0
        if len(a.shape) > 1:
            a = np.mean(a, axis=1)
        if sr_f != sr:
            n = int(len(a) * sr / sr_f)
            a = np.interp(np.linspace(0, len(a)-1, n),
                          np.arange(len(a)), a)
        return a
    elif ext == '.mp3':
        try:
            import librosa
            a, _ = librosa.load(pfad, sr=sr, mono=True)
            return a
        except ImportError:
            print("  pip install librosa"); sys.exit(1)
    print(f"  '{ext}' nicht unterstützt."); sys.exit(1)


def speichere_wav(audio, pfad, sr=22050):
    ai = np.clip(audio * 32767, -32768, 32767).astype(np.int16)
    wavfile.write(pfad, sr, ai)
    print(f"  → {pfad}")


# ============================================================
# VISUALISIERUNG
# ============================================================

def visualisiere(audio, erg, analyse, phasen, sr, out, gen):
    fig, axes = plt.subplots(5, 1, figsize=(16, 16), sharex=True)
    ta = np.arange(len(audio)) / sr
    te = np.arange(len(erg)) / sr
    tf = analyse['t']

    axes[0].plot(ta, audio, 'blue', lw=0.3, alpha=0.7)
    axes[0].set_ylabel('Amplitude')
    axes[0].set_title('Original')
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(tf, analyse['dc'], 'darkblue', lw=1.5)
    b = analyse['beats']
    if len(b) > 0:
        axes[1].scatter(tf[b], analyse['dc'][b], color='red',
                        s=25, zorder=5, label='Beats')
    axes[1].set_ylabel('Energie')
    axes[1].set_title('Hüllkurve')
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)

    axes[2].imshow(analyse['chroma'], aspect='auto', origin='lower',
                   extent=[tf[0], tf[-1], 0, 12], cmap='magma')
    axes[2].set_yticks(range(12))
    axes[2].set_yticklabels(NOTEN_NAMEN, fontsize=7)
    axes[2].set_ylabel('Ton')
    axes[2].set_title('Chroma')

    axes[3].plot(te, erg, 'green', lw=0.5, alpha=0.8)
    axes[3].set_ylabel('Amplitude')
    axes[3].set_title(f'Harmonics (Gen {gen})')
    axes[3].grid(True, alpha=0.3)

    ml = min(len(audio), len(erg))
    mix = audio[:ml] * 0.75 + erg[:ml] * 0.25
    axes[4].plot(np.arange(ml)/sr, mix, 'purple', lw=0.3, alpha=0.7)
    axes[4].set_ylabel('Amplitude')
    axes[4].set_xlabel('Zeit [s]')
    axes[4].set_title('Mix: Original (75%) + Harmonics (25%)')
    axes[4].grid(True, alpha=0.3)

    fig.suptitle(
        f'ResoMusic V5.1: Dezente Harmonics (Gen {gen})\n'
        'Fließender Klangteppich · Begleitung statt Konkurrenz\n'
        'E = π · ε(Δφ) · ℏ · f, κ = 1',
        fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'reso_music.png'), dpi=150)
    plt.close()
    print(f"  → {out}/reso_music.png")


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("RESOMUSIC V5.1: Dezente fließende Harmonics")
    print("E = π · ε(Δφ) · ℏ · f, κ = 1")
    print("=" * 60)

    out = "figures"
    os.makedirs(out, exist_ok=True)
    sr = 22050

    pfad = None
    passes = 5
    reset = False
    for arg in sys.argv[1:]:
        if arg == '--reset':
            reset = True
        elif arg.isdigit():
            passes = int(arg)
        else:
            pfad = arg

    if not pfad:
        print("\n  python reso_music.py song.mp3 [passes] [--reset]")
        sys.exit(0)

    print(f"\n  Lade: {pfad}")
    audio = lade_audio(pfad, sr=sr)
    print(f"  Dauer: {len(audio)/sr:.1f} s")

    agent = ResoMusik(sr=sr)

    erf_pfad = os.path.join(out, ERFAHRUNG_DATEI)
    if not reset:
        agent.erfahrung.laden(erf_pfad)
    else:
        print("  → Reset")

    print("\n  1. Analyse...")
    analyse, phasen = agent.analysiere(audio)

    gt = {}
    for p in phasen:
        gt[p['grundton']] = gt.get(p['grundton'], 0) + 1
    top = sorted(gt.items(), key=lambda x: x[1], reverse=True)[:4]
    print(f"     {len(phasen)} Frames, {len(analyse['beats'])} Beats")
    print(f"     Grundtöne: {top}")

    print(f"\n  2. Lernen ({passes}×)...")
    for d in range(passes):
        agent.lerne(analyse, phasen)
        if (d+1) % max(1, passes//5) == 0 or d == passes-1:
            print(f"     {d+1}/{passes}: {len(agent.erfahrung.noten)}")

    agent.erfahrung.generation += 1
    agent.erfahrung.songs_gelernt += 1
    agent.erfahrung.statistik()
    agent.erfahrung.speichern(erf_pfad)

    gen = agent.erfahrung.generation
    print(f"\n  3. Harmonics (Gen {gen})...")
    erg = agent.erzeuge(analyse, phasen)
    print(f"     {len(erg)/sr:.1f} s")

    speichere_wav(erg, os.path.join(out, 'reso_harmonics.wav'), sr)

    ml = min(len(audio), len(erg))
    # ── Angepasster Mix: Original dominiert ──
    mix = audio[:ml] * 0.75 + erg[:ml] * 0.25
    speichere_wav(mix, os.path.join(out, 'reso_mix.wav'), sr)

    print("\n  4. Plot...")
    visualisiere(audio, erg, analyse, phasen, sr, out, gen)

    with open(os.path.join(out, 'musik_erfahrung.csv'), 'w') as f:
        f.write("schlüssel,score\n")
        for k, s in sorted(agent.erfahrung.noten.items(),
                           key=lambda x: x[1], reverse=True):
            f.write(f"{k},{s:.6f}\n")

    print(f"\n{'=' * 60}")
    print(f"""
  Gen {gen} | {len(agent.erfahrung.noten)} Noten | {agent.erfahrung.songs_gelernt} Songs

  BALANCE-ÄNDERUNGEN V5.1:
  ────────────────────────
  Basis-Lautstärke:  0.08 → 0.04  (Stille-Überbrückung leiser)
  Energie-Faktor:    0.7  → 0.4   (Laute Stellen gedämpfter)
  Chorus:            0.15 → 0.10  (Weniger Schwebung)
  Obertöne:          h^1.8→ h^2.0 (Schnellerer Abfall)
  2. Stimme:         0.30 → 0.20  (Zweiklang dezenter)
  3. Stimme:         0.15 → 0.08  (Dreiklang fast subliminal)
  Wärme:             0.2+e*0.5 → 0.15+e*0.35
  Master-Pegel:      0.85 → 0.55  (Gesamtlautstärke runter)
  Mix:               60/40 → 75/25 (Original dominiert)

  → figures/reso_harmonics.wav  (Harmonics solo)
  → figures/reso_mix.wav        (75% Original + 25% Harmonics)

  python reso_music.py {pfad} {passes}
""")


if __name__ == "__main__":
    main()