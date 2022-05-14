# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:36:04 2022

@author: Asus
"""

import numpy as np
# import mne
#from tqdm import tqdm
# from tqdm import tqdm
import skfda
import pandas as pd
from sklearn.linear_model import LogisticRegression
from skfda.inference.anova import oneway_anova
import scipy

# from sklearn.model_selection import (train_test_split, GridSearchCV,
#                                      StratifiedShuffleSplit)


#canale=input('Canale: ')
#banda=input('Banda: ')
banda=str(1)
p=[]
for i in np.arange(1,2):
    canale=str(i)
    filename_adhd = r"C:\Users\Asus\OneDrive\Desktop\NL2\FDAxEEG\Dataset\ADHD_Matrici_medie\zona"+canale+"_p"+banda
    mat = scipy.io.loadmat(filename_adhd)
    PSD_ADHD=mat['avg']
    df_Channel=pd.DataFrame(data=PSD_ADHD)
    Channel=df_Channel.to_numpy(dtype=None, copy=False)
    Channel = np.nan_to_num(Channel)
    ADHD=skfda.FDataGrid(data_matrix=Channel)
    ADHD.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

    ADHD.plot()

    filename_control = r"C:\Users\Asus\OneDrive\Desktop\NL2\FDAxEEG\Dataset\Control_Matrici_medie\zona"+canale+"_p"+banda
    mat = scipy.io.loadmat(filename_control)
    
    PSD_control=mat['avg']
        
    df_Channel=pd.DataFrame(data=PSD_control)
    Channel=df_Channel.to_numpy(dtype=None, copy=False)
    Channel = np.nan_to_num(Channel)
    Control=skfda.FDataGrid(data_matrix=Channel)
    Control.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

    Control.plot()
    
    ADHD_der=ADHD.derivative()
    ADHD_der.plot()
    
    Control_der=Control.derivative()
    Control_der.plot()
    
    Control_der.data_matrix=np.abs(Control_der.data_matrix)
    a=Control_der.integrate()

    Etichette=np.append(np.zeros(427),np.ones(555))
    Dati=np.concatenate((PSD_control,PSD_ADHD),axis=0)

    df_Channel=pd.DataFrame(data=Dati)
    Channel=df_Channel.to_numpy(dtype=None, copy=False)
    Channel = np.nan_to_num(Channel)
    Misto=skfda.FDataGrid(data_matrix=Channel)
    Misto.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

    Misto.plot()















    v_n, p_val = oneway_anova(Control,ADHD)
    p.append(p_val)