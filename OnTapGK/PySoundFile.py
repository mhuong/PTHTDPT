import soundfile as sf
import os
import numpy as np
from matplotlib import pyplot as plt
import IPython.display as ipd
import pandas as pd
'exec(%matplotlib inline)'

def print_plot_play(x, Fs, text=''):
    """1. Prints information about an audio singal, 2. plots the waveform, and 3. Creates player
    
    Notebook: C1/B_PythonAudio.ipynb
    
    Args: 
        x: Input signal
        Fs: Sampling rate of x    
        text: Text to print
    """
    print('%s Fs = %d, x.shape = %s, x.dtype = %s' % (text, Fs, x.shape, x.dtype))
    plt.figure(figsize=(8, 2))
    plt.plot(x, color='gray')
    plt.xlim([0, x.shape[0]])
    plt.xlabel('Time (samples)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()
    ipd.display(ipd.Audio(data=x, rate=Fs))

# Đọc test.wav với mặc định
fn_wav = os.path.join('test.wav')
x, Fs = sf.read(fn_wav)
print_plot_play(x=x,Fs=Fs,text='WAV file (default): ')

# Đọc wav với dtype = 'int16' 
fn_wav = os.path.join('test.wav')
x, Fs = sf.read(fn_wav, dtype= 'int16')
print_plot_play(x=x,Fs=Fs,text='WAV file (dtype=int16): ')

#Viết tín hiệu 'int16' và đọc với 
fn_out = os.path.join('test3.wav')
sf.write(fn_out, x, Fs)
x, Fs = sf.read(fn_out)
print_plot_play(x=x,Fs=Fs,text='Tín hiệu (int16) sau khi ghi và đọc (mặc định): ')