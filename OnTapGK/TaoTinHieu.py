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

# Tạo tín hiệu 
Fs  =  8000 
x  =  0.5  *  np . cos ( 2  *  np . pi  *  440  *  np . arange ( 0 ,  Fs )  /  Fs ) 
x [ 2000 : 2200 ]  =  2 
print_plot_play ( x = x , Fs = Fs , text = 'Đã tạo tín hiệu:' )

# Ghi tín hiệu 
# Mặc định: 'PCM_16' 
# Tương đương với xử lý trước (phối màu + lượng tử hóa) 
# x = np.int16 (np.round (x * (2 ** 15))) 
# 
print ( 'Mặc định để ghi tệp: ' ,  sf . default_subtype ( 'wav' )) 
fn_out = os.path.join('test6.wav')
sf . write ( fn_out ,  x ,  Fs ,  subtype ='PCM_16' )

# Đọc tín hiệu được tạo ra 
x ,  Fs  =  sf . read ( fn_out ) 
print_plot_play ( x = x , Fs = Fs , text = 'Signal after write and read:' )