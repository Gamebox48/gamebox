from likeprocessing.processing import *

plateau = [["", "", ""], ["", "", ""], ["", "", ""]]


def recherche(liste):
    for i in range(3):
        for j in range(3):
            if liste[i][j] == "":
                return True
    return False


def tour_morpion(y, x, tour):
    global plateau
    plateau[int(y)][int(x)] = tour
    if tour == 1:
        fill("red")
        rect(20+taillecase*x,20+taillecase*y,taillecase-20,taillecase-20)
    else:
        fill("blue")
        circle(20+taillecase*x,20+taillecase*y,taillecase-20)


def gagne(tour):
    global plateau, tour
    for j in range(len(plateau)):
        if plateau[j][0] == tour and plateau[j][1] == tour and plateau[j][2] == tour or plateau[0][j] == tour \
                and plateau[1][j] == tour and plateau[2][j] == tour:
            print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
            print(f"Le joueur {tour} à gagné")
            gagnant=tour
            return True
    if plateau[0][0] == tour and plateau[1][1] == tour and plateau[2][2] == tour or plateau[2][0] == tour \
            and plateau[1][1] == tour and plateau[0][2] == tour:
        print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
        print(f"Le joueur {tour} à gagné")
        return True
    return False

def peut_jouer(y,x):
    global taillecase, plateau
    if y<0 or y>2 or x<0 or x>2:
        return False
    if plateau[int(y)][int(x)] == "":
        return True
    else:
        print("Cette case est déja prise")
        return False

def morpion(name):
    global plateau, tour
    nombre=0
    fin = False
    print(name)
    plateau[name[0]][name[1]]=tour
    gagne(tour)
    tour = tour%2 +1

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

taillecase=100

tour=1

def setup():
    createCanvas(taillecase*3,taillecase*4)
    background("grey")

def compute():
    pass

def draw():
    global tour
    for i in range(3):
        for j in range(3):
            if tour == 1:
                couleur = "red"
            else:
                couleur = "blue"
            if plateau[i][j] =="":
                rect(taillecase*i,taillecase*j,taillecase,taillecase,fill_mouse_on=couleur,command = morpion, name = (i,j))
            elif plateau[i][j] == 1:
                rect(taillecase * i, taillecase * j, taillecase, taillecase,fill = "white")
                circle(10+taillecase * i, 10+taillecase * j, taillecase - 20, no_fill=True, stroke="red", stroke_weight=5)
            else:
                rect(taillecase * i, taillecase * j, taillecase, taillecase,fill = "white")
                strokeWeight(5)
                line(taillecase*i+10,taillecase*j+10,taillecase*(i+1)-10,taillecase*(j+1)-10, stroke="blue")
                line(taillecase * (i+1)-10, taillecase * j+10, taillecase * i+10, taillecase * (j + 1)-10, stroke="blue")
                strokeWeight(1)


run(globals())