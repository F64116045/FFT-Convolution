import numpy as np
import matplotlib.pyplot as plt

# Sampling settings
fs = 1000  # Sampling frequency in Hz
t = np.linspace(0, 1, fs, endpoint=False)  # Time axis: 1 second, 1000 samples

# Synthesize clean signal: 50Hz and 120Hz sine waves
f1 = 50
f2 = 120
signal_clean = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Plot the clean signal
plt.figure(figsize=(10, 4))
plt.plot(t, signal_clean, label='50Hz + 0.5×120Hz')
plt.title("Clean Synthesized Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
