%% control

clear
load("ICA_filtered/control_ica.mat");


for ch = 1:19
    
    [c1, c2, c3, c4, c5, paz] = get_matrices(ch, 16, ALLEEG, false);

    save(append('Control_Matrici_wavelettati/ch',string(ch),'_c1'),'c1')
    save(append('Control_Matrici_wavelettati/ch',string(ch),'_c2'),'c2')
    save(append('Control_Matrici_wavelettati/ch',string(ch),'_c3'),'c3')
    save(append('Control_Matrici_wavelettati/ch',string(ch),'_c4'),'c4')
    save(append('Control_Matrici_wavelettati/ch',string(ch),'_c5'),'c5')
end

save(append('Control_Matrici_wavelettati/paz'),'paz');


%% ADHD

clear
load("ICA_filtered/adhd_ica.mat");


for ch = 1:19
    
    [c1, c2, c3, c4, c5, paz] = get_matrices(ch, 16, ALLEEG, true);

    save(append('ADHD_Matrici_wavelettati/ch',string(ch),'_c1'),'c1')
    save(append('ADHD_Matrici_wavelettati/ch',string(ch),'_c2'),'c2')
    save(append('ADHD_Matrici_wavelettati/ch',string(ch),'_c3'),'c3')
    save(append('ADHD_Matrici_wavelettati/ch',string(ch),'_c4'),'c4')
    save(append('ADHD_Matrici_wavelettati/ch',string(ch),'_c5'),'c5')
end

save(append('ADHD_Matrici_wavelettati/paz'),'paz');
