# BS21010_Seq003
# EEG Analysis Tool

## Overview
This project provides a basic framework for analyzing EEG (Electroencephalogram) data tool. Demonstrating fundamental techniques in EEG signal processing such as preprocessing, frequency domain analysis, and time-frequency analysis. It's designed to assist neuroscientists in processing EEG signals, extracting relevant features, and generating insightful visualizations.

## Features
- Preprocesses EEG signals using bandpass filtering
- Performs frequency domain analysis using Fast Fourier Transform (FFT)
- Conducts time-frequency analysis using spectrogram
- Visualizes results with matplotlib

### Prerequisites
- Python 3.7+
- NumPy
- Matplotlib
- SciPy

You can install the required packages using pip:
pip install numpy matplotlib scipy

## Usage
1. Clone this repository or download the script
2. Run the script using Python
3. The script will generate three plots:
   - Filtered EEG signal
   - Power Spectrum
   - Spectrogram

### Code Structure
- 'preprocess()': Applies a bandpass filter to the EEG data
- 'frequency_analysis()': Performs FFT and calculates the power spectrum
- 'time_frequency_analysis()': Generates a spectrogram of the EEG data

## Customization
- Replacement with own data loading method
- Adjust 'sampling_rate' variable to match the corresponding data's sampling rate
- Modify the bandpass filter parameters in the 'preprocess()' function as needed

## License 

This project is open source


