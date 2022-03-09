# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:39:40 2022

@author: Asus
"""

import numpy as np
from scipy.io import loadmat 
import mne, glob 

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
