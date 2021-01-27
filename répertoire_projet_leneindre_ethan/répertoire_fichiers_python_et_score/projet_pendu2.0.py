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
    a=randint(1,len(liste_dictee))
    mot= liste_dictee[a]
    del liste_dictee[a]
    return mot, liste_dictee

def detection_lettre(mot):
    mot= list(mot.strip())
    mot_vide=[]
    for i in range(len(mot)):
        mot_vide.append('_')
    return mot_vide

'''Code principal et m*rdier'''
score=0
faute=0
liste_dictee, nombre_de_mots= enregistrement_des_mots()
while len(liste_dictee)!=0:
    mot, liste_dictee=choix_du_mot(liste_dictee)