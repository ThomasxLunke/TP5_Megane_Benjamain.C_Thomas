


                # TP5 
                # GROUPES : Thomas SIDAMBAROM, Megan MORTREUX, Benjamin CASSE




################################################ FONCTIONS OUTILS #########################################################################################################################################################################################

def no_space(noms): # Feature 8. Fonction qui permet d'enlever les espaces dans la liste de prénoms en entrée. Elle permet également de créer une liste avec tous les noms. EX : entrée : "bob      ,amy,jerry",   sortie : ['bob','amy','jerry']
    noms = noms.replace(" ", "")
    liste_noms = noms.split(",")
    return liste_noms

def capitalize(liste_noms): # Fonction qui prend une liste de prénom en entrée, et retourne une liste de prénom avec une masjucule à chaque premieres lettres de chaque prénom et des minuscules pour les autres lettres de chaque prénom. EX : entrée : ['bOb','AMY','jerry'],    sortie : ['Bob','Amy','Jerry']
    compteur = 0
    for compteur in range(len(liste_noms)):
        if isinstance(liste_noms[compteur], str) and liste_noms[compteur] [0] != '"':
            liste_noms[compteur] = liste_noms[compteur].lower()
            liste_noms[compteur] = liste_noms[compteur].capitalize()
    return liste_noms

def creation_delete(noms): # Fonction qui permet de supprimer les prénoms avec "!" au début ainsi que leurs homologue sans "!" 
    compteur1 = 0
    compteur2 = 0
    liste_noms = []
    liste_noms = no_space(noms)
    delete = []
    
    for compteur1 in range(len(liste_noms)): # Cette boucle permet de placer dans la liste "delete" tous les noms avec pour premier caractère "!"
        if liste_noms[compteur1][0] == "!":
            liste_noms[compteur1] = liste_noms[compteur1].replace("!", "")
            delete.append(liste_noms[compteur1])

    for compteur2 in range(len(delete)): # Cette boucle permet de supprimer toutes les occurences entre les prénoms de "delete" et les prénoms de "liste-noms"
        compteur1 = 0
        while compteur1 < len(liste_noms):
            if delete[compteur2] == liste_noms[compteur1]:
                liste_noms.remove(liste_noms[compteur1])
            else:
                compteur1 = compteur1 + 1

    return liste_noms

################################################ FONCTIONS AFFICHAGE #########################################################################################################################################################################################

