%% Gruppo ADHD

clear

for ch = 1:19
    
    % comp 1
    filename = append('ADHD_Matrici_wavelettati/ch',string(ch),'_c1.mat');
    mat = load(filename).c1;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('ADHD_Matrici_psd/ch',string(ch),'_p1'),'p','f')
    
    % comp 2
    filename = append('ADHD_Matrici_wavelettati/ch',string(ch),'_c2.mat');
    mat = load(filename).c2;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('ADHD_Matrici_psd/ch',string(ch),'_p2'),'p','f')
    
    % comp 3
    filename = append('ADHD_Matrici_wavelettati/ch',string(ch),'_c3.mat');
    mat = load(filename).c3;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('ADHD_Matrici_psd/ch',string(ch),'_p3'),'p','f')
    
    
    % comp 4
    filename = append('ADHD_Matrici_wavelettati/ch',string(ch),'_c4.mat');
    mat = load(filename).c4;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('ADHD_Matrici_psd/ch',string(ch),'_p4'),'p','f')
    
    
    % comp 5
    filename = append('ADHD_Matrici_wavelettati/ch',string(ch),'_c5.mat');
    mat = load(filename).c5;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('ADHD_Matrici_psd/ch',string(ch),'_p5'),'p','f')
    
end

%% Gruppo di controllo

clear

for ch = 1:19
    
    % comp 1
    filename = append('Control_Matrici_wavelettati/ch',string(ch),'_c1.mat');
    mat = load(filename).c1;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('Control_Matrici_psd/ch',string(ch),'_p1'),'p','f')
    
    % comp 2
    filename = append('Control_Matrici_wavelettati/ch',string(ch),'_c2.mat');
    mat = load(filename).c2;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('Control_Matrici_psd/ch',string(ch),'_p2'),'p','f')
    
    % comp 3
    filename = append('Control_Matrici_wavelettati/ch',string(ch),'_c3.mat');
    mat = load(filename).c3;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('Control_Matrici_psd/ch',string(ch),'_p3'),'p','f')
    
    
    % comp 4
    filename = append('Control_Matrici_wavelettati/ch',string(ch),'_c4.mat');
    mat = load(filename).c4;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('Control_Matrici_psd/ch',string(ch),'_p4'),'p','f')
    
    
    % comp 5
    filename = append('Control_Matrici_wavelettati/ch',string(ch),'_c5.mat');
    mat = load(filename).c5;

    [p, f] = pwelch(mat',[],[],[],128);
    p = 10*log10(p');

    save(append('Control_Matrici_psd/ch',string(ch),'_p5'),'p','f')
    
end


