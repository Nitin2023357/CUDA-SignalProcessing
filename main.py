# main.py

import os
import numpy as np
import cupy as cp
from scipy.io import wavfile
import csv


INPUT_DIR = "input_data"
OUTPUT_DIR = "output_data"   


# Make sure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Loop through all .wav files in the input directory
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".wav"):
        input_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, f"fft_{filename}.csv")

        print(f"Processing: {filename}")

        # Read audio file
        sample_rate, data = wavfile.read(input_path)

        # Handle stereo by using only one channel
        if len(data.shape) == 2:
            data = data[:, 0]

        # Convert to float32
        signal = data.astype(np.float32)

        # Send signal to GPU using CuPy
        signal_gpu = cp.asarray(signal)

        # Compute FFT on GPU
        fft_gpu = cp.fft.rfft(signal_gpu)

        # Compute magnitude spectrum
        magnitude_gpu = cp.abs(fft_gpu)

        # Transfer back to CPU
        magnitude = cp.asnumpy(magnitude_gpu)

        # Save magnitude spectrum to CSV
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            for val in magnitude:
                writer.writerow([val])

print("All audio files processed and saved to CSV.")
