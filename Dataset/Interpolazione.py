# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:36:04 2022

@author: Asus
"""

import numpy as np
import os
from scipy.stats import f_oneway
import skfda
import pandas as pd
from skfda.inference.anova import oneway_anova
import scipy
from skfda.ml.classification import LogisticRegression
from numpy import array

home_path = os.path.abspath(os.getcwd())
home_path

def LogReg(canale, banda, home_path):
    filename_adhd = home_path+"\ADHD_Matrici_medie\zona"+str(canale)+"_p"+str(banda)
    mat = scipy.io.loadmat(filename_adhd)
    PSD_ADHD=mat['avg']
    df_Channel=pd.DataFrame(data=PSD_ADHD)
    Channel=df_Channel.to_numpy(dtype=None, copy=False)
    Channel = np.nan_to_num(Channel)
    ADHD=skfda.FDataGrid(data_matrix=Channel)
    ADHD.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)


    filename_control = home_path+"\Control_Matrici_medie\zona"+str(canale)+"_p"+str(banda)
    mat = scipy.io.loadmat(filename_control)
    
    PSD_control=mat['avg']
        
    df_Channel=pd.DataFrame(data=PSD_control)
    Channel=df_Channel.to_numpy(dtype=None, copy=False)
    Channel = np.nan_to_num(Channel)
    Control=skfda.FDataGrid(data_matrix=Channel)
    Control.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

    
    dati = ADHD.concatenate(Control)
    y = 555*[1] + 427*[0]

    lr = LogisticRegression()
    lr.__init__(p=5, solver='lbfgs', max_iter=100)
    _ = lr.fit(dati[::2], y[::2])
    lr.coef_.round(2)
    lr.points_.round(2)
    score=lr.score(dati[1::2],y[1::2])
    
    return score

score = np.empty((7,5))

for canale in range(1,8):
    for banda in range(1,6):
        score[(canale-1), (banda-1)] = LogReg(canale, banda, home_path) 

print(pd.DataFrame(score))