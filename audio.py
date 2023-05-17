# References: https://stackoverflow.com/questions/65185061/how-to-get-a-list-of-frequencies-in-a-wav-file


from scipy.io import wavfile as wav
import numpy as np
from PIL import Image 

rate, data = wav.read('toImage3.wav')

duration = 1.0 # 1s chunk includes delimiting 5ms 1600hz tone
chunk = int(rate * duration) # calculate the length of our chunk in the np.array using sample rate
offset = int(rate * 0.005) # length of delimiting 1600hz tone
bits = int(len(data) / chunk) # number of bits in the audio data to decode

# ==================================================================
def get_freq(bit):
    
    strt = (chunk * bit) # start position of the current bit
    end = (strt + chunk) - offset # remove the delimiting 1600hz tone
    sliced = data[strt:end] # slice the array for each bit
    w = np.fft.fft(sliced)
    freqs = np.fft.fftfreq(len(w))

    # Find the peak in the coefficients
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * rate)
    return freq_in_hertz

# ====================================================================
def build_image(freqs):

    sound_list = [round(num) for num in freqs]

    w = len(sound_list)
    h =  len(sound_list)
    sound_im = Image.new('RGB', (w,h))

    target_x = 0
    for source_x in range(w):
        target_y = 0
        for source_y in range(h):
            # p = my_src.getpixel((source_x, source_y))
            #hertz value from list
            sound_im.putpixel((target_x, target_y), (sound_list[source_y] , sound_list[source_y], sound_list[source_x], 255 ))
            target_y += 1
        target_x += 1

    sound_im.show()


decoded_freqs = [get_freq(bit) for bit in range(bits)]
print(decoded_freqs)
build_image(decoded_freqs)
