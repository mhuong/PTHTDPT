clear all, close all;

% Lấy mẫu con Chroma lặp lại một lần
imRGB = imread('parrots.jpg');
figure,  imshow(imRGB), title('RGB Full Image');
imYIQ = rgb2ntsc(imRGB);

% Lấy mẫu phụ các Kênh I và Q 4: 2: 0 Loại Lấy mẫu phụ, ví dụ: Nhưng đặt tỷ lệ thành
% một phần tám. 'bilinear' lấy mẫu
imYIQsubI = imresize(imYIQ(:,:,2),0.125,'bilinear');
imYIQsubQ = imresize(imYIQ(:,:,3),0.125,'bilinear');

% Chúng tôi có hình ảnh kích thước nên sao lưu lại mẫu
imYIQupsampI = imresize(imYIQsubI,8);
imYIQupsampQ = imresize(imYIQsubQ,8);
reconstruct_imYIQ= imYIQ;  % Copy YIQ keep Y;
reconstruct_imYIQ(:,:,2) = imYIQupsampI;
reconstruct_imYIQ(:,:,3) = imYIQupsampQ;
% Làm lại RGB và hiển thị
reconstruct_imRGB = uint8(256*ntsc2rgb(reconstruct_imYIQ));
figure, imshow(reconstruct_imRGB); title('Reconstructed RGB Full Image');

% hiển thị lỗi mặt phẳng R, G, B
figure, imshow(abs(imRGB(:,:,1) - reconstruct_imRGB(:,:,1))); title('Reconstructed R Error');
figure, imshow(abs(imRGB(:,:,2) - reconstruct_imRGB(:,:,2))); title('Reconstructed G Error');
figure, imshow(abs(imRGB(:,:,3) - reconstruct_imRGB(:,:,3))); title('Reconstructed B Error');
