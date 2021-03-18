# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:05:32 2021

@author: Saadia Bayou
"""


# Imports des bibliothèques matplotlib et numpy 
import matplotlib.pyplot as plt
import numpy as np

# Données 
# Pression en Pascal
pi=1*10e6
pe=101325
# Dimensions e mètres
ri=0.0525
re=0.0603
L=0.5
e=(re-ri)

# Caractéritiques matériaux 
EY=2.1*10e11
mu=0.3

Dr=[ri,re]
print(Dr)

# Domaine radiale r
r=np.arange(ri,re,0.0001)
print(" \nr = ",r)

# Domaine axiale z
Dz=[0,L]
z=np.arange(0,L+0.01,0.01)
print(" \nz = ",z)


# Constantes A et B

K=((pi*ri**2)/(re**2 -ri**2))

A=(K*(1+mu)*(1-(2*mu)))/(EY)
print("\nA =",A)

B=(K*(1+mu)*(re**2))/(EY) 
print("\nB =",B)

print("\nA/B= ",A/B)

# Déplacements

# Déplacement radial
ur=A*r + (B/r)
    
plt.plot(r,ur)

plt.title(" \nDéplacement radial ur(r) ")
plt.xlabel(" postion r")
plt.ylabel(" Déplacement ur")

plt.savefig("Fig-1-Déplacement radial ur")
plt.show()





# Contraintes
    
sigma_rr=K*(1-((re**2)/(r**2)))

plt.plot(r,sigma_rr, color="r")
plt.title(" Contrainte radiale ur(r) ")
plt.xlabel(" postion r")
plt.ylabel(" sigma_rr")

plt.savefig("Fig-2-Contrainte radiale sigma_rr")
plt.show()

