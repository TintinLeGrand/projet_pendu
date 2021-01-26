from random import randint
from dessin_pendu import *

faute=0

def detection_lettre():
    for i in range(len(liste_dictee[num])):
        if 

def enregistrer_score():
    with open('score.txt','a') as f:
        f.write(str(score)+'\n \n')

def choix_du_mot(liste_dictee):
    lettre=0
    for i in range(len(liste_dictee)):
        if 
    return liste_dictee[num]

def faute():
    if faute==7:
        return True
    dessin_pendu[faute]
    faute+=1

def enregistrement_des_mots():
    x= randint(1)
    liste_dictee=[]
    with open(f'../répertoire_fichiers_texte_dictée/dictée_{x}.txt','r') as f:
        for ligne in f:
            liste_dictee.append(ligne)
    return liste_dictee

def phrase_bien():
    phrase= randint(1,5)
    return phrase_bien[phrase]
    
def main():
    enregistrement_des_mots()
    choix_du_mot(liste_dictee)
    while faute!=True or victoire!=True:
        choix_lettre()
    if victoire==True:
        victoire()
        faute=0
    
phrase_bien=["J'ai un champion en face de moi !", "Tu es trop fort !", "Bonne réponse !", "Ouah, mais tu triches ?", "T'es le plus fort"]