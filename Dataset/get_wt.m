function c_dec = get_wt(data) 


[c,l] = wavedec(data(1,:),4,'db2');

c1 = c(1:l(1));
c2 = c((l(1)+1):(l(1)+l(2)));
c3 = c((l(1)+l(2)+1):(sum(l(1:3))));
c4 = c((sum(l(1:3))+1):(sum(l(1:4))));
c5 = c((sum(l(1:4))+1):(sum(l(1:5))));

c_dec = struct('c1',c1, 'c2',c2, 'c3',c3, 'c4',c4, 'c5',c5);


subplot(2,5,1)
plot(c1)
title("c1 0.01 - 4 Hz")
xlabel('time')
ylabel('\muV')

subplot(2,5,6)
pwelch(c1)
title("Power spectral density c1")

subplot(2,5,2)
plot(c2)
title("c2 4 - 8 Hz")
xlabel('time')

subplot(2,5,7)
pwelch(c2)
title("Power spectral density c2")

subplot(2,5,3)
plot(c3)
title("c3 8 - 16 Hz")
xlabel('time')

subplot(2,5,8)
pwelch(c3)
title("Power spectral density c3")

subplot(2,5,4)
plot(c4)
title("c4 16 - 32 Hz")
xlabel('time')

subplot(2,5,9)
pwelch(c4)
title("Power spectral density c4")

subplot(2,5,5)
plot(c5)
title("c5 32 - 64 Hz")
xlabel('time')

subplot(2,5,10)
pwelch(c5)
title("Power spectral density c5")

end