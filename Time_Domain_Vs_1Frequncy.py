import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 1000      # Sampling frequency (Hz)
T = 1/Fs       # Sampling interval
N = 1000       # Number of samples
t = np.arange(0, N*T, T)

# Signal: sine wave
f_sig = 50  # signal frequency in Hz
x = np.sin(2 * np.pi * f_sig * t)

# Compute FFT
X = np.fft.fft(x) / N   # normalize
freqs = np.fft.fftfreq(N, T)  # frequency bins

# Take only positive half of the spectrum
half = N // 2
X_mag = np.abs(X[:half])
freqs_half = freqs[:half]

# Plot time domain
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(t, x)
plt.title("Time Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot frequency domain
plt.subplot(1,2,2)
plt.stem(freqs_half, X_mag, use_line_collection=True)
plt.title("Frequency Domain (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()
plt.show()
