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

# FFT：進行頻域分析
fft_vals = np.fft.fft(signal_noisy)  # 對雜訊訊號做傅立葉轉換
fft_magnitude = np.abs(fft_vals) / len(t)  # 取絕對值並正規化
freqs = np.fft.fftfreq(len(t), d=1/fs)  # 對應的頻率軸

# 只取正頻率部分
positive_freqs = freqs[:len(freqs)//2]
positive_magnitude = fft_magnitude[:len(freqs)//2]

# 畫頻譜圖
plt.figure(figsize=(10, 4))
plt.plot(positive_freqs, positive_magnitude)
plt.title("Frequency Spectrum of Noisy Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()
