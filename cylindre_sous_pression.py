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
nu=0.3

# Calcul des coefficients de Lamé mu et lambda

mu=(EY/(2*(1+nu)))
lambd=(nu*EY)/((1+nu)*(1-2*nu))

print("\nmu =", mu)
print("\nlambda =", lambd)



Omega_r=[ri,re]
print("\nIntervalle de l'épaisseur matériau :",Omega_r)

# Domaine radiale r
r=np.arange(ri,re,0.0001)
print(" \nr = ",r)

# Domaine axiale z
Omega_z=[0,L]
z=np.arange(0,L+0.01,0.01)
print(" \nz = ",z)

# conversion

def convert_MPa_Pa(F):
    return F*(1e+6)

def convert_Pa_MPa(F):
    return F*(1e-6)

def convert_m_mm(l):
    return l*1e3

def convert_mm_m(l):
    return l*1e-3


# Constantes A et B

K=((pi*ri**2)/(re**2 -ri**2))

A=K/(2*(mu+lambd)) 
print("\nA =",A)

B=(K*(re**2))/(2*mu) 

print("\nB =",B)

#print("\nA/B= ",A/B)
#print("\nB/A= ",B/A)

# Déplacements

# Déplacement radial

def depl_radial(R):
    return A*R + (B/R)

ur=depl_radial(r)

# Tracés du déplacement radial
 
plt.plot(r,ur)

plt.title(" \nDéplacement radial ur(r) ")
plt.xlabel(" postion r")

plt.ylabel(" Déplacement ur")

plt.savefig("Fig-1-Déplacement radial ur")
plt.show()


# Contraintes

# Contrainte radiale

def contr_radiale(R):
    return K*(1-((re**2)/(R**2)))
    
sigma_rr=contr_radiale(r)

plt.plot(r,sigma_rr, color="r")

plt.title(" Contrainte radiale sigma_rr(r) ")

plt.xlabel(" postion r")
plt.ylabel(" sigma_rr")

plt.savefig("Fig-2-Contrainte radiale sigma_rr")
plt.show()


# Contrainte circonferentielle

def contr_circonf(R):
    return K*(1+((re**2)/(R**2)))

sigma_theta_theta=contr_circonf(r)
    
plt.plot(r,sigma_theta_theta, color="g")

plt.title(" Contrainte circonferentielle sigma_théta-théta(r) ")

plt.xlabel(" postion r")
plt.ylabel(" sigma_théta-théta")

plt.savefig("Fig-3-Contrainte circonferentielle sigma_théta-théta")
plt.show()

# Contrainte axiale

def contr_axiale(Z):
    return K*(lambd/(lambd+mu))*Z
    
sigma_zz=contr_axiale(z)

plt.plot(z,sigma_zz, color="orange")

plt.title(" Contrainte axiale sigma_zz(z) ")

plt.xlabel(" postion z")
plt.ylabel(" sigma_zz")

plt.savefig("Fig-4-Contrainte axiale sigma_zz")
plt.show()


