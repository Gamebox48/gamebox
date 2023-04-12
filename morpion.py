from likeprocessing.processing import *
textAlign("center")
textFont("Comic sans ms",30)
ihm = IhmScreen()

plateau = [["", "", ""], ["", "", ""], ["", "", ""]]


def recherche(liste):
    for i in range(3):
        for j in range(3):
            if liste[i][j] == "":
                return True
    return False



def gagne(tour):
    global plateau, gagnant
    for j in range(len(plateau)):
        if plateau[j][0] == tour and plateau[j][1] == tour and plateau[j][2] == tour or plateau[0][j] == tour \
                and plateau[1][j] == tour and plateau[2][j] == tour:
            print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
            print(f"Le joueur {tour} à gagné")
            gagnant = tour
            return True
    if plateau[0][0] == tour and plateau[1][1] == tour and plateau[2][2] == tour or plateau[2][0] == tour \
            and plateau[1][1] == tour and plateau[0][2] == tour:
        print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
        print(f"Le joueur {tour} à gagné")
        gagnant = tour
        return True
    return False


def init_jeu():
    global plateau, fini, gagnant
    plateau = [["", "", ""], ["", "", ""], ["", "", ""]]
    ihm.objet_by_name('bouton_recommencer').visible = False
    ihm.objet_by_name('bouton_menu').visible = False
    fini = 0
    gagnant = 0

def morpion(name):
    global plateau, tour
    if fini == 0:
        print(name)
        plateau[name[1]][name[0]] = tour
        gagne(tour)
        tour = tour % 2 + 1

    # while recherche(plateau) == True and fin == False:
    #     print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
    #     bon_placement=False
    #     tour = nombre % 2 + 1
    #     while bon_placement == False:
    #         print(f'Au joueur {tour} de jouer.')
    #         while mouse_button_pressed()!=0:
    #             pass
    #         y, x = ((mouseY() // taillecase), (mouseX() // taillecase))
    #         bon_placement = peut_jouer(int(y),int(x))
    #     tour_morpion(y,x,tour)
    #     fin = gagne(tour)
    #     nombre+=1


taillecase = 100
ihm.addObjet(Bouton(ihm, (0, 350, 150, 50), 'Recommencer', command=init_jeu), 'bouton_recommencer')
ihm.objet_by_name('bouton_recommencer').visible = False
ihm.addObjet(Bouton(ihm, (150, 350, 150, 50), 'Retour au menu', command=init_jeu), 'bouton_menu', )
ihm.objet_by_name('bouton_menu').visible = False
tour = 1
gagnant = 0
fini = 0


def setup():
    createCanvas(taillecase * 3, taillecase * 4)
    background("grey")


def compute():
    ihm.scan_events()


def draw():
    global tour, gagnant, fini
    for i in range(3):
        for j in range(3):
            if tour == 1:
                couleur = "red"
                text('Au joueur 1 de jouer.', 0, 300, 300, 100)
            else:
                couleur = "blue"
                text('Au joueur 2 de jouer.', 0, 300, 300, 100)
            if plateau[j][i] == "":
                rect(taillecase * i, taillecase * j, taillecase, taillecase, fill_mouse_on=couleur, command=morpion,
                     name=(i, j))
            elif plateau[j][i] == 1:
                rect(taillecase * i, taillecase * j, taillecase, taillecase, fill="white")
                circle(10 + taillecase * i, 10 + taillecase * j, taillecase - 20, no_fill=True, stroke="red",
                       stroke_weight=5)
            else:
                rect(taillecase * i, taillecase * j, taillecase, taillecase, fill="white")
                strokeWeight(5)
                line(taillecase * i + 10, taillecase * j + 10, taillecase * (i + 1) - 10, taillecase * (j + 1) - 10,
                     stroke="blue")
                line(taillecase * (i + 1) - 10, taillecase * j + 10, taillecase * i + 10, taillecase * (j + 1) - 10,
                     stroke="blue")
                strokeWeight(1)
            if gagnant == 1:
                text('Le joueur 1 a gagné!', 0, 300, 300, 100)
                fini = 2
            elif gagnant == 2:
                text('Le joueur 2 a gagné!', 0, 300, 300, 100)
                fini = 2
            if recherche(plateau) == False and fini!=2:
                text('Match nul', 0, 300, 300, 100)
                fini = 1
    if fini != 0:
        ihm.objet_by_name('bouton_recommencer').visible = True
        ihm.objet_by_name('bouton_menu').visible = True
    ihm.draw()


run(globals())
