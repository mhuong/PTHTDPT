%Cơ bản 1 tiết Sóng sin đơn giản
i=0:0.2:2*pi;
y = sin(i);
figure(1)
plot(y);
% sử dụng gốc (y) làm biểu đồ thay thế như trong ghi chú bài giảng
% để xem các giá trị mẫu
title('Simple 1 Period Sine Wave');
% Now Change amplitude
amp = 2.0;
y = amp*sin(i);
figure(2)
plot(y);
title('Simple 1 Period Sine Wave Modified Amplitude');