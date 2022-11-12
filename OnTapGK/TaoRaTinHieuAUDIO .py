import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# Khởi tạo sóng hình sin
sampling_rate = 6000   #tần số lấy mẫu
frequency = 5000
num_samples = 88200
sine_wave = [0.5]  #biên độ tín hiệu
for x in range(num_samples):
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))

# Lưu sóng hình sin thành Wav file
amplitude = 8000
file = "test2.wav"
wav_file=wave.open(file, 'w')
nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

# Phác họa hình sóng sin
plt.plot(sine_wave[:300])
plt.show()