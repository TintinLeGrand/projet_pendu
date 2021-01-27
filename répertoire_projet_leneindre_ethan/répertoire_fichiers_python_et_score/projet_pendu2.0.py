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
    print(mot)
    return mot, liste_dictee

def transformation_mot(mot):
    mot= list(mot.strip())
    mot_vide=[]
    for i in range(len(mot)):
        mot_vide.append('_')
    print(mot_vide)
    return mot_vide

def detection_victoire():
    mot=str(choix_du_mot)
    if score==len(mot):
        return True
    else:
        pass

def detection_lettre(a,b):
    commun=0
    etat=False
    for i in range(len(mot)):
        lettre= mot[i]
        if lettre==a:
            commun+=1
    if commun==0:
        b+=1
        etat=True
    return b, mot_vide, etat
    
def enregistrer_score(score):
    with open('score.txt','a') as f:
        f.write(str(score)+'\n \n')
    
def reset():
    f=0
    x=0
    faute=0
    return f, x, faute

'''Code fumier'''
phrase_bien=["J'ai un champion en face de moi !", "Tu es trop fort !", "Bonne réponse !", "Ouah, mais tu triches ?", "T'es le plus fort"]
score=0
liste_dictee, nombre_de_mots= enregistrement_des_mots()
nombre_mots=len(liste_dictee)
while nombre_mots>1:
    f, x, faute=reset()
    mot, liste_dictee=choix_du_mot(liste_dictee)
    mot_vide=transformation_mot(mot)
    while f!=1:
        a=input('Choisissez une lettre')
        faute, mot_vide, etat=detection_lettre(a,faute)
        if faute>=7:
            f=1
        affichage_du_mort(faute)
        if etat==False:
            print(phrase_bien[randint(0,4)])
    if detection_victoire==True:
        print(phrase_victoire(randint(1,6)))
        