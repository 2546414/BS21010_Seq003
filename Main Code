import numpy as np
import matplotlib.pyplot as plt
from scipy import signal 
from scipy.fft import fft, fftfraq

# Preprocessing
def preprocess(data):
  b, a = signal.butter(4, [0.5, 50], btype= 'bandpass', fs=sampling_rate)
  filtered_data = signal.filtfilt(b, a, data)
  return filtered_data

filtered_eeg = preprocess(eeg_data)

# Frequency domain analysis
def frequency_analysis(data): 
  n = len(data)
  fft_result = fft(data)
  freqs = fftfreq(n, 1/sampling_rate)
  return freqs[:n//2], np.abs(fft_result)[:n//2]

freqs, power = frequency_analysis(flitered_eeg)

# Time-frequency analysis
def time_frequency_analysis(data):
  f, t, Sxx = signal.spectrogram(data, fs=sampling_rate)
  return f, t, Sxx

f, t, Sxx= time_frequency_analysis(flitered_eeg)
freqs, power = frequency_analysis(filtered_eeg)
f, t, Sxx = time_frequency_analysis(filtered_eeg)

# Plotting
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(time, filtered_eeg)
plt.title('Filtered EEG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(freqs, power)
plt.title('Power Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')

plt.subplot(3, 1, 3)
plt.pcolormesh(t, f, 10 * np.log10(Sxx))
plt.title('Spectrogram')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

plt.tight_layout()
plt.show()



