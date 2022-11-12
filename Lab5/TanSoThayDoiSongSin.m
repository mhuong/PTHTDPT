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