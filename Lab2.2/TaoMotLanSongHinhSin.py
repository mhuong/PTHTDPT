import numpy as np

import wave

import struct

import matplotlib.pyplot as plt

# Tần số là số lần sóng lặp lại một giây

frequency = 1000

num_samples = 48000

# Tần số là số lần sóng lặp lại một giây

sampling_rate = 48000.0

amplitude = 16000

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


