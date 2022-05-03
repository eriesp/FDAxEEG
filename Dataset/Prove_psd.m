
c1 = c1'; % 0.01 a 4 Hz
[p] = pwelch(c1,[],[],[],128);

subplot(2,1,1)
plot(10*log10(p))

subplot(2,1,2)
pwelch(c1)


% data = c1(1,:);
% [p] = pwelch(data,[],[],[],128);
% 
% subplot(2,3,1)
% plot(10*log10(p))
% grid on
% 
% subplot(2,3,4)
% pwelch(data)
% 
% 
% % ===============
% data = c2(1,:);
% [p] = pwelch(data,[],[],[],128);
% 
% subplot(2,3,2)
% plot(10*log10(p))
% 
% subplot(2,3,5)
% pwelch(data)
% 
% 
% 
% %%  ===============
% data = c5(1,:);
% [p] = pwelch(data,[],[],[],128);
% 
% subplot(2,3,3)
% plot(10*log10(p))
% 
% subplot(2,3,6)
% pwelch(data)
% 
