# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:36:04 2022

@author: Asus
"""

import numpy as np
import mne
from tqdm import tqdm
import skfda
import pandas as pd
import os
import matplotlib.pyplot as plt
from skfda.exploratory.visualization import Boxplot
from skfda.inference.anova import oneway_anova
import scipy
from skfda.ml.classification import KNeighborsClassifier

from sklearn.model_selection import (train_test_split, GridSearchCV,
                                     StratifiedShuffleSplit)

import sklearn
from sklearn.cluster import AgglomerativeClustering

#canale=input('Canale: ')
#banda=input('Banda: ')

# Fp=[1, 2]
# F=[3, 4, 11, 12, 17]
# C=[5, 6, 18]
# P=[7, 8, 15, 16, 19]
# Tsx=[13]
# Tdx=[14]
# O=[9, 10]

# #Prefrontal
# Prefrontal=[]
# for i in Fp:
#     canale=str(i)
#     filename_adhd = r"C:\Users\Asus\OneDrive\Desktop\NL2\FDAxEEG\Dataset\ADHD_Matrici_pyulear\ch"+canale+"_p"+banda
#     mat = scipy.io.loadmat(filename_adhd)

#     PSD_ADHD=mat['p'].T
    
#     # for k in np.arange(len(PSD_ADHD,)):
#     #     Prefrontal[k]=Prefrontal[k].append([PSD_ADHD[k]])
    
#     Prefrontal.append([PSD_ADHD])

# Fp_ADHD=[]
# for i in np.arange(len(PSD_ADHD)):
#     Fp_ADHD.append(np.mean([Prefrontal[0][i], Prefrontal[1][i]],axis=0))

canale=input('Canale: ')
banda=input('Banda: ')

filename_adhd = r"C:\Users\Asus\OneDrive\Desktop\NL2\FDAxEEG\Dataset\ADHD_Matrici_pyulear\ch"+canale+"_p"+banda
mat = scipy.io.loadmat(filename_adhd)
PSD_ADHD=mat['p'].T
df_Channel=pd.DataFrame(data=PSD_ADHD)
Channel=df_Channel.to_numpy(dtype=None, copy=False)
Channel = np.nan_to_num(Channel)
ADHD=skfda.FDataGrid(data_matrix=Channel)
ADHD.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

ADHD.plot()

filename_control = r"C:\Users\Asus\OneDrive\Desktop\NL2\FDAxEEG\Dataset\Control_Matrici_pyulear\ch"+canale+"_p"+banda
mat = scipy.io.loadmat(filename_control)

PSD_control=mat['p'].T
    
df_Channel=pd.DataFrame(data=PSD_control)
Channel=df_Channel.to_numpy(dtype=None, copy=False)
Channel = np.nan_to_num(Channel)
Control=skfda.FDataGrid(data_matrix=Channel)
Control.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

Control.plot()

Etichette=np.append(np.zeros(427),np.ones(555))
Dati=np.concatenate((PSD_control,PSD_ADHD),axis=0)

df_Channel=pd.DataFrame(data=Dati)
Channel=df_Channel.to_numpy(dtype=None, copy=False)
Channel = np.nan_to_num(Channel)
Misto=skfda.FDataGrid(data_matrix=Channel)
Misto.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

Misto.plot()

# Dati_train, Dati_test, Etichette_train, Etichette_test = train_test_split(Misto, Etichette, test_size=0.25,
#                                                     stratify=Etichette, random_state=0)

# knn = KNeighborsClassifier()
# knn.fit(Dati_train, Etichette_train)

# pred = knn.predict(Dati_test)

# score = knn.score(Dati_test, Etichette_test)
# print(score)

v_n, p_val = oneway_anova(Control,ADHD)

# clustering = AgglomerativeClustering().fit(Dati)
# AgglomerativeClustering()