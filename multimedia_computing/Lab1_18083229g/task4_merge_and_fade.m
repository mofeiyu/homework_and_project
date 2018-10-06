% read files
filename1 = "handel.flac";
filename2 = "laugh.mp3";
filename3 = "clap.mp3";
[y1, f1] = audioread(filename1);
[y2, f2] = audioread(filename2);
[y3, f3] = audioread(filename3);

f = max(f1, f2);
f = max(f, f3);    % find the max frequency

% resample them
y1 = resample(y1, f1, f);
y2 = resample(y2, f2, f);
y3 = resample(y3, f3, f); 

% merge them
y = [y1; y2; y3];  

% fade in and out
in_length = 3*f; % 3s fade in
out_length = 3*f; % 3s fade out

% prepare masks
in_mask = (1:in_length)' / in_length;    % small to big
out_mask = (out_length:-1:1)' / out_length;    % big to small

% apply mask
y(1:in_length) = y(1:in_length) .* in_mask;    % change 3s head
y(end - out_length + 1:end) = y(end - out_length + 1:end) .* out_mask;    % change 3s end

% save
filename = "my_creation.flac";
audiowrite(filename, y, f);     
fprintf('Save to %s\n', filename);
