from likeprocessing.processing import *
taillecase = 50
nb_case_hauteur = 5
nb_case_largeur = 5
plateau = [[i*nb_case_largeur+j+1 for j in range(nb_case_largeur)] for i in range(nb_case_hauteur)]
plateau[-1][-1]=0


def setup():
    createCanvas(taillecase*nb_case_largeur, taillecase*(nb_case_hauteur+2))
    background("grey")
    textAlign("center", "center")
    textFont("arial", 20)
    melange()

def move(case:tuple):
    global plateau,nb_case_largeur,nb_case_hauteur
    i,j=case
    if i > nb_case_hauteur or j >nb_case_largeur or i > nb_case_largeur or j > nb_case_hauteur:
        return False
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
    global fini
    for i in range(nb_case_hauteur):
        for j in range(nb_case_largeur):
            if plateau[i][j]!=0 and plateau[i][j] != i*nb_case_largeur+j+i:
                return False
    fini=2
    ihm.objet_by_name('bouton_recommencer_fin').visible = True
    ihm.objet_by_name('bouton_menu_fin').visible = True
    return True


def melange():
    global plateau
    c=0
    while c<100:
        i,j = randint(0,nb_case_hauteur-1), randint(0,nb_case_largeur-1)
        print(i,j)
        if move((i,j)):
            c+=1

def pause():
    global fini
    ihm.objet_by_name('bouton_pause').visible = False
    ihm.objet_by_name('bouton_reprendre').visible=True
    ihm.objet_by_name('bouton_recommencer_pause').visible = True
    ihm.objet_by_name('bouton_menu_pause').visible = True
    fini=1

def reprendre():
    global fini
    ihm.objet_by_name('bouton_pause').visible = True
    ihm.objet_by_name('bouton_reprendre').visible=False
    ihm.objet_by_name('bouton_recommencer_pause').visible = False
    ihm.objet_by_name('bouton_menu_pause').visible = False
    fini=0

ihm.addObjet(Bouton(ihm, (75, 250, 100, 100), '||', command=pause), 'bouton_pause')
ihm.addObjet(Bouton(ihm, (250//2, 350, 150, 50), '||', command=reprendre), 'bouton_reprendre')
ihm.objet_by_name('bouton_reprendre').visible = False
ihm.addObjet(Bouton(ihm, (0, 350, 150, 50), 'Recommencer', command=reprendre), 'bouton_recommencer_pause')
ihm.objet_by_name('bouton_recommencer_pause').visible = False
ihm.addObjet(Bouton(ihm, (0, 350, 150, 50), 'Retour au menu', command=reprendre), 'bouton_menu_pause')
ihm.objet_by_name('bouton_menu_pause').visible = False
ihm.addObjet(Bouton(ihm, (0, 350, 150, 50), 'Recommencer', command=reprendre), 'bouton_recommencer_fin')
ihm.objet_by_name('bouton_recommencer_fin').visible = False
ihm.addObjet(Bouton(ihm, (0, 350, 150, 50), 'Retour au menu', command=reprendre), 'bouton_menu_fin')
ihm.objet_by_name('bouton_menu_fin').visible = False

fini=0

def compute():
    if mouse_button_pressed() == 0:
        i, j = ((mouseY() // taillecase), (mouseX() // taillecase))
        if i <= nb_case_largeur-1 and j <= nb_case_hauteur-1:
            move((i, j))

def draw():
    for j in range(nb_case_largeur):
        for i in range(nb_case_hauteur):
            if plateau[j][i] != 0:
                text(str(plateau[j][i]), taillecase * i, taillecase * j, taillecase, taillecase)
    draw_

run(globals())
