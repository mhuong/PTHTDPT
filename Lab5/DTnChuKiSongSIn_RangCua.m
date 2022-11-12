% Natural frequency is 2*pi radians
% If sample rate is F_s HZ then 1 HZ is 2*pi/F_s
% If wave frequency is F_w then freequency is F_w* (2*pi/F_s)
% set n samples steps up to sum duration nsec*F_s where
% nsec is the duration in seconds
% So we get y = amp*sin(2*pi*n*F_w/F_s);
F_s = 11025;
F_w = 440;
nsec = 2;
dur= nsec*F_s;
n = 0:dur;
y = amp*sin(2*pi*n*F_w/F_s);
figure(3)
plot(y(1:500));
title('N second Duration Sine Wave');

% To plot n cycles of a waveform
ncyc = 2;
n=0:floor(ncyc*F_s/F_w);
y = amp*sin(2*pi*n*F_w/F_s);
figure(4)
plot(y);
title('N Cycle Duration Sine Wave');

% MATLAB Dạng sóng hình vuông và răng cưa
% Square and Sawtooth Waveforms created using Radians
ysq = amp*square(2*pi*n*F_w/F_s);
ysaw = amp*sawtooth(2*pi*n*F_w/F_s);
figure(6);
hold on
plot(ysq,'b');
plot(ysaw,'r');
title('Square (Blue)/Sawtooth (Red) Waveform Plots');
hold off;