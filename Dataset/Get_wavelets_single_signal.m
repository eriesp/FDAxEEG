clear all
close all
clc


load("ICA_filtered/ADHD/v1p.mat")

% load("Wavelettati/v1p_wt.mat")
% signals = dec.ca;


plot(1:length(data(1,:)),data(1,:));

[c,l] = wavedec(data(1,:),4,'db2');
% c vettore decomposizione
% l book keeping vector for sparse
c1 = c(1:l(1));                                 %760 elementi
c2 = c((l(1)+1):(l(1)+l(2)));                 %760 elem 
c3 = c((l(1)+l(2)+1):(sum(l(1:3))));       %1518 elem
c4 = c((sum(l(1:3))+1):(sum(l(1:4))));      %3034 elem
c5 = c((sum(l(1:4))+1):(sum(l(1:5))));    %6066 elem

subplot(2,3,1)
plot(c5)
title("c5 64 - 32 Hz")

subplot(2,3,2)
plot(c4)
title("c4 16 - 32 Hz")

subplot(2,3,3)
plot(c3)
title("c3 8 - 16 Hz")

subplot(2,3,4)
plot(c2)
title("c2 4 - 8 Hz")

subplot(2,3,5)
plot(c1)
title("c1 0.01 - 4 Hz")


subplot(2,3,1)
pwelch(c1)
title("c1 0.01 - 4 Hz")

subplot(2,3,2)
pwelch(c2)
title("c2 4 - 8 Hz")

subplot(2,3,3)
pwelch(c3)
title("c3 8 - 16 Hz")

subplot(2,3,4)
pwelch(c4)
title("c4 16 - 32 Hz")

subplot(2,3,5)
pwelch(c5)
title("c5 32 - 64 Hz")