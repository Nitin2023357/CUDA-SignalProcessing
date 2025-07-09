# generate_audio.py

import os
import numpy as np
from scipy.io.wavfile import write

os.makedirs("input_data", exist_ok=True)

sample_rate = 44100
duration = 2.0
frequencies = np.linspace(200, 2000, 100)

for i, freq in enumerate(frequencies):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    waveform = 0.5 * np.sin(2 * np.pi * freq * t)
    waveform = (waveform * 32767).astype(np.int16)

    filename = f"input_data/audio_{i}.wav"
    write(filename, sample_rate, waveform)

print("100 small .wav files created in input_data/")
