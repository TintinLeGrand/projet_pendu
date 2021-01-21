from random import randint
from dessin_pendu import *

def detection_lettre():
    pass

def enregistrer_score():
    with open('score.txt','a') as f:
        f.write(str(score)+'\n \n')

def phrase_bien():
    phrase= randint(1,5)
    return phrase
    
phrase_bien=["J'ai un champion en face de moi !", "Tu es trop fort !", "Bonne réponse !", "Ouah, mais tu triches ?", "T'es le plus fort"]

def enregistrement_des_mots():
    x= randint(1,1)
    liste_dictee=[]
    with open(f'../répertoire_fichiers_texte_dictée/dictée_{x}.txt','r') as f:
        for ligne in f:
            liste_dictee.append(ligne)
    return liste_dictee