filename = "clap.mp3";
[y,f] = audioread(filename);    % read clap.mp3 file

filename = "clap2.flac";
audiowrite(filename, y, f*2);    % frequency * 2 to speed 
