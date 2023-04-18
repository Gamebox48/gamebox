"""programme de base"""
from likeprocessing.processing import *
from random import shuffle

def init_nourriture(n=10)->list:
    posx = [i for i in range(10, 400, 10)]
    shuffle(posx)
    posy = [i for i in range(10, 400, 10)]
    shuffle(posy)
    return [(posx[i], posy[i]) for i in range(n)]

x, y = 100, 100
vitesse_x = 10
vitesse_y = 0
tempo = Tempo(100)
serpent = [(x - 10 * i, y) for i in range(1)]
perdu = False
nourriture = init_nourriture(39)

def setup():
    createCanvas(400, 400)
    background("grey")
    rectMode("center")
    ellipseMode("center")


def compute():
    global x, y, vitesse_x, vitesse_y, serpent, perdu,nourriture
    if tempo.fin() and perdu == False:
        x += vitesse_x
        y += vitesse_y
        if (x, y) in serpent[:-1]:
            perdu = True
        elif (x,y) in nourriture:
            serpent = [(x, y)] + serpent
            nourriture.remove((x,y))
            if len(nourriture)==0:
                nourriture = init_nourriture()
        else:
            serpent = [(x, y)] + serpent[:-1]
        if vitesse_x != 0:
            if x >= width():
                x = 0
            elif x <= -10:
                x = width()
        else:
            if y >= height():
                y = 0
            elif y <= -10:
                y = height()

    if keyIsPressed():
        if keyIsDown(K_RIGHT):
            vitesse_x = 10
            vitesse_y = 0
        elif keyIsDown(K_LEFT):
            vitesse_x = -10
            vitesse_y = 0
        elif keyIsDown(K_DOWN):
            vitesse_y = 10
            vitesse_x = 0
        elif keyIsDown(K_UP):
            vitesse_y = -10
            vitesse_x = 0


def draw():
    for i in range(len(nourriture)):
        circle(nourriture[i][0], nourriture[i][1],10,fill="green")
    for i in range(len(serpent)):
        rect(serpent[i][0], serpent[i][1], 10, 10, fill="red")
    if perdu:
        text("Tu as perdu", 200, 200, 400, 50, font_size=50, align_h="center", no_fill=True, no_stroke=True)


run(globals())
