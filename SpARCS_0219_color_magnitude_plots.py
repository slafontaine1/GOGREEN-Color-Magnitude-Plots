import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os

UVJinfo = pd.read_csv('UBVJ_MASTER_SpARCS_0219.csv')
KJzRinfo = pd.read_csv('SpARCS_0219_totalall_FOURSTARKs_photom.csv')

ID = KJzRinfo.id
k_flux = KJzRinfo.FOURSTARKs_tot
R_flux = KJzRinfo.VIMOSR
z_flux = KJzRinfo.VIMOSz
J_flux = KJzRinfo.FOURSTARJ
k_star = KJzRinfo.K_star
mask = KJzRinfo.totmask
IDUVJ = UVJinfo.PHOTID
CLUSTERZ = UVJinfo.CLUSTERZ
indivz = UVJinfo.INDIVZ
U_V = UVJinfo.U_V
V_J = UVJinfo.V_J



J_K = 2.5*np.log10(k_flux/J_flux)
z_K = 2.5*np.log10(k_flux/z_flux)
R_K = 2.5*np.log10(k_flux/R_flux)
K = -2.5*np.log10(k_flux) + 25


a = 0
JMINK = np.zeros((len(k_star),1), dtype=float)
zMINK = np.zeros((len(k_star),1), dtype=float)
RMINK = np.zeros((len(k_star),1), dtype=float)
UMINV = np.zeros((len(k_star),1), dtype=float)
VMINJ = np.zeros((len(k_star),1), dtype=float)
KMAG = np.zeros((len(k_star),1), dtype=float)
for i in range(len(k_star)):
    JMINK[a]=J_K[i]
    zMINK[a]=z_K[i]
    RMINK[a]=R_K[i]
    UMINV[a]=U_V[i]
    VMINJ[a]=V_J[i]
    KMAG[a]=K[i]
    a=a+1
    

goodJK = np.where((k_star < 0.97) & (mask ==0) & (~np.isnan(J_K[i]) == True))
goodzK = np.where((k_star < 0.97) & (mask ==0) & (~np.isnan(z_K[i]) == True))
goodRK = np.where((k_star < 0.97) & (mask ==0) & (~np.isnan(R_K[i]) == True))
goodUVJ = np.where((k_star < 0.97) & (mask ==0))
