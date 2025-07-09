# Audio FFT Processing on GPU using CUDA and CuPy

---

## Overview

This project demonstrates the use of GPU acceleration for performing Fast Fourier Transform (FFT) on a large set of audio signals. Using the **CuPy** library (a GPU-accelerated drop-in replacement for NumPy), we compute the FFT of `.wav` audio files and save the results as `.csv` files containing the magnitude spectrum.

The purpose of this project is to show how CUDA and GPU programming can be used for efficient signal processing at scale. The code is structured to handle either:
- 100 small audio files (short-duration samples), or
- 10 large audio files (longer samples)

This project was developed as part of the "CUDA at Scale for the Enterprise" module.

---

## Project Structure

```

CUDA-SignalProcessing/
├── input\_data/           # Contains generated .wav files for processing
├── output\_data/          # Contains FFT output .csv files (generated after execution)
├── main.py               # Main script to perform FFT on audio using GPU
├── generate\_audio.py     # Script to generate synthetic audio files for input
├── requirements.txt      # Python dependencies required to run the project
├── Makefile              # Build system interface for executing commands
├── run.sh                # Shell script for simplified execution
└── README.md             # Project documentation (this file)

````

---

## Key Concepts

- Signal processing on GPU
- FFT using CuPy
- Python automation with Makefile and run.sh
- Batch audio file handling and output generation

---

## Requirements

Install the following software before running the project:

- Python 3.7 or later
- Google Colab (for easy GPU access, optional)
- CuPy with CUDA support (e.g., `cupy-cuda12x`)
- NumPy
- SciPy

You can install all dependencies using the following command:

```bash
pip install -r requirements.txt
````

---

## How to Run the Project

You can run the project on your **local machine** (with an NVIDIA GPU and CuPy installed), or on **Google Colab** using a T4 GPU runtime.

### Option 1: Google Colab (Recommended)

1. Upload the folder `CUDA-SignalProcessing/` to your Google Drive
2. Open a new Google Colab notebook
3. Mount your Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

4. Navigate to the project folder:

```python
%cd /content/drive/MyDrive/CUDA-SignalProcessing
```

5. Install dependencies:

```bash
!pip install -r requirements.txt
```

6. Run the script:

```bash
!python3 main.py
```

### Option 2: Local System (with CUDA)

If you are using a local machine with CUDA and Python installed, follow these steps:

```bash
cd CUDA-SignalProcessing
pip install -r requirements.txt
python3 generate_audio.py   # Generates 100 input files
python3 main.py             # Runs FFT processing on GPU
```

Or use:

```bash
make run
```

To clean output files:

```bash
make clean
```

---

## Output Format

* Each input `.wav` file is processed using GPU-based FFT
* The output is saved as `.csv` with one column containing the magnitude spectrum
* Example:

```
output_data/
├── fft_audio_0.wav.csv
├── fft_audio_1.wav.csv
├── ...
├── fft_audio_99.wav.csv
```

Each `.csv` file contains numeric values corresponding to the magnitude of the FFT bins.

---

## Sample Configuration

The default setup generates:

* 100 `.wav` files
* Each file is 2 seconds long
* Sample rate: 44,100 Hz
* FFT is applied per file and results are written to CSV

These parameters can be easily adjusted in `generate_audio.py` and `main.py`.

---

## How FFT Is Performed

The FFT steps executed in `main.py` are:

1. Load `.wav` audio using `scipy.io.wavfile`
2. Convert to float32 if necessary
3. Transfer signal to GPU using `cupy.asarray()`
4. Compute FFT using `cp.fft.rfft()`
5. Compute magnitude using `cp.abs()`
6. Bring back result to CPU using `cp.asnumpy()`
7. Write result to `.csv`

---

## Makefile Commands

You can automate project tasks with the following make commands:

```bash
make run       # Executes generate_audio.py and main.py
make clean     # Removes all files in output_data/
```

---

## Supported Environment

* GPU: NVIDIA GPU with CUDA 12.x support (T4, A100, etc.)
* OS: Linux, Windows, Google Colab
* CPU Arch: x86\_64
* CUDA Libs: CuPy, NumPy, SciPy

---

## Credits

Developed by Nitin Giri as part of an independent CUDA assignment on signal processing.
This project was implemented to demonstrate scalable GPU-accelerated FFTs on audio data.

---

## License

This project is for educational purposes under course guidelines. No open-source license is currently applied.

```

---
