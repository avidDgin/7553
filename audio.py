from scipy.io import wavfile as wav

import numpy as np

rate, data = wav.read('newsong.wav')

# 1s chunk includes delimiting 5ms 1600hz tone
duration = 1.0

# calculate the length of our chunk in the np.array using sample rate
chunk = int(rate * duration)

# length of delimiting 1600hz tone
offset = int(rate * 0.005)

# number of bits in the audio data to decode
bits = int(len(data) / chunk)

def get_freq(bit):
    # start position of the current bit
    strt = (chunk * bit) 
    
    # remove the delimiting 1600hz tone
    end = (strt + chunk) - offset
    
    # slice the array for each bit
    sliced = data[strt:end]

    w = np.fft.fft(sliced)
    freqs = np.fft.fftfreq(len(w))

    # Find the peak in the coefficients
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * rate)
    return freq_in_hertz

decoded_freqs = [get_freq(bit) for bit in range(bits)]

print(decoded_freqs)