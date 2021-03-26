#-*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:05:32 2021

@author: Saadia Bayou
"""


""" Ce programme calcul les grandeurs : champs de déplacement, de contrainte , de déformation 
    et trace les courbes ur(r), sigma_rr(r), sigma_tt_(r), uz (z), sigma_zz  """

# Imports matplotlib et numpy 
import matplotlib.pyplot as plt
import numpy as np

# Données du problème

# Pression en Pascal
pi=1*1e6
pe=101325

# Dimensions en mètres
ri=0.0525 # rayon intérieur
re=0.0603 # rayon extérieur
L=0.5# longueur cylindre
e=(re-ri) # épaisseur
rm= (re+ri)/2 # rayon milieu section rectangulaire
# Caractéritiques matériaux 
EY=2.1*10e11
nu=0.3
# Limite élastique en Pa
Re=200000000
# Calcul des coefficients de Lamé mu et lambda
mu=(EY/(2*(1+nu)))
lambd=(nu*EY)/((1+nu)*(1-2*nu))


# Fonctions conversions

def convert_MPa_Pa(F):
    """Convertit une grandeur en MPa en Pa"""
    return F*(1e+6)

def convert_Pa_MPa(F):
    """Convertit une grandeur en Pa en MPa"""
    return F*(1e-6)

def convert_m_mm(l):
    """Convertit une grandeur en mètre en millimètre"""
    return l*10e3

def convert_mm_m(l):
    """Convertit une grandeur en millimètre en mètre"""
    return l*10e-3

# metre -> micrometre
def convert_m_microm (l):
    """Convertit une grandeur en mètre en micromètre"""
    L=l*(1e+06)
    return L

# Domaine radiale r
Omega_r=[ri,re]
print("\nIntervalle de l'épaisseur matériau :",Omega_r)

r=np.arange(ri,re,0.0001)
#print(" \nr = ",r)

# Domaine axiale z
Omega_z=[0,L]

z=np.arange(0,L+0.01,0.01)
#print(" \nz = ",z)

# Coefficients de Lamé
mu_MPa=convert_Pa_MPa(mu)
lambd_MPa =convert_Pa_MPa(lambd)

print("\nmu = ", mu_MPa, " MPa")
print("\nlambda = ", lambd_MPa, "MPa")

# Constantes A et B

# Constante K 
K=((pi*ri**2)/(re**2 -ri**2))
print("\nK = ",K, "Pa")
# Conversion
K_MPa=convert_Pa_MPa(K)

print("\nK en MPa = ",K_MPa, "MPa")
# Constante A
A=K/(2*(mu+lambd)) 
print("\nA =",A)

# Constante B 
B=(K*(re**2))/(2*mu) 
print("\nB =",B , "m²")

# Rapport A/B

print("\nRapport A/B =",A/B)

# Déplacements

# Déplacement radial

# Fonction déplacement radial
def depl_radial(R):
    """  Fonction calcul du déplacement radial """
    return A*R + (B/R)

# Définition déplacement radial
ur=depl_radial(r)


# Tracés du déplacement radial
plt.plot(r,ur)

# Titre et légendes graphe ur(r)
plt.title(" \nDéplacement radial ur(r) ")
plt.xlabel(" postion r en m")
plt.ylabel(" Déplacement ur en m")
# Graphe déplacement radial
plt.savefig("Fig-1-Déplacement radial ur")
plt.show()


# Contraintes

# Contrainte radiale

# Fonction contrainte radiale
def contr_radiale(R):
    """  Fonction calcul de la contrainte radial """
    return K*(1-((re**2)/(R**2)))

# Définition contrainte radiale 
sigma_rr_Pa=contr_radiale(r)

# Conversion en MPa
sigma_rr=convert_Pa_MPa(sigma_rr_Pa)
# Tracé contrainte radiale 
plt.plot(r,sigma_rr, color="r")

# Titre et légendes graphe sigma_rr(r)
plt.title(" Contrainte radiale sigma_rr(r) ")
plt.xlabel(" postion r en m")
plt.ylabel(" sigma_rr en MPa")

# Graphe  contrainte radiale 
plt.savefig("Fig-2-Contrainte radiale sigma_rr")
plt.show()


# Contrainte circonferentielle

# Fonction contrainte circonferentielle
def contr_circonf(R):
    """  Fonction calcul de la contrainte circonferentielle """
    return K*(1+((re**2)/(R**2)))

# Définition contrainte circonferentielle 
sigma_tt_Pa=contr_circonf(r)
# Conversion en MPa
sigma_tt=convert_Pa_MPa(sigma_tt_Pa)
# Tracés de la contrainte circonferentielle : sigma_théta_théta(r)
plt.plot(r,sigma_tt, color="orange")

# Titre et légendes sigma_théta_théta (r)
plt.title(" Contrainte circonferentielle sigma_tt(r) ")
plt.xlabel(" postion r en m")
plt.ylabel(" sigma_tt en MPa")

# Graphe  contrainte circonferentielle 
plt.savefig("Fig-3-Contrainte circonferentielle sigma_tt")
plt.show()


# Contrainte axiale

# Fonction contrainte axiale
def contr_axiale():
    """  Fonction calcul de la contrainte axiale """
    return (K*2*lambd)/(mu+lambd)

sigma_zz=contr_axiale()

print("\nContrainte axiale sigma_zz =", round (sigma_zz,2) , "Pa" )

sigma_zz_MPa=convert_Pa_MPa(sigma_zz)
print("\nsigma_zz =", round(sigma_zz_MPa,2), " MPa")

# Déplacement axial

# Fonction déplacement axiale
def depl_axial(Z):
    """  Fonction calcul du déplacement axial """
    return ((1/(2*mu))*(2*lambd*A+sigma_zz))*Z

# Définition contrainte axiale
uz=depl_axial(z)

# Tracés du déplacement axial uz(z)
plt.plot(z,uz,color="g")

# Titre et légendes graphe 
plt.title(" Déplacement axial uz(z) ")
plt.xlabel(" postion z en m")
plt.ylabel(" Déplacement uz en m")

# Graphe 
plt.savefig("Fig-4-Déplacement axial uz")
plt.show()

# Déformations

# Déformation radiale

# Fonction deformation radiale 
def deform_radiale(R):
    """  Fonction calcul de la déformation radiale """
    return A-(B/(R**2))


eps_rr=deform_radiale(r)
# Tracé contrainte radiale 
plt.plot(r,eps_rr, color="b")

# Titre et légendes graphe sigma_rr(r)
plt.title(" Déformation radiale epsilon_rr (r) ")
plt.xlabel(" postion r")
plt.ylabel(" eps_rr")

# Graphe  contrainte radiale 
plt.savefig("Fig-5-Déformation radiale epsilon_rr")
plt.show()


# Déformation circonferentielle

# Fonction deformation theta 
 
def deform_circonf(R):
    """ Fonction calcul de la déformation circonferentielle  """
    return A+(B/(R**2))

eps_theta_theta=deform_circonf(r)
# Tracé contrainte theta 
plt.plot(r,eps_theta_theta, color="m")

# Titre et légendes graphe sigma_theta_theta(r)
plt.title(" Déformation epsilon_tt (r) ")
plt.xlabel(" postion r")
plt.ylabel(" eps_tt")

# Graphe  contrainte theta
plt.savefig("Fig-6-Déformation epsilon_tt ")
plt.show()



# Calculs
print("\n ***** Calculs - Bloc Applications Numériques *****")

print("\nre/ri =",re/ri)


# Champ de déplacement radial
print("\ndéplacement radial en mètre :")

# Affectations
ur_ri=depl_radial(ri)
ur_rm=depl_radial(rm)
ur_re=depl_radial(re)

print("\nu_r(ri)=",round (depl_radial(ri),10), "m")
print("\nu_r(rm)=",round(depl_radial(rm),10), "m")
print("\nu_r(re)=",round(depl_radial(re),10), "m")

print("\n *** Champs de déplacement radial en micromètre *** ")

# Conversion en micromètres et affichage
ur_ri_microm=convert_m_microm (ur_ri)
print ("\nur(ri)= " , round(ur_ri_microm,3), "micromètre")

ur_milieu_microm=convert_m_microm (ur_rm)
print ("\nur(r_milieu) = " , round(ur_milieu_microm,3), "micromètre")

ur_re_microm=convert_m_microm (ur_re)
print ("\nur(re)= " , round(ur_re_microm,3) ,"micromètre")


# Champ de contrainte radiale
print(" \nChamps de contrainte radiale en Pascal ")

sigma_rr_ri=contr_radiale(ri)
sigma_rr_rm=contr_radiale(rm)
sigma_rr_re=contr_radiale(re)

print("\nsigma_rr(ri)=",round(sigma_rr_ri, 2), "Pa")
print("\nsigma_rr(r_milieu)=",round(sigma_rr_rm, 2), "Pa")
print("\nsigma_rr(re)=",round(sigma_rr_re, 2), "Pa")

print("\n ***  Champs de contraintes radiales en MégaPascal  *** ")

# Conversion
sigma_rr_ri_MPa=convert_Pa_MPa(sigma_rr_ri)
sigma_rr_rm_MPa=convert_Pa_MPa(sigma_rr_rm)
sigma_rr_re_MPa=convert_Pa_MPa(sigma_rr_re)


print("\nsigma_rr(ri)=",round(sigma_rr_ri_MPa, 2), "MPa")
print("\nsigma_rr(r_milieu)=",round(sigma_rr_rm_MPa, 2), "MPa")
print("\nsigma_rr(re)=",round(sigma_rr_re_MPa, 2), "MPa")


# Champ de contrainte circonférentielle
 
print ("\n** Contrainte circonférentielle ** : ")

sigma_tt_ri=contr_circonf(ri)
sigma_tt_rm=contr_circonf(rm)
sigma_tt_re=contr_circonf(re)

print("\nsigma_tt(ri)=",round(sigma_tt_ri, 2), "Pa")
print("\nsigma_tt(r_milieu)=",round(sigma_tt_rm, 2), "Pa")
print("\nsigma_tt(re)=",round(sigma_tt_re, 2), "Pa")


print("\n ***  Champs de contraintes circonferentielle en MégaPascal  *** ")

# Conversion
sigma_tt_ri_MPa=convert_Pa_MPa(sigma_tt_ri)
sigma_tt_rm_MPa=convert_Pa_MPa(sigma_tt_rm)
sigma_tt_re_MPa=convert_Pa_MPa(sigma_tt_re)

print("\nsigma_rr(ri)=",round(sigma_tt_ri_MPa, 2), "MPa")
print("\nsigma_rr(r_milieu)=",round(sigma_tt_rm_MPa, 2), "MPa")
print("\nsigma_rr(re)=",round(sigma_tt_re_MPa, 2), "MPa")

#sigma_tt_max=convert_Pa_MPa(contr_circonf(ri))
sigma_tt_max_MPa=convert_Pa_MPa(contr_circonf(ri))
print ("\nsigma_tt_max en MPa :\n \nsigma_tt_max =", round(sigma_tt_max_MPa,2), "MPa")


print("\nepsilon_rr(ri)=",round(deform_radiale(ri), 10))
print("\nepsilon_rr(ri+re/2)=",round(deform_radiale((ri+re)/2), 10))
print("\nepsilon_rr(re)=",round(deform_radiale(re), 10))


print("\nCalcul pi_max")
# conversion 
l_e=convert_MPa_Pa(200) # limite élastique l_e
# On pose a et b tels que :
a=((re**2)/(ri**2))
b=((re**2)-(ri**2))
pi_max=(l_e/((1+a)*(ri**2)/b))

print("\npi_max=",pi_max, "Pa")

pi_max_MPa =convert_Pa_MPa(pi_max)

print("\npi_max=",pi_max_MPa, "MPa")


# rapport Re/sigma_tt_max

# Limite élatique 
print("\nLimite élastique, \nRapport sigma_tt_max/Re")
lim_elast=sigma_tt_max_MPa/Re
print("\nsigma_tt_max/Re =",round(lim_elast,10))