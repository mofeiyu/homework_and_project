%% Task 2 Color Image Processing

%% read image 'Flowers.jpg', 
flowers = imread('Flowers.jpg');


%% 1. Complement Image. (1 point)
%   1.1 compute complement image of Flowers.
%   1.2 save it to 'negativeFlowers.jpg'
invFlowers=255-flowers;    % 1.1 compute complement image of Flowers.
imwrite(invFlowers, 'negativeFlowers.jpg')    % 1.2 save it to 'negativeFlowers.jpg'


%% 2. Modify image saturation. (1 point)
%   2.1 convert flowers to HSV format
%   2.2 reduce Saturation of all pixels to half
%   2.3 convert back to RGB format.
%   2.4 save it to 'LessColorfulFlowers.jpg'
hsvFlowers = rgb2hsv(flowers);    % 2.1 convert flowers to HSV format
hsvFlowers(:,:,2) = hsvFlowers(:,:,2)*0.5;    % 2.2 reduce Saturation of all pixels to half
rgbFlowers = hsv2rgb(hsvFlowers);    % 2.3 convert back to RGB format.
imwrite(rgbFlowers, 'LessColorfulFlowers.jpg')    % 2.4 save it to 'LessColorfulFlowers.jpg'


%% 3. Image Segmentation. (0.5 point)
%   3.1 separate yellow flowers from the background
%   3.2 save it to 'segFlowers.jpg'
%
%   Tips:
%       1. Yellow is a mix of red and green, and contains little blue.
%       2. Element-wise logical and operator '&' may help you.
%       3. Segmentation may not be perfect. It's OK.
redChannel = flowers(:,:,1);    % extract red channel
greenChannel = flowers(:,:,2);  % extract green channel
blueChannel = flowers(:,:,3);   % extract blue channel
BWR=redChannel>165;    % set red channel booling values by low thresold value 165
BWG=greenChannel>115;  % set red channel booling values by low thresold value 115
BWB=blueChannel<70;    % set red channel booling values by top thresold value 70
combine_bool =BWR&BWG&BWB;    % '&' combine three channels booling values
flowers(:,:,1) = flowers(:,:,1).*uint8(combine_bool);    % convert combine_bool to unit8 and filter red channel
flowers(:,:,2) = flowers(:,:,2).*uint8(combine_bool);    % convert combine_bool to unit8 and filter green channel
flowers(:,:,3) = flowers(:,:,3).*uint8(combine_bool);    % convert combine_bool to unit8 and filter blue channel
figure(1)
imshow(flowers);    % show the new image
imwrite(flowers, 'segFlowers.jpg')    % save image




