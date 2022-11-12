I = imread(’cameraman.tif’);
BW = dither(I);
imshow(BW);