def affichage(noms, nbFct):
    nomsfinal = ""
    compteur = 0
    if (nbFct == 0):
        for compteur in range(len(noms)):  
            nomTmp = noms[compteur]
            nomsfinal = nomsfinal + " " + nomTmp
            nomTmp = ""


    elif (nbFct == 1):
        for compteur in range(len(noms)): 
            nomTmp = noms[compteur]
            nomsfinal = nomsfinal + ", " + nomTmp
            nomTmp = ""
    

    elif (nbFct == 2):
        for compteur in range(len(noms)): 
            if (compteur == len(noms) - 1) and len(noms) != 1:
                nomTmp = noms[compteur]
                nomsfinal = nomsfinal + " and " + nomTmp
                nomTmp = ""
            else:
                nomTmp = noms[compteur]
                nomsfinal = nomsfinal + ", " + nomTmp
                nomTmp = ""


    elif (nbFct == 3):
        for compteur in range(len(noms)):  # print
            if (compteur == len(noms) - 1):
                nomTmp = noms[compteur]
                nomsfinal = nomsfinal + "and " + nomTmp 
                nomTmp = ""
            else:
                nomTmp = noms[compteur]
                nomsfinal = nomsfinal + nomTmp + ", "
                nomTmp = ""


    elif (nbFct == 10): # Feature 10
        while compteur < len(noms):
            if noms[compteur + 1] == 1:
                if (compteur == len(noms) - 2):
                    nomTmp = noms[compteur]
                    nomsfinal = nomsfinal + " and " + nomTmp
                    nomTmp = ""
                    compteur = compteur + 2
                else:
                    nomTmp = noms[compteur]
                    nomsfinal = nomsfinal + ", " + nomTmp
                    nomTmp = ""
                    compteur = compteur + 2
            else:
                if (compteur == len(noms) - 2):
                    nomTmp = noms[compteur]
                    nomsfinal = nomsfinal + " and " + nomTmp + " " + "(" + "x" + str(noms[compteur + 1]) + ")"
                    nomTmp = ""
                    compteur = compteur + 2
                else:
                    nomTmp = noms[compteur]
                    nomsfinal = nomsfinal + ", " + nomTmp + " " + "(" + "x" + str(noms[compteur + 1]) + ")"
                    nomTmp = ""
                    compteur = compteur + 2
    

    elif (nbFct == 11): # Feature 11
        return "Hello, world !"


    elif (nbFct == 12): # Feature 12
        return "HELLO, WORLD !"
    

    elif (nbFct == 15) : # Feature 15
        for compteur in range(len(noms)): 
                if (compteur == len(noms) - 1) and len(noms) != 1:
                    nomTmp = noms[compteur]
                    nomsfinal = nomsfinal + "and " + nomTmp
                    nomTmp = ""
                else:
                    if len(noms) == 1:
                        nomTmp = noms[compteur]
                        nomsfinal = nomsfinal  + nomTmp
                        nomTmp = ""
                    else:
                        nomTmp = noms[compteur]
                        nomsfinal = nomsfinal  + nomTmp +  ", "
                        nomTmp = ""


    elif (nbFct == 16) : # Feature 16
        for compteur in range(len(noms)):
                if compteur != len(noms) -1 :
                    nomTmp = noms[compteur]
                    nomsfinal = nomsfinal + nomTmp + " & " 
                    nomTmp = ""
                else:
                    nomTmp = noms[compteur]
                    nomsfinal = nomsfinal  + nomTmp
                    nomTmp = ""
                
    return nomsfinal


################################################## FEATURE 1 ##############################################################################################################################################################################

def sortie_nom(nom): 

    nom = nom.lower()  # Met le nom en majuscule
    nom = nom.capitalize()  # 1ere lettre du nom en majuscule
    return "Hello, " + nom

################################################## FEATURE 2 ##############################################################################################################################################################################

def entree_nulle(nom): 

    compteur = 0
    nul = 0
    if len(nom) == 0:
        return "Hello, my friend"
    for compteur in range(len(nom)):
        if (nom[compteur] != " "):
            nul = 1
    if nul == 1:
        return "Erreur : ce nom n'est pas nul"
    else:
        return "Hello, my friend"

################################################## FEATURE 3 ##############################################################################################################################################################################

def entree_cris(nom):

    NOM = nom.upper()
    if nom == NOM and entree_nulle(nom) != "Hello, my friend" : # On vérifie que le nom n'est pas nul.
        return "HELLO, " + nom + " !"
    else:
        return "Erreur : Ce nom n'est pas un cri"

################################################## FEATURE 4 ##############################################################################################################################################################################

def entree_deux_noms(noms): 

    liste_noms = []
    liste_noms = no_space(noms)
    liste_noms = capitalize(liste_noms)
    return "Hello" + affichage(liste_noms,1)

################################################## FEATURE 5 ##############################################################################################################################################################################

def entree_plusieurs_noms(noms): 
    
    liste_noms = []
    liste_noms = no_space(noms)
    liste_noms = capitalize(liste_noms)
    return "Hello" + affichage(liste_noms, 1)

################################################## FEATURE 6 ##############################################################################################################################################################################

def gestion_des_cris(noms):

    liste_noms = []
    liste_noms_maj = []
    liste_noms = no_space(noms)
    
    compteur = 0
    while compteur < len(liste_noms):
        if liste_noms[compteur].upper() == liste_noms[compteur] and entree_nulle(liste_noms[compteur]) != "Hello, my friend" :
            liste_noms_maj.append(liste_noms[compteur])
            del liste_noms[compteur]
        else :
            compteur = compteur + 1
    if entree_nulle(liste_noms[compteur-1]) != "Hello, my friend":
        liste_noms = capitalize(liste_noms)
    if len(liste_noms_maj) == 0:
        return "Erreur : il n'y a pas de cri"
    return "Hello" + affichage(liste_noms,1) + ". AND HELLO" + affichage(liste_noms_maj,1) + " !"

