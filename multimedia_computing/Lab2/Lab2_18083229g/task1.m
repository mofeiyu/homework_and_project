%% Task 1 Gray Image Processing

%% 1. Basic image read, write and display. (1 point)
%   1.1 read 'lena.bmp' by imread.
%   1.2 reduce all pixel values by half.
%   1.4 display it by imshow.
%   1.3 save to 'lena2.bmp' by imwrite.
%   1.5 Answer the question: 
%       What is the visual difference between 'lena.bmp' and 'lena2.bmp'.
grayLena = imread('lena.bmp');    % read 'lena.bmp' by imread.
grayLena_half = grayLena*0.5;     % reduce all pixel values by half.
figure(9);                       
imshow(grayLena_half),title("half pixel value");  % display it by imshow.
imwrite(grayLena_half, 'lena2.bmp')               % save to 'lena2.bmp' by imwrite.

%% 2. Bit-plane (1 point)
%   One of the bit-planes of 'lena.bmp' hide a secret message. 
%   Which bit-plane is it and what is the message?
%   Find it out and save that plane to 'message.bmp'
%   Can you perceive this message directly from the image without any image
%   processing? Why?

for index = 1:8
    figure(index);    % named the figure
    eachPlaneLena=bitget(grayLena,index);    %  get bit at specified position
    imshow(logical(eachPlaneLena)),title((index-1) + " bit plane");    % show and titled by bit-plane every picture
    if index == 1
        imwrite(logical(eachPlaneLena), "message.bmp")    % save picture of 0 bit-plane and named message.bmp
    end
end
%% 3. Lossy Compression by Discarding Lower Bits. (0.5 point)
%   Humans are not sensitive to lower bits of images, 
%   so we can compress an image by discarding them.
%
%   3.1 Extract highest four bit-planes (5-8) from 'lena.bmp'
%
%   3.2 Save the four bit-planes to 'compressed.mat' by 'save'.
%       How large is the image file 'lena.bmp'? 
%       How large is the file 'compressed.mat'?
%
%   3.4 load the four bit-planes from 'compressed.mat' by
%                   load('compressed.mat')
%
%   3.5 Reconstruct the image from the highest four bit-planes.
%
%   3.6 Save it to 'compressed.bmp'. 
%       Could you see the difference after lossy compression? 
%       What is the difference?
%
%   Tips:
%       If you do not know how to use 'save', 
%       see https://www.mathworks.com/help/matlab/ref/save.html#btppzj8-1

plane8 = bitget(grayLena,8);    % 3.1 Extract 8 bit-planes from 'lena.bmp'
plane7 = bitget(grayLena,7);    % 3.1 Extract 7 bit-planes from 'lena.bmp'
plane6 = bitget(grayLena,6);    % 3.1 Extract 6 bit-planes from 'lena.bmp'
plane5 = bitget(grayLena,5);    % 3.1 Extract 5 bit-planes from 'lena.bmp'

save('compressed.mat', 'plane5', 'plane6', 'plane7', 'plane8');    %3.2 Save the four bit-planes to 'compressed.mat' by 'save'
S=load('compressed.mat');    % 3.4 load the four bit-planes from 'compressed.mat' by load('compressed.mat')
concat = S.plane5*2^4 + S.plane6*2^5 + S.plane7*2^6 + S.plane8*2^7;    % 3.5 Reconstruct the image from the highest four bit-planes.

imwrite(concat, 'compressed.bmp')    % 3.6 Save it to 'compressed.bmp'. 














