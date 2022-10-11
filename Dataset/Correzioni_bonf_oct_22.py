# loading the packages
import numpy as np
# import mne
from tqdm import tqdm
# from tqdm import tqdm
import skfda
import pandas as pd
# import os
# import matplotlib.pyplot as plt
# from skfda.exploratory.visualization import Boxplot
from skfda.inference.anova import oneway_anova
import scipy
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import  train_test_split
import matplotlib.pyplot as plt
from scipy.stats import permutation_test


# getting the home path
home_path = os.path.abspath(os.getcwd())
home_path

## FUNCTIONS ##

# function to compute the integral of the first derivative
def Integrale(canale, banda, home_path):
    
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

    # compute the derivatives of the functions
    ADHD_der=ADHD.derivative()
    Control_der=Control.derivative()

    # integral of the derivative of the adhd group
    ADHD_der_abs = ADHD_der
    ADHD_der_abs.data_matrix=np.abs(ADHD_der.data_matrix)

    n_adhd = ADHD_der_abs.data_matrix.shape[0]

    int_adhd = np.empty(n_adhd)
    for i in range(n_adhd):
        int_adhd[i]=scipy.integrate.simpson(np.transpose(ADHD_der_abs.data_matrix[i]), ADHD_der_abs.grid_points[0])
        

    # integral of the derivative of the control group
    Control_der_abs = Control_der
    Control_der_abs.data_matrix=np.abs(Control_der.data_matrix)

    n_cont = Control_der_abs.data_matrix.shape[0]

    int_cont = np.empty(n_cont)
    for i in range(n_cont):
        int_cont[i]=scipy.integrate.simpson(np.transpose(Control_der_abs.data_matrix[i]), Control_der_abs.grid_points[0])

    return int_adhd, int_cont


# function to compute the norm
def Norma(canale, banda, home_path, order=2):
    
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

    # L2 norm of ADHD group
    n_adhd = ADHD.data_matrix.shape[0]

    norm_adhd = np.empty(n_adhd)
    for i in range(n_adhd):
        norm_adhd[i]=np.linalg.norm(ADHD.data_matrix[i], ord = order)

    # L2 norm of control group
    n_cont = Control.data_matrix.shape[0]

    norm_cont = np.empty(n_cont)
    for i in range(n_cont):
        norm_cont[i]=np.linalg.norm(Control.data_matrix[i], ord = order)

    # ANOVA

    #aov = scipy.stats.f_oneway(norm_adhd,norm_cont, axis=0)
    # print("ANOVA results: \nF statistics: \t"+str(aov.statistic)+"\np_value: \t"+ str(aov.pvalue))

    #res = permutation_test((norm_adhd, norm_cont), statistic, alternative='two-sided')
    return norm_adhd, norm_cont

# function to return the max
def Picco(canale, banda, home_path):
    
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

    Picco_ADHD=ADHD.data_matrix.max(1)

    Picco_Control=Control.data_matrix.max(1)

    return Picco_ADHD, Picco_Control



## TESTS ##

alpha = 0.05

#coeff Bonferroni correction
k_bonf = 105
# I have 5 bands for 7 channels for 3 features
# 7*5*3 = 105

alpha_bonf = alpha/k_bonf



# upload p-values already computed



## INTEGRAL ##
# intergal p-val
p_val_int = np.array([0.5286,  0.4052,  0.3312,  0.1022,  0.2952,
                      0.0454,  0.0394,  0.0002,  0.0002,  0.2352,
                      0.4528,  0.5666,  0.1252,  0.1166,  0.7752,
                      0.6408,  0.5594,  0.6018,  0.0728,  0.0014,
                      0.3272,  0.2708,  0.1088,  0.2588,  0.0224,
                      0.1526,  0.9322,  0.3024,  0.2476,  0.0456,
                      0.0002,  0.0002,  0.0032,  0.0304,  0.4020])

indxs = np.where(p_val_int <= alpha_bonf)[0]
#print(indxs)

# per risalire dall'elemento del vettore al canale e banda basta sapere che se ci si trova in
# posizione i 
# i = 5*zona + banda
# zona = i mod 5 
# banda = i - i mod 5 * 5

