from likeprocessing.processing import *
from snake import Snake

jeux=['Morpion','Puissance 4','Snake','Démineur','Casse-tête','Pendu','Memory','Sudoku']
img = [loadImage('img/Morpion.jpg'),loadImage('img/Puissance4.jpg'),loadImage('img/Snake.jpg'),loadImage('img/Démineur.jpg'),loadImage('img/Casse_tete.jpg'),loadImage('img/Pendu.jpg'),loadImage('img/Memory.jpg'),loadImage('img/Sudoku.jpg')]
fond = loadImage('img/logo.png')
boite = loadImage('img/boite.jpg')
index_jeu = 0
jeu_en_cours = False
def click(name):
    global index_jeu
    if name==2:
        index_jeu = 2
        Snake.init_snake()


def setup():
    createCanvas(1200, 600)
    background('white')
def compute():
    global jeu_en_cours
    if index_jeu==2:
        Snake.compute()
        jeu_en_cours = True
def draw():
    x = 25
    y = 60
    l = 300
    h = 50
    #affichage image

    rect(0,0,350,600,fill="black")
    #text('', 400, 25, 730, 550, allign_h="center",allign_v="center")
    rect(516,46,533,98,fill="black")

    #bouton de gauche
    for i in range(len(jeux)):
        textFont('Comic sans ms',35)
        text(jeux[i],x,i*(h+10)+60,l,h,allign_h="center",allign_v="center",fill="orange",padx=5,fill_mouse_on=(255,0,0),command=click,name=i)
    # affichage image jeux
    if not jeu_en_cours:
        for i in range(len(jeux)):
            if mouseX()>x and mouseX()<x+l and mouseY()>i*(h+10)+60 and mouseY()<60+i*(h+10)+h:
                rect(397, 21, 738, 558,fill="black")
                image(img[i], 401, 26)
                break
            else:
                image(boite,533,200)
                image(fond,520,50)

    if index_jeu ==2:

        Snake.draw()


run(globals())