import numpy as np
import matplotlib.pyplot as plt

# 定義連續時間軸（模擬連續訊號用）
t = np.linspace(-1, 5, 1000)  # 時間從 -1 到 5 秒
dt = t[1] - t[0]              # 取樣間距

# 定義 x(t): 線性三角形波
x = np.where((t >= 0) & (t <= 4), t, 0)

# 定義 h(t): 單邊指數衰減（模擬類似濾波器）
h = np.exp(-t) * (t >= 0)

# 計算卷積 y(t) ≈ x(t) * h(t)（數值近似）
y = np.convolve(x, h) * dt
t_y = np.linspace(2 * t[0], 2 * t[-1], len(y))  # 卷積後的時間軸

# 繪圖：三張圖並列，使用不同顏色
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x, color='blue')
plt.title("Signal x(t) (triangular)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t, h, color='green')
plt.title("Signal h(t) (exponential decay)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(t_y, y, color='red')
plt.title("Convolution y(t) = x(t) * h(t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
