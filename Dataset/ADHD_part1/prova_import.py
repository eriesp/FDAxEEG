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

matfiles = glob.glob('*.mat')

data = loadmat(matfiles[1])

channel_names = ["Fp1", "Fp2","F3","F4","C3","C4","P3","P4","O1","O2","F7","F8","T7", 
              "T8", "P7","P8","Fz","Cz","Pz"] 
sfreq=128

n_channels = len(data['v12p'][1,:])

info = mne.create_info(
        ch_names = channel_names,
        ch_types = ['eeg']*n_channels,
        sfreq    = sfreq 
        )   

info.set_montage('standard_1020')

simulated_raw = mne.io.RawArray(data['v12p'].T, info)
simulated_raw.plot(show_scrollbars=False, show_scalebars=False, n_channels=1)
fp1=simulated_raw._data[1]
t=simulated_raw.times

plt.plot(t,fp1)
plt.show()

power_bands=nk.eeg_power(fp1, sampling_rate=128, frequency_band=['Gamma', 'Beta', 'Alpha', 'Theta', 'Delta'])


#Queste righe sono solo prove

#events = mne.make_fixed_length_events(simulated_raw,id=1, start=0, duration=20)
#epochs = mne.Epochs(simulated_raw, events, preload=True)

#epochs.plot_psd(fmin=0., fmax=64., average=True, spatial_colors=False)
#epochs.plot_psd_topomap(ch_type='eeg', normalize=False)