################################################## FEATURE 7 ##############################################################################################################################################################################

def gestion_et(noms): 
    liste_noms = []
    liste_noms = no_space(noms)
    liste_noms = capitalize(liste_noms)
    return "Hello" + affichage(liste_noms, 2) 

##################################### Feature 8 (voir tout en haut dans "FONCTIONS OUTILS") ################################################################################################################################################


################################################## FEATURE 9 ##############################################################################################################################################################################

def point_exclamation(liste_noms): 
    liste_noms = creation_delete(liste_noms)  # (voir tout en haut dans "FONCTIONS OUTILS" pour la fonction "creation_delete")
    if len(liste_noms) == 1:
        return "Hello" + affichage(capitalize(liste_noms), 1)
    else:
        return "Hello" + affichage(capitalize(liste_noms), 2)

################################################## FEATURE 10 ##############################################################################################################################################################################

def multiple_name(noms,affich): 
    if affich == True : # Si affich = True, alors on produit la "Feature 10" (EX : entrée : ("bob,bob,amy,jerry,!jerry",True ) sortie : ("Hello, Bob (x2) and Amy")) , si affich = False, alors on renvoie la liste de nom avec le prénom et le nombre d'occurence du prénom, (EX : entrée : (['Bob','Bob','Jerry','Jerry'],False)  sortie : (['Bob',2,'Jerry',2]) )                            
        noms=creation_delete(noms)
    noms_occ=[noms[0],1] 
    fin_boucle = 0
    compteur1 = 1
    compteur2 = 0
    while compteur1 < len(noms):

        while compteur2 < len(noms_occ) and fin_boucle == 0:

            if noms_occ[compteur2] == noms[compteur1]:
                noms_occ[compteur2+1] = noms_occ[compteur2+1]+1
                fin_boucle = 1
            else :
                compteur2 = compteur2 + 2

        if compteur2 >= len(noms_occ):
            noms_occ.append(noms[compteur1])
            noms_occ.append(1) 

        compteur2 = 0
        compteur1 = compteur1 + 1
        fin_boucle = 0

    noms_occ = capitalize(noms_occ)

    if affich == True:
        return "Hello" + affichage(noms_occ,10)
    else :
        return noms_occ

################################################## FEATURE 11/12 ##############################################################################################################################################################################

def noms_differents(liste_noms): # Cette fonction permet de connaitre le nombre de prénom different dans une liste. La fonction prend une liste de noms en paramètres (EX : entrée : ['Bob','Jerry','Amy','Jerry']   sortie : 3)
    if len(liste_noms) == 0:
        return "Erreur : la liste de noms est vide"
    liste_noms = multiple_name(liste_noms, False)
    return len(liste_noms) // 2


def nombre_noms_maj(noms):#prend une chaine de caractère en paramètre
    compteurNomMaj=0
    liste_noms = creation_delete(noms)
    for noms in liste_noms:
        if noms == noms.upper():
            compteurNomMaj += 1
    return compteurNomMaj

def gestion_plus_de_cinq_noms(noms):#prend une chaine de caractère en paramètre
    liste_noms = creation_delete(noms)
    if noms_differents(liste_noms) > 5 and nombre_noms_maj(noms) > 5:
        return affichage(liste_noms, 12)
    elif noms_differents(liste_noms) > 5:
        return affichage(liste_noms, 11)
    else:
        return 1

################################################## FEATURE 13/14 ##############################################################################################################################################################################

def gestion_yoda(noms):

    liste_noms = []
    liste_noms = creation_delete(noms)
    liste_noms = capitalize(liste_noms)
    presence_Yoda = 0

    for element in range(len(liste_noms)):
        if liste_noms[element] == "Yoda":
            presence_Yoda = 1

    if presence_Yoda == 1 and noms_differents(liste_noms) >= 5:
        return "World, Hello"

    elif presence_Yoda == 1:
        return affichage(liste_noms, 3) + ", Hello"

    else:
        return "Erreur, Yoda n'est pas là !"

