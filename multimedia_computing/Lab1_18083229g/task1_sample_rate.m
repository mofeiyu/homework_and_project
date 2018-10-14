filename = "clap.mp3";
[y,f] = audioread(filename);    % read clap.mp3 file
fprintf("sample rate:%dHz\n",f);
