#!/bin/bash

echo "📦 Installing required Python packages..."
pip install -r requirements.txt

echo "🚀 Running audio FFT processing script..."
python3 main.py
