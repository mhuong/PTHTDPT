% Set Up
sample_rate=10000;
dt=1/sample_rate;
len=0.01;
t=0:dt:(len-dt);
f=500;
N = length(t);
% Generate signal
signal=sin(2*pi*f*t);
% Define a phase shift
phase = pi/4;
num_samp =
round((sample_rate/f)
*(phase/(2*pi)));
% Get the FFT of the signal
signalfft =fft(signal);
% Rotate each FFT component
k=1:length(signalfft);
% Range of Phasor phase values
w = 2*pi/N*(k-1);
spec=signalfft.*
exp(-j*w*num_samp);
% Get the new signal
newsignal=(ifft(spec));
% Plot the signals
figure;plot(t,real(signal));
hold on;
plot(t,real(newsignal),'g');

% Rotate each FFT component
k=1:length(signalfft);
% Range of Phasor phase values
w = 2*pi/N*(k-1);
spec=signalfft.*exp(-j*w*num_samp);