# Spectrum-of-Sampled-Signal-for-a-Given-Sinusoidal-Signal-Using-Impulse-Train
Signal Sampling and Frequency Domain Analysis
This project demonstrates signal sampling using an impulse train and analyzes both the time-domain and frequency-domain behavior of the sampled signal using FFT (Fast Fourier Transform). It provides visual insights into the original signal, the impulse train, the sampled signal, and their frequency spectra.

📁 Project Structure
bash
Copy code
├── sampling_frequency_analysis.py  # Main script to generate and analyze sampled signals  
├── requirements.txt                # List of dependencies  
└── README.md                       # Documentation of the project  
🚀 How It Works
1. Signal Sampling
The original signal 
𝑚
(
𝑡
)
m(t) is a sine wave with a frequency of 5 Hz.
An impulse train is generated at a sampling frequency 
𝑓
𝑠
=
100
 
𝐻
𝑧
f 
s
​
 =100Hz.
The sampled signal is obtained by multiplying the original signal with the impulse train.
2. Frequency Domain Analysis
The FFT of the original, impulse train, and sampled signals is computed.
Frequency spectra are plotted to visualize how the original signal is affected by sampling.
📦 Dependencies
Install the required dependencies using:

bash
Copy code
pip install -r requirements.txt
requirements.txt:

Copy code
numpy
matplotlib
📝 Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/signal-sampling-analysis.git
cd signal-sampling-analysis
Run the Script:

bash
Copy code
python sampling_frequency_analysis.py
Expected Output:

A six-panel plot showing:
Original Signal in the time domain.
Impulse Train in the time domain.
Sampled Signal in the time domain.
Frequency Spectrum of the Original Signal.
Frequency Spectrum of the Impulse Train.
Frequency Spectrum of the Sampled Signal.
📊 Code Overview
python
Copy code
# Parameters
t = np.linspace(0, 1, 100)          # Time vector
mt = np.sin(2 * np.pi * 5 * t)      # Original sine wave signal (5 Hz)
fs = 100                            # Sampling frequency
Ts = 1 / fs                         # Sampling period
n = np.arange(0, 1 + Ts, Ts)        # Time points for the impulse train

# Generate Impulse Train
delta_n = np.zeros_like(t)
for i in range(len(n)):
    delta_n[np.abs(t - n[i]) < Ts/2] = 1

# Generate Sampled Signal
m_sampled = mt * delta_n

# Frequency Domain Calculations
N = len(t)                          # Number of samples
f = np.fft.fftfreq(N, t[1] - t[0])  # Frequency vector

M_f = np.fft.fftshift(np.abs(np.fft.fft(mt) / N))  # FFT of original signal
Delta_f = np.abs(np.fft.fft(delta_n))               # FFT of impulse train
M_sampled_f = np.abs(np.fft.fft(m_sampled))         # FFT of sampled signal
🎯 Features
Visualizes time-domain and frequency-domain properties of sampled signals.
Demonstrates sampling theory and how an impulse train affects a signal.
Easy to modify the signal frequency, sampling rate, and plotting behavior.
🛠 Troubleshooting
Incorrect FFT Plot: Ensure that the time vector and sampling frequency are correctly aligned.
Python Compatibility: Tested on Python 3.8+.
📄 License
This project is licensed under the MIT License - see the LICENSE file for more details.

💡 Contributing
Feel free to submit issues or pull requests if you have suggestions for improvement.

👨‍💻 Author
Vijay Bhushan Singh
