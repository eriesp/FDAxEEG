% funzione che dato il canale mi trova le matricine delle componenti
% wavelet
function [c1, c2, c3, c4, c5] = get_matrices(ch, t_epoch, ALLEEG)
    
    l_epoch = t_epoch*128;   % numero punti per epoch
    
    % estrarre data per ogni paziente

    c_paz = 1;  % contatore pazienti

    % i_mat = 1;  % contatore riga delle matrici


    % creo matrici per il primo paziente e poi proseguo

    data = ALLEEG(c_paz).data;

    n_epoch = floor(length(data)/l_epoch);

    jj = 1;
    sub_data = data(:,(jj-1)*l_epoch + 1 : jj*l_epoch);

    c_dec = get_wt(sub_data,ch);

    c1 = c_dec.c1;
    c2 = c_dec.c2;
    c3 = c_dec.c3;
    c4 = c_dec.c4;
    c5 = c_dec.c5;

    % i_mat = i_mat + 1;

    for jj = 2:n_epoch

        sub_data = data(:,(jj-1)*l_epoch + 1 : jj*l_epoch);

        c_dec = get_wt(sub_data,ch);

        c1 = [c1; c_dec.c1];
        c2 = [c2; c_dec.c2];
        c3 = [c3; c_dec.c3];
        c4 = [c4; c_dec.c4];
        c5 = [c5; c_dec.c5];

        % i_mat = i_mat + 1;
    end

    c_paz = c_paz + 1;

    % ora continuo con gli altri pazienti
    
    % !!!!!! CAMBIARE LIMITE c_paz IN CASO SIANO DI CONTROLLO O ADHD
    while c_paz <= 60
        data = ALLEEG(c_paz).data;

        n_epoch = floor(length(data)/l_epoch);

        for jj = 1:n_epoch

            sub_data = data(:,(jj-1)*l_epoch + 1 : jj*l_epoch);

            c_dec = get_wt(sub_data,ch);

            c1 = [c1; c_dec.c1];
            c2 = [c2; c_dec.c2];
            c3 = [c3; c_dec.c3];
            c4 = [c4; c_dec.c4];
            c5 = [c5; c_dec.c5];

            % i_mat = i_mat + 1;
        end

        c_paz = c_paz + 1;
        
    end
    
   
    
end