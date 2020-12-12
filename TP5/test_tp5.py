import tp5 as m

def test_sortie_nom():
    assert m.sortie_nom("bob") == "Hello, Bob"
    assert m.sortie_nom("BOB") == "Hello, Bob"
    assert m.sortie_nom("BOb") == "Hello, Bob"
    assert m.sortie_nom("b") == "Hello, B"


def test_entree_nulle():
    assert m.entree_nulle("") == "Hello, my friend"
    assert m.entree_nulle("    ") == "Hello, my friend"
    assert m.entree_nulle("b") == "Erreur : ce nom n'est pas nul"

def test_entree_cris():
    assert m.entree_cris("JERRY")=="HELLO, JERRY !"
    assert m.entree_cris("thomas")== "Erreur : Ce nom n'est pas un cri"
    assert m.entree_cris("    ")== "Erreur : Ce nom n'est pas un cri"
    assert m.entree_cris("")== "Erreur : Ce nom n'est pas un cri"

def test_entree_deux_noms():
    assert m.entree_deux_noms("Amy,bob") == "Hello, Amy, Bob"
    assert m.entree_deux_noms("Amy,BOB") == "Hello, Amy, Bob"
    assert m.entree_deux_noms("AMy,BOB") == "Hello, Amy, Bob"

def test_entree_plusieurs_noms():
    assert m.entree_plusieurs_noms("Amy,bob,Max") == "Hello, Amy, Bob, Max"
    assert m.entree_plusieurs_noms("Amy,bob,MAX") == "Hello, Amy, Bob, Max"
    assert m.entree_plusieurs_noms("Amy,bob,MAX,tomy") == "Hello, Amy, Bob, Max, Tomy"

def test_gestion_des_cris():
    assert m.gestion_des_cris("aMy,Tom,BOB") == "Hello, Amy, Tom. AND HELLO, BOB !"
    assert m.gestion_des_cris("") == "Erreur : il n'y a pas de cri"
    assert m.gestion_des_cris("aMy,Tom,Bob") == "Erreur : il n'y a pas de cri"
    assert m.gestion_des_cris("aMy,Tom,BOB,THOMAS") == "Hello, Amy, Tom. AND HELLO, BOB, THOMAS !"


def test_gestion_et():
    assert m.gestion_et("bob,amy,jerry") == "Hello, Bob, Amy and Jerry"
    assert m.gestion_et("bob      ,amy,jerry") == "Hello, Bob, Amy and Jerry"
    assert m.gestion_et("bob") == "Hello, Bob"

def test_point_exclamation():
    assert m.point_exclamation("bob,!bob,amy,bob,!jerry")=="Hello, Amy"
    assert m.point_exclamation("bob,amy,bob,!jerry")=="Hello, Bob, Amy and Bob"
    assert m.point_exclamation("!jerry")=="Hello"
    assert m.point_exclamation("bob,!jerry")=="Hello, Bob"

def test_multiple_name():
    assert m.multiple_name("bob,bob,amy,jerry,!jerry",True)=="Hello, Bob (x2) and Amy"
    assert m.multiple_name("bob,bob,amy,amy,bob,jerry,!jerry",True)=="Hello, Bob (x3) and Amy (x2)"
    assert m.multiple_name("vincent,bob,bob,amy,amy,bob,jerry,!jerry",True)=="Hello, Vincent, Bob (x3) and Amy (x2)"
    assert m.multiple_name(['Bob','Bob','Jerry','Jerry'], False)  ==  ['Bob',2,'Jerry',2]
    assert m.multiple_name(['Bob','Bob','Amy','Jerry','Jerry'], False)  ==  ['Bob',2,'Amy',1,'Jerry',2] 
    assert m.multiple_name(['Jerry','Amy','Bob','Jerry','Jerry'], False)  ==  ['Jerry',3,'Amy',1,'Bob',1] 

def test_gestion_yoda():
    assert m.gestion_yoda("bob,yoda,amy") == "Bob, Yoda, and Amy, Hello"
    assert m.gestion_yoda("bob,yoda,amy,!yoda") == "Erreur, Yoda n'est pas là !"
    assert m.gestion_yoda("bob,yoda,amy,thomas,valerie,anakin") == "World, Hello"
    assert m.gestion_yoda("bob,amy,thomas,valerie,anakin") == "Erreur, Yoda n'est pas là !"
    assert m.gestion_yoda("bob,yoda,thomas,valerie,anakin") == "World, Hello"


