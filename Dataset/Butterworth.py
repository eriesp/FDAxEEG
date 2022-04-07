# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:45:37 2022

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
import pywt
import sys

def impo(x):
    channel_names = ["Fp1", "Fp2","F3","F4","C3","C4","P3","P4","O1","O2","F7","F8","T7", 
               "T8", "P7","P8","Fz","Cz","Pz"] 
    directory = os.getcwd()
    path_adhd = "\ADHD"
    matfiles_adhd = glob.glob(directory + path_adhd + '/*.mat')
    path_control = "\Control"
    matfiles_control = glob.glob(directory + path_control + '/*.mat')
    sfreq=128
    n_channels = 19
    info = mne.create_info(
        ch_names = channel_names,
        ch_types = ['eeg']*n_channels,
        sfreq    = sfreq 
        )   
    info.set_montage('standard_1020')
    channel_adhd=[]
    t_adhd=[]
    channel_control=[]
    t_control=[]
    for n in np.arange(len(matfiles_adhd)):
        data_adhd = loadmat(matfiles_adhd[n])
        val=list(data_adhd.values())[3]
        raw = mne.io.RawArray(val.T, info)
        raw_times=raw.times
        raw_data=raw._data[x]
        filt_raw = raw.copy().filter(l_freq=0.5, h_freq=50.,method='iir', iir_params=None)
        data=filt_raw._data[x]
        times=filt_raw.times
        channel_adhd.append(data)
        t_adhd.append(times)
        
        mintime = 0
        maxtime = mintime + 2000

        plt.figure()
        plt.subplot(2, 1, 1)
        plt.plot(raw_times[mintime:maxtime], raw_data[mintime:maxtime])
        plt.xlabel('time (s)')
        plt.ylabel('microvolts (uV)')
        plt.title("Raw signal")
        plt.subplot(2, 1, 2)
        plt.plot(times[mintime:maxtime], data[mintime:maxtime])
        plt.xlabel('time (s)')
        plt.ylabel('microvolts (uV)')
        plt.title("De-noised signal with Butterworth")
        
    for n in np.arange(len(matfiles_control)):
        data_control = loadmat(matfiles_control[n])
        val=list(data_control.values())[3]
        raw = mne.io.RawArray(val.T, info)
        filt_raw = raw.copy().filter(l_freq=0.5, h_freq=50.,method='iir', iir_params=None)
        data=filt_raw._data[x]
        times=filt_raw.times
        channel_control.append(data)
        t_control.append(times)
    return channel_adhd, t_adhd, channel_control, t_control

channel_adhd, t_adhd, channel_control, t_control=impo(0)









