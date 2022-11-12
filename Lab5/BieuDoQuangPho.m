load('handel')
[N M] = size(y);
figure(1)
spectrogram(y,512,20,1024,Fs);