def test_noms_differents():
    assert m.noms_differents(["bob","amy"]) == 2
    assert m.noms_differents([]) == "Erreur : la liste de noms est vide"
    assert m.noms_differents(["bob","amy","amy"]) == 2
    

def test_gestion_plus_de_cinq_noms():
    assert m.gestion_plus_de_cinq_noms("bob,yoda,amy,thomas,valerie,anakin") == "Hello, world !"
    assert m.gestion_plus_de_cinq_noms("bob,yoda,amy,thomas,valerie") == 1
    assert m.gestion_plus_de_cinq_noms("bob,yoda,amy,thomas,valerie,!anakin") == 1
    assert m.gestion_plus_de_cinq_noms("BOB,YODA,AMY,THOMAS,VALERIE,ANAKIN") == "HELLO, WORLD !"
    assert m.gestion_plus_de_cinq_noms("BOB,YODA,AMY,THOMAS,VALERIE") == 1
    assert m.gestion_plus_de_cinq_noms("BOB,YODA,AMY,THOMAS,VALERIE,!ANAKIN") == 1

def test_nombre_noms_maj():
    assert m.nombre_noms_maj("bob, yoda,amy,thomas,valerie,anakin") == 0
    assert m.nombre_noms_maj("BOB, Yoda,AMY,thOmas,!valerie,!ANAKIN") == 2

def test_gestion_guest():
    assert m.gestion_guest("bob, *amy*, jerry") == "Hello, Bob our special guest Amy, and Jerry"
    assert m.gestion_guest("bob,*amy*,jerry,thomas") == "Hello, Bob our special guest Amy, Jerry, and Thomas"
    assert m.gestion_guest("bob,*amy*") == "Hello, Bob our special guest Amy"
    assert m.gestion_guest("bob,bob,*amy*") == "Hello, Bob and Bob our special guest Amy"
    assert m.gestion_guest("thomas,bob,bob,*amy*") == "Hello, Thomas, Bob and Bob our special guest Amy"

def test_gestion_guest_feature16():
    assert m.gestion_guest_feature16("*bob*, *amy*, jerry") == "Hello, our special guests Bob & Amy, and Jerry"
    assert m.gestion_guest_feature16("*bob*, *amy*,*toto*, jerry") == "Hello, our special guests Bob & Amy & Toto, and Jerry"
    assert m.gestion_guest_feature16("*bob*, *amy*,*toto*, jerry,fifi") == "Hello, our special guests Bob & Amy & Toto, Jerry, and Fifi"
    assert m.gestion_guest_feature16("*bob*, jerry") == "Erreur : Il n'ya qu'un seul guest"

def test_autoriser_les_virgules():
    assert m.autoriser_les_virgules("Bob, vanessa , \"Amy, toto, Jerry\"") == "Hello, Bob, Vanessa and Amy, Toto, Jerry"
    assert m.autoriser_les_virgules("Bob, \"Amy,Jerry\"") ==  "Hello, Bob and Amy, Jerry"
    assert m.autoriser_les_virgules("Bob, \"Amy\"") ==  "Hello, Bob and Amy"
    assert m.autoriser_les_virgules("\"Amy, toto, Jerry\", Bob, vanessa ") == "Hello, Amy, Toto, Jerry, Bob and Vanessa"

################################# TEST FONCTIONS OUTILS ##############################################

def test_capitalize():
    assert m.capitalize(['bOb','AMY','jerry','thOMas']) == ['Bob','Amy','Jerry','Thomas']
    assert m.capitalize([]) == []

def test_no_space():
    assert m.no_space("bob      ,amy,jerry") == ['bob','amy','jerry']
    assert m.no_space("bob      ,  amy, jerry   ") == ['bob','amy','jerry']
    assert m.no_space("bob,amy,jerry") == ['bob','amy','jerry']

def test_creation_delete():
    assert m.creation_delete("!jerry,bob,amy,thomas,!thomas") == ['bob','amy']
    assert m.creation_delete("!jerry,!bob,!amy,thomas,!thomas") == []
    assert m.creation_delete("!thomas") == []
