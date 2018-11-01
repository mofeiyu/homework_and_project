clear
clc

%% Read the image
colorLena=imread('colorLena.png');
figure(1);
imshow(colorLena);


%% Color Channels
figure(2);
% extract the three channel(a 512*512 matrix) 
redChannel = colorLena(:,:,1); 
greenChannel = colorLena(:,:,2); 
blueChannel = colorLena(:,:,3);

% z = zeros(512, 512);
% r = cat(3, redChannel, z, z);
% g = cat(3, z, greenChannel, z);
% b = cat(3, z, z, blueChannel);

subplot(1,3,1);
imshow(redChannel), title('Red channel')
subplot(1,3,2);
imshow(greenChannel), title('Green channel')
subplot(1,3,3);
imshow(blueChannel), title('Blue channel')

%% RGB to HSV
hsvLena = rgb2hsv(colorLena);
hChannel = hsvLena(:,:,1); 
sChannel = hsvLena(:,:,2); 
vChannel = hsvLena(:,:,3);
figure(3);
subplot(1,3,1);
imshow(hChannel), title('H channel')
subplot(1,3,2);
imshow(sChannel), title('S channel')
subplot(1,3,3);
imshow(vChannel), title('V channel')

%% Thresholding
figure(4);
threshold=200;
% if a pixel in redChannel is larger than the threshold
% it becomes true, otherwise it is false
BWR=redChannel>threshold; 
imshowpair(redChannel,BWR,'montage');

%% image segmentation
figure(5);
% Convert BWR to unit8, the same data type as 8-bit RGB image.
BWR = uint8(BWR); 
segLena=colorLena;
% Dot multiply each channel with the mask
segLena (:,:,1) = segLena (:,:,1).*BWR;
segLena (:,:,2) = segLena (:,:,2).*BWR;
segLena (:,:,3) = segLena (:,:,3).*BWR;
imshow(segLena);

%% histogram
figure(6);
imhist(redChannel);