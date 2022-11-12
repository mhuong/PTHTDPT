import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Tỷ lệ mẫu
seconds = 3  #  time ghi

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Chờ cho đến khi bản ghi hoàn tất
write('output.wav', fs, myrecording)  # Lưu dưới dạng WAV File 