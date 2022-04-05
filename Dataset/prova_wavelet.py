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

def diocristo(x):
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
        filt_raw = raw.copy().filter(l_freq=0.5, h_freq=50.,method='iir', iir_params=None)
        data=filt_raw._data[x]
        times=filt_raw.times
        channel_adhd.append(data)
        t_adhd.append(times)
        
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

a,b,c,d=diocristo(0)

# simulated_raw = mne.io.RawArray(data_adhd['v12p'].T, info)
# filt_raw = simulated_raw.copy().filter(l_freq=1., h_freq=None)
# data=filt_raw._data[0]
# index=filt_raw.times

# # Create wavelet object and define parameters
# w = pywt.Wavelet('db2')
# maxlev = pywt.dwt_max_level(len(data), w.dec_len)
# # maxlev = 2 # Override if desired
# print("maximum level is " + str(maxlev))

# threshold = 0.04 # Threshold for filtering

# # Decompose into wavelet components, to the level selected:
# coeffs = pywt.wavedec(data, 'sym4', level=maxlev)

# #cA = pywt.threshold(cA, threshold*max(cA))
# plt.figure()
# for i in range(1, len(coeffs)):
#     plt.subplot(maxlev, 1, i)
#     plt.plot(coeffs[i])
#     #var=np.median(np.abs(coeffs[i]))/0.6745
#     #N=len(data)
#     # threshold = var*np.sqrt(2*np.log(N))
#     # coeffs[i] = pywt.threshold(coeffs[i], threshold)
#     coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))
#     plt.plot(coeffs[i])


# datarec = pywt.waverec(coeffs, 'sym4')


# mintime = 1000
# maxtime = mintime + 2000

# plt.figure()
# plt.subplot(2, 1, 1)
# plt.plot(index[mintime:maxtime], data[mintime:maxtime])
# plt.xlabel('time (s)')
# plt.ylabel('microvolts (uV)')
# plt.title("Raw signal")
# plt.subplot(2, 1, 2)
# plt.plot(index[mintime:maxtime], datarec[mintime:maxtime])
# plt.xlabel('time (s)')
# plt.ylabel('microvolts (uV)')
# plt.title("De-noised signal using wavelet techniques")

# plt.tight_layout()
# plt.show()

# fs = 500
# f, t, Sxx = signal.spectrogram(data, fs)
# plt.pcolormesh(t, f, Sxx)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.ylim(0, 50)
# plt.show()









