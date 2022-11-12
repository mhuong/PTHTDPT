clear all, close all;

% Nhiều lần lặp lại Chroma lấy mẫu con
imRGB = imread('parrots.jpg');
figure,  imshow(imRGB), title('RGB Full Image');
imYIQ = rgb2ntsc(imRGB);

for i = 1:1000  % Mô phỏng sao chép nhiều lần 1000 lần!
% Lấy mẫu con Kênh I và Kênh Q 4: 2: 0 Lấy mẫu
imYIQsubI = imresize(imYIQ(:,:,2),0.5,'bilinear');
imYIQsubQ = imresize(imYIQ(:,:,3),0.5, 'bilinear');

%Chúng tôi có hình ảnh kích thước nên sao lưu lại mẫu
imYIQupsampI = imresize(imYIQsubI,2);
imYIQupsampQ = imresize(imYIQsubQ,2);


imYIQ(:,:,2) = imYIQupsampI;
imYIQ(:,:,3) = imYIQupsampQ;


end
% Làm lại RGB và hiển thị
reconstruct_imRGB = uint8(256*ntsc2rgb(imYIQ));
figure, imshow(reconstruct_imRGB); title('Reconstructed (1000 Iterations) RGB Full Image');


% hiển thị lỗi mặt phẳng R, G, B
figure, imshow(256*abs(imRGB(:,:,1) - reconstruct_imRGB(:,:,1))); title('Reconstructed (1000 Iterations) R Error');
figure, imshow(256*abs(imRGB(:,:,2) - reconstruct_imRGB(:,:,2))); title('Reconstructed (1000 Iterations) G Error');
figure, imshow(256*abs(imRGB(:,:,3) - reconstruct_imRGB(:,:,3))); title('Reconstructed (1000 Iterations) B Error');
