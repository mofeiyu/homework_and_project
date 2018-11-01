clear
clc
 
% Read the image
grayLena = imread('lena.png');
figure(1);
imshow(grayLena);  % Display the image

%% Complement image
figure(2);
subplot(1,3,1);
imshow(grayLena);
title('Gray Lena');
% Solution 1
invGrayLena1=255-grayLena;
subplot(1,3,2);
imshow(invGrayLena1);
title('complement Lena Solution 1');
% Solution 2
invGrayLena2=imcomplement(grayLena);
subplot(1,3,3);
imshow(invGrayLena2);
title('complement Lena Solution 2');
%% bitplane 
figure(3);
plane4Lena=bitget(grayLena,4); 
imshow(logical(plane4Lena));

%% write image files
imwrite(invGrayLena1,"InvGrayLena.png");
