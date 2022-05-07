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

canale=str(1)
banda=str(1)
filename_adhd = r"C:\Users\Asus\OneDrive\Desktop\NL2\FDAxEEG\Dataset\ADHD_Matrici_pyulear\ch"+canale+"_p"+banda
mat = scipy.io.loadmat(filename_adhd)

PSD_ADHD=mat['p'].T
    
df_Channel=pd.DataFrame(data=PSD_ADHD)
Channel=df_Channel.to_numpy(dtype=None, copy=False)
Channel = np.nan_to_num(Channel)
DG_Channel=skfda.FDataGrid(data_matrix=Channel)
DG_Channel.interpolation=skfda.representation.interpolation.SplineInterpolation(interpolation_order=3)

DG_Channel.plot()