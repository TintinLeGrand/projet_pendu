from random import randint
from dessin_pendu import *

def victoire():
    mot=str(choix_du_mot)
    if score==len(mot):
        return True
    else:
        pass

def score():
    pass

def detection_lettre():
    mot= choix_du_mot(liste_dictee)
    mot= list(str(mot).strip())
    mot_vide=[]
    for i in range(len(mot)):
        mot_vide.append('_')
    return mot_vide

def enregistrer_score():
    with open('score.txt','a') as f:
        f.write(str(score)+'\n \n')

def choix_du_mot(liste_dictee):
    a=randint(1,len(liste_mots)-1)
    mot= liste_dictee[a]
    del liste_dictee[a]
    return mot, liste_dictee

def faute():
    if faute==7:
        return True
    else:
        return False
    dessin_pendu[faute]
    faute+=1

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

"""def phrase_bien():
    phrase= int(randint(1,5))
    phrase= phrase_bien[phrase]
    return phrase"""    

'''Petit tas de code'''
score=0
phrase_bien=["J'ai un champion en face de moi !", "Tu es trop fort !", "Bonne réponse !", "Ouah, mais tu triches ?", "T'es le plus fort"]
faute=0
partie=0
liste_dictee,w=enregistrement_des_mots()
liste_mots= enregistrement_des_mots()
while partie!=w:
    victoire=victoire()
    choix_du_mot(list(enregistrement_des_mots()))
    while faute!=True or victoire!=True:
        detection_lettre()
    if victoire==True:
        victoire()
        faute=0
reponse=input("Choisissez une lettre\n->")