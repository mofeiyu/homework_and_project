filename = "clap.mp3";
[y,f] = audioread(filename);    % read clap.mp3 file

%%%%% draw frequency spectrum pic %%%%%
Y = fft(y);
L = length(y);
P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = f*(0:(L/2))/L;
plot(f,P1) 
title('clap.mp3	¡¯s frequency spectrum')
xlabel('f (Hz)')
ylabel('|P1(f)|')