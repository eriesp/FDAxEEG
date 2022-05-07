% pyulear prove

clear

ch = 1;
filename = append('Control_Matrici_wavelettati/ch',string(ch),'_c1.mat');
mat = load(filename).c1;

% for or = 1:20
%     [p, f] = pyulear(mat',or,[],128);
%     
%     [H,F] = freqz(1,A,[],1);
%     plot(F,20*log10(abs(H)))
%     
% end

%% prova

close



[p_w,f_w] = pwelch(mat',[],[],[],128);

Q_w_med = median(trapz(p_w));
Q_w_sum = sum(trapz(p_w));

ord_vec = 20:2:50;

n = length(ord_vec);

Q_med = zeros(n,1);
Q_sum = zeros(n,1);

ii = 1;

for or = ord_vec
%     subplot(2,3,ii)
    [p, f] = pyulear(mat',or,[],128);
%     plot(f,p(:,idx)')
%     hold on
%     
%     plot(f_w,p_w(:,1)')
%     title(append('Yule-Walker ord: ',string(or)))
%     legend('YW','Welch')
    
    Q = trapz(p);
    Q_med(ii) = median(Q);
    Q_sum(ii) = sum(Q);
    
    ii = ii+1;
end

Q_dif_med = abs(Q_med - Q_w_med);
Q_dif_sum = abs(Q_sum - Q_w_sum);

subplot(1,2,1)
plot(ord_vec,Q_dif_med)
title('diff of median')

subplot(1,2,2)
plot(ord_vec,Q_dif_sum)
title('diff of sum')

[~,I] = min(Q_dif_med);
ord_vec(I) 

% 
% idx = 50;
% 
% plot(f,p(:,idx)')
% hold on
% 
% plot(f_w,p_w(:,1)')
% title(append('Yule-Walker ord: ',string(or)))
% legend('YW','Welch')

% 
% [H,F] = freqz(1,mat(1:10)',[],1);
% plot(F,20*log10(abs(H)))

%% Campione misto tra ADHD e Control

clear

ch = 1;
filename_control = append('Control_Matrici_wavelettati/ch',string(ch),'_c5.mat');
mat_control = load(filename_control).c5;

filename_adhd = append('ADHD_Matrici_wavelettati/ch',string(ch),'_c5.mat');
mat_adhd = load(filename_adhd).c5;

mat_misto = [mat_control(1:100,:);mat_adhd(1:100,:)];

[p_w,f_w] = pwelch(mat_misto',[],[],[],128);

Q_w_med = median(trapz(p_w));
Q_w_sum = sum(trapz(p_w));

ord_vec = 1:1:100;

n = length(ord_vec);

Q_med = zeros(n,1);
Q_sum = zeros(n,1);

ii = 1;

for or = ord_vec
    [p, f] = pyulear(mat_misto',or,[],128);
    Q = trapz(p);
    Q_med(ii) = median(Q);
    Q_sum(ii) = sum(Q);
    
    ii = ii+1;
end

Q_dif_med = abs(Q_med - Q_w_med);
Q_dif_sum = abs(Q_sum - Q_w_sum);

subplot(1,2,1)
plot(ord_vec,Q_dif_med)
title('diff of median')

subplot(1,2,2)
plot(ord_vec,Q_dif_sum)
title('diff of sum')

[~,I] = min(Q_dif_med);
ord_vec(I) 

[p, f] = pyulear(mat_misto',35,[],128);
plot(f(1:60),p(:,1:60))