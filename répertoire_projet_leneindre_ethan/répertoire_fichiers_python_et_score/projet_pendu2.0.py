from random import randint
from dessin_pendu import *
import time
import datetime

def enregistrement_des_mots():
    x= randint(1,1)
    nombre_de_mots=0
    liste_dictee=[]
    with open(f'../répertoire_fichiers_texte_dictée/dictée_{x}.txt','r') as f:
        for ligne in f:
            ligne=ligne.replace("\n", "")
            liste_dictee.append(ligne)
            nombre_de_mots+=1
    return list(liste_dictee), nombre_de_mots

def choix_du_mot(liste_dictee):
    a=randint(0,len(liste_dictee)-1)
    mot= liste_dictee[a]
    del liste_dictee[a]
    return mot, liste_dictee

def transformation_mot(mot):
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

def detection_lettre(lettre,le_mot,mot_en_cours):
    etat=False
    for i in range(len(le_mot)):
        if lettre==le_mot[i]:
            mot_en_cours[i]=lettre
            etat=True
    return mot_en_cours, etat

def enregistrer_score(score, date):
    with open('score.txt','a') as f:
        f.write(date+ "Score atteint lors de la session : "+ str(score)+'%.\n\n')
    
def reset():
    f=0
    x=0
    faute=0
    return f, x, faute

'''Code principal'''
phrase_bien=["J'ai un champion en face de moi !", "Tu es trop fort !", "Bonne réponse !", "Ouah, mais tu triches ?", "T'es le plus fort"]
points=0
score=0
liste_dictee, nombre_de_mots= enregistrement_des_mots()
total=nombre_de_mots
while nombre_de_mots>1:
    nombre_de_mots=len(liste_dictee)
    f, x, faute=reset()
    mot, liste_dictee=choix_du_mot(liste_dictee)
    mot_vide=transformation_mot(mot)
    print(f'\033[34mNouveau mot :{mot_vide}')
    mot_en_cours=mot_vide
    while f!=1:
        ltr=input('\033[30mChoisissez une lettre')
        mot_en_cours, etat=detection_lettre(ltr,mot,mot_en_cours)
        affichage_du_mort(faute)
        if etat==False:
            faute+=1
        if faute>=8:
            f=1
            print(f"\033[31mMot perdu, c'était le mot {mot}.\n____________________\n")
            time.sleep(3)
        if faute<8:
            print(f'\033[30m{mot_en_cours}')
        if etat==True:
            print(f'\033[30m{phrase_bien[randint(0,4)]}\n')
        if mot_en_cours==list(mot.strip()):
            f=1
            points=points+1
            print("\033[32mMot trouvé !\n____________________\n")
            time.sleep(3)
score=int(100*points/total)
print(f'Le score est de {score}%')
date= datetime.datetime.now().strftime("Le %d/%m/%Y à %H:%M:%S : ")
enregistrer_score(score, date)