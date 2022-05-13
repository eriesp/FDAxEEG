clear all
clc

%Prefrontale
for comp = 1:5
    filename=append('ADHD_Matrici_pyulear/ch',string(1),'_p',string(comp));
    mat_1 = load(filename);
    f=mat_1.f;
    fp1=mat_1.p;
    fp1=fp1';
    filename=append('ADHD_Matrici_pyulear/ch',string(2),'_p',string(comp));
    mat_2 = load(filename);
    fp2=mat_2.p;
    fp2=fp2';
    
    avg=zeros(555,129);
    for ii = 1:length(fp2)
        signals=[fp1(ii,:); fp2(ii,:)];
        avg(ii,:)=mean(signals);
    end
    
    save(append('ADHD_Matrici_medie/zona1_p',string(comp)),'avg','f')
end

%Frontale
for comp = 1:5
    filename=append('ADHD_Matrici_pyulear/ch',string(3),'_p',string(comp));
    mat_1 = load(filename);
    f=mat_1.f;
    F3=mat_1.p;
    F3=F3';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(4),'_p',string(comp));
    mat_2 = load(filename);
    F4=mat_2.p;
    F4=F4';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(11),'_p',string(comp));
    mat_3 = load(filename);
    F7=mat_3.p;
    F7=F7';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(12),'_p',string(comp));
    mat_4 = load(filename);
    F8=mat_4.p;
    F8=F8';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(17),'_p',string(comp));
    mat_5 = load(filename);
    Fz=mat_5.p;
    Fz=Fz';
    
    avg=zeros(555,129);
    for ii = 1:length(F3)
        signals=[F3(ii,:); F4(ii,:);F7(ii,:);F8(ii,:);Fz(ii,:)];
        avg(ii,:)=mean(signals);
    end
    
    save(append('ADHD_Matrici_medie/zona2_p',string(comp)),'avg','f')
end

%Centrale
for comp = 1:5
    filename=append('ADHD_Matrici_pyulear/ch',string(5),'_p',string(comp));
    mat_1 = load(filename);
    f=mat_1.f;
    C3=mat_1.p;
    C3=C3';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(6),'_p',string(comp));
    mat_2 = load(filename);
    C4=mat_2.p;
    C4=C4';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(18),'_p',string(comp));
    mat_3 = load(filename);
    Cz=mat_3.p;
    Cz=Cz';
    
    avg=zeros(555,129);
    for ii = 1:length(F3)
        signals=[C3(ii,:); C4(ii,:);Cz(ii,:)];
        avg(ii,:)=mean(signals);
    end
    
    save(append('ADHD_Matrici_medie/zona3_p',string(comp)),'avg','f')
end

%Parietale
for comp = 1:5
    filename=append('ADHD_Matrici_pyulear/ch',string(7),'_p',string(comp));
    mat_1 = load(filename);
    f=mat_1.f;
    P3=mat_1.p;
    P3=P3';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(8),'_p',string(comp));
    mat_2 = load(filename);
    P4=mat_2.p;
    P4=P4';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(15),'_p',string(comp));
    mat_3 = load(filename);
    P7=mat_3.p;
    P7=P7';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(16),'_p',string(comp));
    mat_4 = load(filename);
    P8=mat_4.p;
    P8=P8';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(19),'_p',string(comp));
    mat_5 = load(filename);
    Pz=mat_5.p;
    Pz=Pz';
    
    avg=zeros(555,129);
    for ii = 1:length(F3)
        signals=[P3(ii,:); P4(ii,:);P7(ii,:);P8(ii,:);Pz(ii,:)];
        avg(ii,:)=mean(signals);
    end
    
    save(append('ADHD_Matrici_medie/zona4_p',string(comp)),'avg','f')
end

%Occipitale
for comp = 1:5
    filename=append('ADHD_Matrici_pyulear/ch',string(9),'_p',string(comp));
    mat_1 = load(filename);
    f=mat_1.f;
    O1=mat_1.p;
    O1=O1';
    
    filename=append('ADHD_Matrici_pyulear/ch',string(10),'_p',string(comp));
    mat_2 = load(filename);
    O2=mat_2.p;
    O2=O2';
    
    avg=zeros(555,129);
    for ii = 1:length(fp2)
        signals=[O1(ii,:); O2(ii,:)];
        avg(ii,:)=mean(signals);
    end
    
    save(append('ADHD_Matrici_medie/zona5_p',string(comp)),'avg','f')
end

%Temporale sx e dx sono unici canali

