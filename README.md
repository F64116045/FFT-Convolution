# FFT & Convolution

Exploring and validating key concepts in time and frequency domains.  
Demonstrates waveform synthesis, spectral analysis, 1D convolution, and the convolution theorem.

##  Features
- Generate and visualize composite signals with various frequency components
- Perform Fast Fourier Transform (FFT) and inverse FFT (IFFT)
- Apply noise filtering by removing high-frequency components
- Load and analyze real-world audio (.wav) files
- Simulate 1D convolution of two signals in the time domain
- Verify the convolution theorem in the frequency domain

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


