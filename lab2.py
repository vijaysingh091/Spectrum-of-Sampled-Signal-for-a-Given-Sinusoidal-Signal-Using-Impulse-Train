import numpy as np
import matplotlib.pyplot as plt

# Parameters
t = np.linspace(0, 1, 100)
mt = np.sin(2 * np.pi * 5 * t)

fs = 100
Ts = 1 / fs
n = np.arange(0, 1 + Ts, Ts)

# Impulse train delta_n
delta_n = np.zeros_like(t)
for i in range(len(n)):
    delta_n[np.abs(t - n[i]) < Ts/2] = 1

# Sampled signal
m_sampled = mt * delta_n

# Frequency domain calculations
N = len(t)
f = np.fft.fftfreq(N, t[1] - t[0])

M_f = np.fft.fftshift(np.abs(np.fft.fft(mt) / N))
Delta_f = np.abs(np.fft.fft(delta_n))
M_sampled_f = np.abs(np.fft.fft(m_sampled))

# Plotting
plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.plot(t, mt, linewidth=1.5)
plt.title('Original Signal m(t)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 3)
(stemlines, stemmarkers, baseline) = plt.stem(t, delta_n, 'r', markerfmt='ro', basefmt=" ")
plt.setp(stemlines, linewidth=1.5)
plt.title('Impulse Train')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 5)
(stemlines, stemmarkers, baseline) = plt.stem(t, m_sampled, 'g', markerfmt='go', basefmt=" ")
plt.setp(stemlines, linewidth=1.5)
plt.title('Sampled Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 2)
plt.plot(np.fft.fftshift(f), M_f, linewidth=1.5)
plt.title('Spectrum of Message Signal m(t)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.subplot(3, 2, 4)
plt.plot(f, Delta_f, linewidth=1.5)
plt.title('Spectrum of Impulse Train')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.subplot(3, 2, 6)
plt.plot(f, M_sampled_f, linewidth=1.5)
plt.title('Spectrum of Sampled Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
