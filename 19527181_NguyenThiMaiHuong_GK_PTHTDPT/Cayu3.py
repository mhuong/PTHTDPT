#a,Phân biệt tần số lấy mẫu và tần số tín hiệu
#b,Viết code tạo ra một sóng hình sin với tần số là 2000,biên độ là 10000,tần số lấy mâuc là 48000
#Giải thíc code
import numpy as np

import wave

import struct

import matplotlib.pyplot as plt

# Tần số là số lần sóng lặp lại một giây

frequency = 2000

num_samples = 48000

# Tỷ lệ lấy mẫu của chuyển đổi từ tương tự sang kỹ thuật số

sampling_rate = 48000.0

amplitude = 10000

file = "test10.wav"
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]
nframes=num_samples

comptype="NONE"

compname="not compressed"

nchannels=1

sampwidth=2
wav_file=wave.open(file, 'w')

wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
       wav_file.writeframes(struct.pack('h', int(s*amplitude)))
struct.pack('h', int(s*amplitude))


