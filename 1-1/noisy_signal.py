import numpy as np
import matplotlib.pyplot as plt

# Sampling settings
fs = 1000  # Sampling frequency in Hz
t = np.linspace(0, 1, fs, endpoint=False)  # Time axis: 1 second, 1000 samples

# Synthesize clean signal: 50Hz and 120Hz sine waves
f1 = 50
f2 = 120
signal_clean = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)


f_noise = 300
noise = 0.3 * np.sin(2 * np.pi * f_noise * t)

# Combine the clean signal with high-frequency noise
signal_noisy = signal_clean + noise

# Plot the noisy signal
plt.figure(figsize=(10, 4))
plt.plot(t, signal_noisy, label='Noisy Signal (with 300Hz)')
plt.title("Signal with High-Frequency Noise")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Only plot 300Hz noise
plt.figure(figsize=(10, 4))
plt.plot(t, noise)
plt.title("Pure 300Hz Noise")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
