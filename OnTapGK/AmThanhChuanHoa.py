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

Fs = 8000
x = 0.1 * np.cos(2 * np.pi * 440 * np.arange(0, 2 * Fs) / Fs)

plt.figure(figsize=(6, 1.5))
plt.plot(x, color='gray')
plt.xlim([0, x.shape[0]])
plt.ylim([-1, 1])
plt.xlabel('Time (samples)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

print('Audio playback with default settings (normalized audio)')
ipd.display(ipd.Audio(data=x, rate=Fs))

print('Audio playback without normalization (original audio) ')
ipd.display(ipd.Audio(data=x, rate=Fs, normalize=False))