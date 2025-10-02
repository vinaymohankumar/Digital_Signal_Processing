import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fs = 2000      # Sampling frequency (Hz)
T = 1/Fs       # Sampling interval
N = 2000       # Number of samples
t = np.arange(0, N*T, T)

# Define (frequency, amplitude) pairs
signals = [(50, 1.0), (150, 0.5), (300, 0.1)]  # (Hz, amplitude)

# Create signal as sum of sinusoids
x = np.zeros_like(t)
for f, A in signals:
    x += A * np.sin(2 * np.pi * f * t)

# Compute FFT
X = np.fft.fft(x) / N   # normalize
freqs = np.fft.fftfreq(N, T)

# Take only positive half of the spectrum
half = N
X_mag = np.abs(X[:half])
freqs_half = freqs[:half]

# Plot time domain
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(t, x)
plt.title("Time Domain Signal (Multiple Frequencies with Amplitudes)")
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
