
clear all

load('ADHD_Matrici_psd/ch1_p3.mat')

figure(1)
plot(f,p(1:10,:)')

figure(2)
plot(f,10.^(p(1:10,:)'./10))

load('Control_Matrici_psd/ch1_p3.mat')

figure(3)
plot(f,p(1:10,:)')

figure(4)
plot(f,10.^(p(1:10,:)'./10))
