from likeprocessing.processing import *
taillecase = 50
nb_case_hauteur = 5
nb_case_largeur = 5
plateau = [[i*nb_case_largeur+j+1 for j in range(nb_case_largeur)] for i in range(nb_case_hauteur)]
plateau[-1][-1]=0


def setup():
    createCanvas(taillecase*nb_case_largeur, taillecase*nb_case_hauteur)
    background("grey")
    textAlign("center", "center")
    textFont("arial", 20)
    melange()

def move(case:tuple):
    global plateau,nb_case_largeur,nb_case_hauteur
    i,j=case
    if i+1 <= nb_case_hauteur-1 and plateau[i+1][j] == 0:
        plateau[i][j],plateau[i+1][j]=plateau[i+1][j],plateau[i][j]
        print("la case s'est déplacé en bas")
    elif i-1 >= 0 and plateau[i-1][j] == 0:
        plateau[i][j], plateau[i-1][j]= plateau[i-1][j], plateau[i][j]
        print("la case s'est déplacé en haut")
    elif j+1 <= nb_case_largeur-1 and plateau[i][j+1] == 0:
        plateau[i][j], plateau[i][j+1] = plateau[i][j+1],plateau[i][j]
        print("la case s'est déplacé à droite")
    elif j-1 >= 0 and plateau[i][j-1] == 0:
        plateau[i][j],plateau[i][j-1]=plateau[i][j-1],plateau[i][j]
        print("la case s'est déplacé à gauche")
    else:
        return False
    return True

def gagne():
    for i in range(nb_case_hauteur):
        for j in range(nb_case_largeur):
            if plateau[i][j]!=0 and plateau[i][j] != i*nb_case_largeur+j+i:
                return False
    return True


def melange():
    global plateau
    c=0
    while c<100:
        i,j = randint(0,nb_case_hauteur-1), randint(0,nb_case_largeur-1)
        print(i,j)
        if move((i,j)):
            c+=1


def compute():
    if mouse_button_pressed() == 0:
        i, j = ((mouseY() // taillecase), (mouseX() // taillecase))
        move((i, j))

def draw():
    for j in range(nb_case_largeur):
        for i in range(nb_case_hauteur):
            if plateau[j][i] != 0:
                text(str(plateau[j][i]), taillecase * i, taillecase * j, taillecase, taillecase)

run(globals())
