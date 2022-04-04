# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:39:40 2022

@author: Asus
"""

import numpy as np
from scipy.io import loadmat 
import mne, glob 
import matplotlib.pyplot as plt
import neurokit2 as nk
import pandas as pd
import os
import skfda
import scipy

directory = os.getcwd()

path_adhd = "\ADHD"
matfiles_adhd = glob.glob(directory + path_adhd + '/*.mat')

path_control = "\Control"
matfiles_control = glob.glob(directory + path_control + '/*.mat')

data_adhd = loadmat(matfiles_adhd[1])
data_control = loadmat(matfiles_control[1])

channel_names = ["Fp1", "Fp2","F3","F4","C3","C4","P3","P4","O1","O2","F7","F8","T7", 
              "T8", "P7","P8","Fz","Cz","Pz"] 
sfreq=128

n_channels = len(data_adhd['v12p'][1,:])

info = mne.create_info(
        ch_names = channel_names,
        ch_types = ['eeg']*n_channels,
        sfreq    = sfreq 
        )   

info.set_montage('standard_1020')

simulated_raw = mne.io.RawArray(data_adhd['v12p'].T, info)
fp1_preica=simulated_raw._data[0]
t_preica=simulated_raw.times

fs=128
f_preica, Pxx_den_preica = scipy.signal.welch(fp1_preica, fs)
P_log_preica=np.log(Pxx_den_preica)

#FILTRI
filt_raw = simulated_raw.copy().filter(l_freq=1., h_freq=40.)

simulated_raw.plot_psd()
filt_raw.plot_psd()

ica = mne.preprocessing.ICA(n_components=15, random_state=97, max_iter=800)
ica.fit(filt_raw)
ica.plot_components()
# ica.exclude = [1, 2]
ica.plot_properties(simulated_raw) #picks=ica.exclude)

# orig_raw = simulated_raw.copy()
# simulated_raw.load_data()
# ica.apply(simulated_raw)

# chan_idxs = [simulated_raw.ch_names.index(ch) for ch in channel_names]
# orig_raw.plot(order=chan_idxs, start=12, duration=4)
# simulated_raw.plot(order=chan_idxs, start=12, duration=4)

# fp1=simulated_raw._data[0]
# t=simulated_raw.times

# f, Pxx_den = scipy.signal.welch(fp1, fs)
# P_log=np.log(Pxx_den)

# fig, axes = plt.subplots(nrows=1, ncols=2)
# fig.set_size_inches(10, 5)
# axes[0].set_title("Preica" )
# axes[0].plot(f_preica, P_log_preica, label='EFP',color='C0')
    
# axes[1].set_title("Postica")
# axes[1].plot(f, P_log, label='EFP', color='C1')
# for ax in axes.flat:
#     ax.label_outer()
# fig.tight_layout()