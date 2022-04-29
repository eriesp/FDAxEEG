clear
clc

load("ICA_filtered/adhd_ica.mat")

% CHANNEL 1
ch = 1;

% creo matrici vuote per ogni componente

% componente 1
ch1_c1 = zeros(61,750);

% componente 2
ch1_c2 = ch1_c1; % hanno la stessa dimensione

% componente 3
ch1_c3 = zeros(61,1497);

% componente 4
ch1_c4 = zeros(61,2992);

% componente 5
ch1_c5 = zeros(61,5981);

% estrarre data per ogni paziente

for ii = 1:61
    data = ALLEEG(ii).data;
    c_dec = get_wt(data,ch);
    
    ch1_c1(ii,:) = c_dec.c1;
    ch1_c2(ii,:) = c_dec.c2;
    ch1_c3(ii,:) = c_dec.c3;
    ch1_c4(ii,:) = c_dec.c4;
    ch1_c5(ii,:) = c_dec.c5;
end
    
