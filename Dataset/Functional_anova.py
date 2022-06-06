# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:45:08 2022

@author: Asus
"""

# loading the packages
import numpy as np
from tqdm import tqdm
import skfda
import pandas as pd
import os
# from skfda.exploratory.visualization import Boxplot
from skfda.inference.anova import oneway_anova
import scipy
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import  train_test_split
import matplotlib.pyplot as plt
from scipy.stats import permutation_test
from skfda.ml.classification import LogisticRegression
from numpy import array
from skfda.preprocessing.dim_reduction import FPCA
from skfda.exploratory.visualization import FPCAPlot
from skfda.representation.basis import BSpline, Fourier, Monomial


home_path = os.path.abspath(os.getcwd())
home_path

def FAnova(canale, banda, home_path):
    
    # loading the data of ADHD
    filename_adhd = home_path+"\ADHD_Matrici_medie\zona"+str(canale)+"_p"+str(banda)
    mat = scipy.io.loadmat(filename_adhd)
    PSD_ADHD=mat['avg']
    df_Channel=pd.DataFrame(data=PSD_ADHD)
    Channel=df_Channel.to_numpy(dtype=None, copy=False)
    Channel = np.nan_to_num(Channel)
    ADHD=skfda.FDataGrid(data_matrix=Channel)
    ADHD.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

    # loading the data of control
    filename_control = home_path+"\Control_Matrici_medie\zona"+str(canale)+"_p"+str(banda)
    mat = scipy.io.loadmat(filename_control)
    PSD_control=mat['avg']
    df_Channel=pd.DataFrame(data=PSD_control)
    Channel=df_Channel.to_numpy(dtype=None, copy=False)
    Channel = np.nan_to_num(Channel)
    Control=skfda.FDataGrid(data_matrix=Channel)
    Control.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

    v_n, p_val = oneway_anova(Control, ADHD)
    
    dati = ADHD.concatenate(Control)
    
    fpca = FPCA(n_components=5)
    fpca.fit(dati)
    fpca.components_.plot()

    return p_val

p_val = np.empty((7,5))

for canale in range(1,8):
    for banda in range(1,6):
        p_val[(canale-1), (banda-1)] = FAnova(canale, banda, home_path) 
        
print(pd.DataFrame(p_val))







