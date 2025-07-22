# FFT-Convolution-Lab

## Introduction

This project explores and validates key concepts in the time and frequency domains through hands-on signal processing techniques. It demonstrates waveform synthesis, spectral analysis... .

## Mathematical Background

### Time-Domain Convolution

Convolution describes how the shape of one signal is modified by another. For continuous signals:

$$
(f * g)(t) = \int_{-\infty}^{\infty} f(\tau)\, g(t - \tau) \, d\tau
$$

For discrete signals (used in digital signal processing):

$$
(f * g)[n] = \sum_{k=-\infty}^{\infty} f[k] \cdot g[n - k]
$$

In practical applications, we compute over finite-length signals, so the summation limits are bounded.

### Frequency-Domain Representation

The Discrete Fourier Transform (DFT) of a discrete signal $x[n]$ is defined as:

$$
X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-j \frac{2\pi kn}{N}}
$$

And the inverse transform (IDFT) is:

$$
x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] \cdot e^{j \frac{2\pi kn}{N}}
$$

Fast Fourier Transform (FFT) is a fast algorithm to compute the DFT in $O(N \log N)$ time.

## Convolution Theorem

The **convolution theorem** establishes a duality between time and frequency domains:

$$
\mathcal{F}\{f * g\} = \mathcal{F}\{f\} \cdot \mathcal{F}\{g\}
$$

That is, convolution in the time domain corresponds to pointwise multiplication in the frequency domain. If:

- $F = \mathcal{F}\{f\}$
- $G = \mathcal{F}\{g\}$

Then:

$$
\mathcal{F}\{f * g\} = F \cdot G
$$

Conversely, multiplication in the time domain corresponds to convolution in the frequency domain:

$$
\mathcal{F}\{f \cdot g\} = F * G
$$

### Practical Application with FFT

To compute convolution using the FFT:

1. Compute $F = \text{FFT}(f)$ and $G = \text{FFT}(g)$
2. Multiply: $H = F \cdot G$
3. Compute inverse FFT: $h = \text{IFFT}(H)$

This approach is computationally efficient and often used in large-scale signal processing tasks.


## Features

- Generate and visualize composite signals with various frequency components
- Perform Fast Fourier Transform (FFT) and inverse FFT (IFFT)
- Apply basic noise filtering by removing high-frequency components
- Load and analyze real-world audio (.wav) files
- Simulate one-dimensional convolution of signals in the time domain
- Verify the convolution theorem using frequency-domain analysis


##  Project Structure

```
FFT-Convolution-Lab/
├── 1-1/
│   ├── clean_signal.py         # Generate clean composite signal
│   ├── noisy_signal.py         # Add high-frequency noise
│   ├── FFT.py                  # Frequency analysis
│   ├── IFFT.py                 # Restore signal after filtering
├── 1-2/
│   ├── FFT.py                  # Spectrum analysis of real audio
│   ├── Piano.wav               # Input audio file (29s)
├── 2/
│   ├── convolution.py          # Time-domain convolution simulation
│   ├── validation.py           # Verify convolution theorem via FFT
```


##  Run

Navigate to any folder and run the desired script, for example:

```bash
cd 1-1
python clean_signal.py
```

All plots will display inline via `matplotlib`.


