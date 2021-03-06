clear
clc

load("ICA_filtered/adhd_ica.mat")

% faccio epoches di 16s
t_epoch = 16;       % tempo per epoch
l_epoch = t_epoch*128;   % numero punti per epoch

% CHANNEL 1
ch = 2;


% estrarre data per ogni paziente

c_paz = 1;  % contatore pazienti

% i_mat = 1;  % contatore riga delle matrici


% creo matrici per il primo paziente e poi proseguo

data = ALLEEG(c_paz).data;

n_epoch = floor(length(data)/l_epoch);

jj = 1;
sub_data = data(:,(jj-1)*l_epoch + 1 : jj*l_epoch);

c_dec = get_wt(sub_data,ch);

ch1_c1 = c_dec.c1;
ch1_c2 = c_dec.c2;
ch1_c3 = c_dec.c3;
ch1_c4 = c_dec.c4;
ch1_c5 = c_dec.c5;

% i_mat = i_mat + 1;

for jj = 2:n_epoch

    sub_data = data((jj-1)*l_epoch + 1 : jj*l_epoch);

    c_dec = get_wt(sub_data,ch);

    ch1_c1 = [ch1_c1; c_dec.c1];
    ch1_c2 = [ch1_c2; c_dec.c2];
    ch1_c3 = [ch1_c3; c_dec.c3];
    ch1_c4 = [ch1_c4; c_dec.c4];
    ch1_c5 = [ch1_c5; c_dec.c5];

    % i_mat = i_mat + 1;
end

c_paz = c_paz + 1;

% ora continuo con gli altri pazienti

while c_paz <= 61
    data = ALLEEG(c_paz).data;
    
    n_epoch = floor(length(data)/l_epoch);
    
    for jj = 1:n_epoch
        
        sub_data = data((jj-1)*l_epoch + 1 : jj*l_epoch);
        
        c_dec = get_wt(sub_data,ch);

        ch1_c1 = [ch1_c1; c_dec.c1];
        ch1_c2 = [ch1_c2; c_dec.c2];
        ch1_c3 = [ch1_c3; c_dec.c3];
        ch1_c4 = [ch1_c4; c_dec.c4];
        ch1_c5 = [ch1_c5; c_dec.c5];
        
        % i_mat = i_mat + 1;
    end
    
    c_paz = c_paz + 1;
    
end


    
