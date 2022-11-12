
im = imread('cameraman.tif'); %Tải hình ảnh

di = 4*ones(4,4);  % THAY THẾ BẰNG MATRIX Phối màu CHUYÊN NGHIỆP
[m n] = size(im); % Có được kích thước hình ảnh		
mat = repmat(di, m/4, n/4); % Lặp lại ma trận với cùng kích thước
im = im / 17; % Ánh xạ cường độ thành 0-16
dithered = im > mat; % Đặt 1 khi mục nhập có im > mat 	
imshow(dithered); % Hiển thị hình ảnh hòa sắc


