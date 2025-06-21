import numpy as np
import matplotlib.pyplot as plt

# 1. 定義時間軸與訊號
t = np.linspace(-1, 5, 1000)
dt = t[1] - t[0]
x = np.where((t >= 0) & (t <= 4), t, 0)         # 三角波
h = np.exp(-t) * (t >= 0)                      # 指數衰減

# 2. 計算時域卷積 y(t)
y_time = np.convolve(x, h) * dt
t_y = np.linspace(2 * t[0], 2 * t[-1], len(y_time))

# 3. Zero Padding 使 x, h 長度與 y 一致
N = len(t_y)
x_pad = np.zeros(N)
h_pad = np.zeros(N)
x_pad[:len(x)] = x
h_pad[:len(h)] = h

# 4. 計算頻域表示 (傅立葉轉換)
X_f = np.fft.fft(x_pad)
H_f = np.fft.fft(h_pad)
Y_f_theoretical = X_f * H_f
Y_f_actual = np.fft.fft(y_time)

# 5. 擷取正頻率部分
freqs = np.fft.fftfreq(N, d=dt)
positive_freqs = freqs[:N // 2]
mag_theoretical = np.abs(Y_f_theoretical[:N // 2])
mag_actual = np.abs(Y_f_actual[:N // 2])

# 6. 畫出對照圖
plt.figure(figsize=(14, 6))
plt.plot(positive_freqs, mag_theoretical, label="X(f) · H(f)", linewidth=2)
plt.plot(positive_freqs, mag_actual, '--', label="FFT{x * h}", linewidth=2)
plt.title("Verification of Convolution Theorem in Frequency Domain")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
