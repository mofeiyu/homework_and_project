% resample.m

function new_y = resample(y, old_f, new_f)
% RESAMPLE Resample by linear interpolation
%   y,      data
%   old_f,  original sample rate
%   new_f,  new sample rate
%   
%   RESAMPLE(y, old_f, new_f)

    l = length(y)/old_f;
    original_t = (1:length(y))/old_f;
    sample_t = 0:1/new_f:l;
    
    % See https://www.mathworks.com/help/matlab/ref/interp1.html 
    % or wikipeida for more information of linear interpolation.
    new_y = linear_interp(original_t, y, sample_t)';
end

function new_y = linear_interp(X, Y, Z)
% Linear Interpolation
% X should be in increasing order.
% Given N points 
%   (X(1), Y(1)), (X(2), Y(2)), ..., (X(N), Y(N)) 
% on the function f curve, return predicted function values on Z(i) in vector form 
%   [f(Z(1)), f(Z(2)), f(Z(3)), ... ]

    new_y = Z;
    j = 1;
    for i = 1:length(Z)
        x = Z(i);
        if x <= X(1)
            j = 1;
        elseif x >= X(end)
            j = length(X) - 1;
        else
            while(x < X(j))
                j = j - 1;
            end
            while(x > X(j+1))
                j = j + 1;
            end
        end
        x1 = X(j);
        x2 = X(j+1);
        y1 = Y(j);
        y2 = Y(j+1);
        
        new_y(i) = ((x-x1)*y2 + (x2-x)*y1)/(x2-x1);
    end
end