matrice_int_adhd = np.empty((555,indxs.size))
matrice_int_cont = np.empty((427,indxs.size))

# salvo le features di mio interesse
# della zona e banda di mio interesse devo avere vettore integrali di adhd e vettore integrali di control
for i,indx in enumerate(indxs):
    zona = indx//5
    banda = indx - indx//5*5
    int_adhd, int_cont = Integrale(canale=zona+1,  banda=banda+1, home_path=home_path)
    matrice_int_adhd[:,i] = int_adhd
    matrice_int_cont[:,i] = int_cont
    
mat_int_adhd = pd.DataFrame(matrice_int_adhd)
mat_int_cont = pd.DataFrame(matrice_int_cont)

mat_int_adhd.to_csv(home_path+'\Bonf_Feat_int_adhd.csv', index = False, sep = ',')
mat_int_cont.to_csv(home_path+'\Bonf_Feat_int_cont.csv', index = False, sep = ',')



## NORM ##
p_val_norm = np.array([0.6820,  0.6504,  0.3608,  0.0118,  0.3410,
                    0.0002,  0.0012,  0.0002,  0.0002,  0.1232,
                    0.2532,  0.1022,  0.2542,  0.2148,  0.4512,
                    0.8926,  0.8962,  0.1468,  0.0526,  0.0016,
                    0.0204,  0.2140,  0.1850,  0.2968,  0.0410,
                    0.6058,  0.0620,  0.4740,  0.3442,  0.0656,
                    0.0002,  0.0002,  0.0062,  0.0164,  0.9768])


indxs = np.where(p_val_norm <= alpha_bonf)[0]
#print(indxs)

matrice_norm_adhd = np.empty((555,indxs.size))
matrice_norm_cont = np.empty((427,indxs.size))

# salvo le features di mio interesse
# della zona e banda di mio interesse devo avere vettore integrali di adhd e vettore integrali di control
for i,indx in enumerate(indxs):
    zona = indx//5
    banda = indx - indx//5*5
    norm_adhd, norm_cont = Norma(canale=zona+1,  banda=banda+1, home_path=home_path)
    matrice_norm_adhd[:,i] = norm_adhd
    matrice_norm_cont[:,i] = norm_cont

pd.DataFrame(matrice_norm_adhd).to_csv(home_path+'\Bonf_Feat_norm_adhd.csv', index = False, sep = ',')
pd.DataFrame(matrice_norm_cont).to_csv(home_path+'\Bonf_Feat_norm_cont.csv', index = False, sep = ',')



## MAX ##
p_val_picco = np.array([0.7554,  0.2928,  0.1538,  0.0290,  0.2234,
                    0.0880,  0.1310,  0.0004,  0.0002,  0.9514,
                    0.2384,  0.4092,  0.7544,  0.0978,  0.7872,
                    0.9306,  0.5938,  0.4330,  0.0506,  0.0004,
                    0.3982,  0.7732,  0.2830,  0.1536,  0.0210,
                    0.2098,  0.9840,  0.9844,  0.7440,  0.0310,
                    0.0002,  0.0002,  0.0150,  0.0030,  0.1934])


indxs = np.where(p_val_picco <= alpha_bonf)[0]
# print(indxs)

matrice_picco_adhd = np.empty((555,indxs.size))
matrice_picco_cont = np.empty((427,indxs.size))

# salvo le features di mio interesse
# della zona e banda di mio interesse devo avere vettore integrali di adhd e vettore integrali di control
for i,indx in enumerate(indxs):
    zona = indx//5
    banda = indx - indx//5*5
    picco_adhd, picco_cont = Picco(canale=zona+1,  banda=banda+1, home_path=home_path)
    matrice_picco_adhd[:,i] = np.reshape(picco_adhd, (555,))
    matrice_picco_cont[:,i] = np.reshape(picco_cont, (427,))
    
    print('Zona: '+str(zona)+'\tBanda: '+str(banda))

pd.DataFrame(matrice_picco_adhd).to_csv(home_path+'\Bonf_Feat_picco_adhd.csv', index = False, sep = ',')
pd.DataFrame(matrice_picco_cont).to_csv(home_path+'\Bonf_Feat_picco_cont.csv', index = False, sep = ',')






