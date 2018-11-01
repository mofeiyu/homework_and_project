clc
clear



%% Control Structure overview 
nrows=4;
ncols=6;
A=ones(nrows,ncols);

for c=1:ncols
    for r=1:nrows
        if r==c
            A(r,c)=2;
        elseif abs(r-c)==1
            A(r,c)=-1;
        else
            A(r,c)=0;
        end
    end
end

%% if statements
day=2;
if day==6||day==7
    state='weekend';
elseif day==1||day==2||day==3||day==4||day==5
    state='weekday';
else 
    state ='wrong number';
end

%% switch statments
month=4;
leapYear=false;

switch month
    
    case {4,6,9,11} % Apr, June, Sept or Nov
        days=30;
    case 2 % Feb
        if leapYear % whether it is leap Year
            days=29;
        else
            days=28;
        end
    case{1,3,5,7,8,10,12} % Other months
        days=31;
    otherwise 
        error('bad month index');
end

%% for statements

%% while statements