################################################## FEATURE 15 ##############################################################################################################################################################################

def gestion_guest(noms): #La fonction place tous les prénoms contenu dans "liste_noms", après le prénom entouré d'"*" dans "liste_etoile". 
    
    liste_noms = []
    liste_etoile = []
    liste_noms = creation_delete(noms)
    compteur = 0
    fin_boucle = 0
    
    while compteur < len(liste_noms) and fin_boucle == 0:
        if liste_noms[compteur] [0] == "*" and liste_noms[compteur] [len(liste_noms[compteur]) - 1] == "*":
            liste_etoile.append(liste_noms[compteur])
            del liste_noms[compteur]
            fin_boucle = 1 
        else :
            compteur = compteur + 1
    liste_etoile[0] =  liste_etoile[0].replace('*','')

    while compteur < len(liste_noms):
        liste_etoile.append(liste_noms[compteur])
        del liste_noms[compteur]
    liste_etoile = capitalize(liste_etoile)
    liste_noms = capitalize(liste_noms)
    
    return "Hello" + affichage(liste_noms,2)  + " our special guest " + affichage(liste_etoile,15)

################################################## FEATURE 16 ##############################################################################################################################################################################

def gestion_guest_feature16(noms):  # Presque même principe que le feature précedente sauf que cette fois ci on stock les prénoms avec "*" dans "liste_etoile" et les prénoms normaux situé après les *prenom* dans "liste_apres_etoile"
    liste_noms = []
    liste_etoile = []
    liste_apres_etoile = []

    liste_noms = creation_delete(noms)
    compteur = 0
    fin_boucle = 0
    
    while compteur < len(liste_noms) :
        if liste_noms[compteur] [0] == "*" and liste_noms[compteur] [len(liste_noms[compteur]) - 1] == "*":
            liste_etoile.append(liste_noms[compteur])
            del liste_noms[compteur]
            fin_boucle = 1 

        elif fin_boucle == 1:
            liste_apres_etoile.append(liste_noms[compteur])
            del liste_noms[compteur]
        else :
            compteur= compteur + 1 

    for compteur in range(len(liste_etoile)):
        liste_etoile[compteur] =  liste_etoile[compteur].replace('*','')
    
    liste_etoile = capitalize(liste_etoile)
    liste_noms = capitalize(liste_noms)
    liste_apres_etoile = capitalize(liste_apres_etoile)

    if len(liste_etoile) > 1 :
        return "Hello," + affichage(liste_noms,2) + " our special guests " + affichage(liste_etoile,16) +", "+ affichage(liste_apres_etoile,3)
    else :
        return "Erreur : Il n'ya qu'un seul guest"

################################################## FEATURE 17 ##############################################################################################################################################################################

def autoriser_les_virgules(noms):
    liste_noms = no_space(noms)
    liste_noms = capitalize(liste_noms)
    print("base liste_noms = ",liste_noms)
    i = 0
    fin = 0

    while i < len(liste_noms) and fin == 0:
        if liste_noms[i][0] == '"'  and len(liste_noms[i+1:]) > 0:

            while liste_noms [i+1] [len(liste_noms [i+1])-1] != '"':
                liste_noms[i] = liste_noms[i] + ", " + liste_noms[i+1]
                del liste_noms[i+1]
            liste_noms[i] = liste_noms[i] + ", " + liste_noms[i+1]
            del liste_noms[i+1]
            liste_noms[i] = liste_noms[i].replace('"','')
            fin = 1

        elif liste_noms[i][0] == '"' and liste_noms[i][len(liste_noms[i])-1] == '"': #pour le cas ou on a en entré ce cas: \"Amy\" (= un seul parmetre entre slash : voir assert 3 "Feature 17")
            liste_noms[i] = liste_noms[i].replace('"','')
          
        else :
            i = i + 1
    return "Hello" + affichage(liste_noms,2)

