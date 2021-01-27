from random import randint
from dessin_pendu import *

def enregistrement_des_mots():
    x= randint(1,1)
    w=0
    liste_dictee=[]
    with open(f'../répertoire_fichiers_texte_dictée/dictée_{x}.txt','r') as f:
        for ligne in f:
            ligne=ligne.replace("\n", "")
            liste_dictee.append(ligne)
            w+=1
    return list(liste_dictee), w

def choix_du_mot(liste_dictee):
    a=randint(0,len(liste_dictee)-1)
    mot= liste_dictee[a]
    del liste_dictee[a]
    return mot, liste_dictee

def transformation_mot(mot):
    mot= list(mot.strip())
    mot_vide=[]
    for i in range(len(mot)):
        mot_vide.append('_')
    return mot_vide

def detection_victoire():
    mot=str(choix_du_mot)
    if score==len(mot):
        return True
    else:
        pass

def faute(x):
    faute=f+x
    x+=1
    return x, faute

def detection_lettre(a,b):
    commun=0
    for i in range(len(mot)):
        lettre= mot[i]
        if lettre==a:
            commun+=1
        if commun==0:
            return faute, mot_vide
        return mot_vide

'''Code principal et m*rdier'''
score=0
f=0
x=0
liste_dictee, nombre_de_mots= enregistrement_des_mots()
while len(liste_dictee)!=0:
    x, faute=faute(x)
    mot, liste_dictee=choix_du_mot(liste_dictee)
    mot_vide=transformation_mot(mot)
    while faute!=7 or detection_victoire()!=True:
        a=input('Choisissez une lettre')
        mot_vide=detection_lettre(a,faute)
        print(mot_vide)
        pass
        
    if detection_victoire==True:
        pass