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
#import skfda
import scipy

path_adhd = r"C:\Users\erica\Documents\UNI\NECSTCamp\NL2\Project-git\FDAxEEG\Dataset\ADHD"
matfiles_adhd = glob.glob(path_adhd + '/*.mat')

path_control = r"C:\Users\erica\Documents\UNI\NECSTCamp\NL2\Project-git\FDAxEEG\Dataset\Control"
matfiles_control = glob.glob(path_control + '/*.mat')

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
simulated_raw.plot(show_scrollbars=False, show_scalebars=False, n_channels=1)
fp1_preica=simulated_raw._data[0]
t_preica=simulated_raw.times

plt.plot(t_preica,fp1_preica)
plt.show()

# events = mne.make_fixed_length_events(simulated_raw,id=1, start=0, duration=20)
# epochs = mne.Epochs(simulated_raw, events, preload=True)
# evoked = epochs.average()
# x=evoked.data[0]

fs=128
f_preica, Pxx_den_preica = scipy.signal.welch(fp1_preica, fs)
plt.plot(f_preica, Pxx_den_preica)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

P_log_preica=np.log(Pxx_den_preica)
plt.plot(f_preica, P_log_preica)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

# basis = skfda.representation.basis.BSpline(n_basis=20)
# df_Channel=pd.DataFrame(data=P_log)
# Channel=df_Channel.to_numpy(dtype=None, copy=False)
# Channel = np.nan_to_num(Channel)
# DG_Channel=skfda.FDataGrid(data_matrix=Channel)

# X_basis = DG_Channel.to_basis(basis)
# X_basis.plot()
# plt.show()

ica = mne.preprocessing.ICA(n_components=19, random_state=0, max_iter=800)
ica.fit(simulated_raw)
ica.exclude = [1, 2]  # details on how we picked these are omitted here
ica.plot_properties(simulated_raw, picks=ica.exclude)

orig_raw = simulated_raw.copy()
simulated_raw.load_data()
ica.apply(simulated_raw)

# show some frontal channels to clearly illustrate the artifact removal
chan_idxs = [simulated_raw.ch_names.index(ch) for ch in channel_names]
orig_raw.plot(order=chan_idxs, start=12, duration=4)
simulated_raw.plot(order=chan_idxs, start=12, duration=4)

fp1=simulated_raw._data[0]
t=simulated_raw.times

plt.plot(t,fp1)
plt.show()

fs=128
f, Pxx_den = scipy.signal.welch(fp1, fs)
plt.plot(f, Pxx_den)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

P_log=np.log(Pxx_den)
plt.plot(f, P_log)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2)
fig.set_size_inches(10, 5)
axes[0].set_title("Preica" )
axes[0].plot(f_preica, P_log_preica, label='EFP',color='C0')
    
axes[1].set_title("Postica")
axes[1].plot(f, P_log, label='EFP', color='C1')
for ax in axes.flat:
    ax.label_outer()
fig.tight_layout()