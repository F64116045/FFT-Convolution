import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 1. 讀取音訊檔（請自行確認檔名與路徑正確）
sample_rate, data = wavfile.read("Piano.wav")  # 可改成你的音訊檔名

# 2. 若為雙聲道音訊（Stereo），取單聲道（左聲道）
if data.ndim == 2:
    data = data[:, 0]

# 3. 畫出音訊波形圖（前 1 秒）
duration_sec = 1
samples_to_plot = int(sample_rate * duration_sec)
time_axis = np.linspace(0, duration_sec, samples_to_plot, endpoint=False)

plt.figure(figsize=(12, 4))
plt.plot(time_axis, data[:samples_to_plot], color='orange')
plt.title("Raw Audio Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. 計算 FFT 並畫出頻譜圖
N = len(data)
fft_vals = np.fft.fft(data)
fft_magnitude = np.abs(fft_vals) / N
freqs = np.fft.fftfreq(N, d=1/sample_rate)

# 5. 只取正頻率部分
pos_freqs = freqs[:N // 2]
pos_magnitude = fft_magnitude[:N // 2]

plt.figure(figsize=(12, 4))
plt.plot(pos_freqs, pos_magnitude)
plt.title("Frequency Spectrum of Audio")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()
