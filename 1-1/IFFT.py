import numpy as np
import matplotlib.pyplot as plt

# 時間與訊號參數
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
f1, f2, f_noise = 50, 120, 300

# 合成訊號與高頻雜訊
signal_clean = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)
noise = 0.3 * np.sin(2 * np.pi * f_noise * t)
signal_noisy = signal_clean + noise

# FFT 分析
fft_vals = np.fft.fft(signal_noisy)
freqs = np.fft.fftfreq(len(t), d=1/fs)

# 濾波：移除高於 200Hz 的頻率成分
cutoff = 200
fft_filtered = fft_vals.copy()
fft_filtered[np.abs(freqs) > cutoff] = 0

# IFFT：還原濾波後訊號
signal_filtered = np.fft.ifft(fft_filtered).real

# 畫圖：濾波後的時域波形（圖 4）
plt.figure(figsize=(10, 4))
plt.plot(t, signal_filtered, label="Filtered Signal", color="tab:blue")
plt.title("Filtered Signal After Removing High-Frequency Noise (>200Hz)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
