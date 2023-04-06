from likeprocessing.processing import *

rectMode("center")
ellipseMode("center")

def morpion():
    global x,y,taillecase
    plateau=[["","",""],["","",""],["","",""]]
    for i in range(4):
        jouer=0
        while jouer!=1:
            print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
            print("Au joueur 1 de jouer.")
            v = y,x
            if plateau[int(v[0])][int(v[1])] =="":
                plateau[int(v[0])][int(v[1])] = 1
                jouer=1
                fill("blue")
                rect((x+1)*taillecase//2,(y+1)*taillecase//2,80,80)
            else:
                print("Cette case est déja prise")
        for j in range(len(plateau)):
            if plateau[j][0]==1 and plateau[j][1]==1 and plateau[j][2]==1:
                print("joueur 1 à gagné")
                return None
            if plateau[0][j] == 1 and plateau[1][j] == 1 and plateau[2][j] == 1:
                print("joueur 1 à gagné")
                return None
        if plateau[0][0]==1 and plateau[1][1]==1 and plateau[2][2]==1:
            print("joueur 1 à gagné")
            return None
        if plateau[2][0]==1 and plateau[1][1]==1 and plateau[0][2]==1:
            print("joueur 1 à gagné")
            return None
        jouer=0
        while jouer != 1:
            print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
            print("Au joueur 2 de jouer")
            v = x,y
            if plateau[int(v[0])][int(v[1])]=="":
                plateau[int(v[0])][int(v[1])] = 2
                jouer=1
                fill("red")
                circle((x+1)*taillecase//2,(y+1)*taillecase//2,80)
            else:
                print("Cette case est déja prise")
        for j in range(len(plateau)):
            if plateau[j][0] == 2 and plateau[j][1] == 2 and plateau[j][2] == 2 or plateau[0][j] == 2 and plateau[1][j] == 2 and plateau[2][j] == 2:
                print("joueur 2 à gagné")
                return None
        if plateau[0][0] == 2 and plateau[1][1] == 2 and plateau[2][2] == 2 or plateau[2][0] == 2 and plateau[1][1] == 2 and plateau[0][2] == 2:
            print("joueur 2 à gagné")
            return None
    jouer = 0
    while jouer != 1:
        print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
        print("Au joueur 1 de jouer.")
        v = x,y
        if plateau[int(v[0])][int(v[1])] == "":
            plateau[int(v[0])][int(v[1])] = 1
            jouer = 1
            fill("blue")
            rect((x + 1) * taillecase // 2, (y + 1) * taillecase // 2, 80, 80)
        else:
            print("Cette case est déja prise")
    for j in range(len(plateau)):
        if plateau[j][0] == 1 and plateau[j][1] == 1 and plateau[j][2] == 1:
            print("joueur 1 à gagné")
            return None
        if plateau[0][j] == 1 and plateau[1][j] == 1 and plateau[2][j] == 1:
            print("joueur 1 à gagné")
            return None
    if plateau[0][0] == 1 and plateau[1][1] == 1 and plateau[2][2] == 1:
        print("joueur 1 à gagné")
        return None
    if plateau[2][0] == 1 and plateau[1][1] == 1 and plateau[0][2] == 1:
        print("joueur 1 à gagné")
        return None
    print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
    print("Egalité")

morpion()

taillecase=100

def setup():
    createCanvas(taillecase*3,taillecase*3)
    background("grey")

def compute():
    if mouse_button_pressed() == 0:
        y, x = ((mouseY() // taillecase), (mouseX() // taillecase))
        morpion()

def draw():
    pass

run(globals())