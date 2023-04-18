from likeprocessing.processing import *

jeux=['Morpion','Puissance 4','Snake','Démineur','Casse-tête','Pendu','Memory','Sudoku']
img = [loadImage('Morpion.jpg'),loadImage('Puissance4.jpg'),loadImage('Snake.jpg'),loadImage('Démineur.jpg'),loadImage('Solitaire.jpg'),loadImage('Pendu.jpg'),loadImage('Memory.jpg'),loadImage('Dame.jpg')]
fond = loadImage('logo.png')
boite = loadImage('boite.jpg')

def click(name):
    print(name)


def setup():
    createCanvas(1200, 600)
    background('white')

def draw():
    x = 25
    y = 60
    l = 300
    h = 50
    image(boite,533,200)
    fill('black')
    rect(0,0,350,600)
    #text('', 400, 25, 730, 550, allign_h="center",allign_v="center")
    fill('black')
    rect(516,46,533,98)
    image(fond,520,50)
    for i in range(len(jeux)):
        fill('red')
        rect(x-3,y-3,l+6,h+6)
        if mouseX()>x and mouseX()<x+l and mouseY()>y and mouseY()<y+h:
            fill('black')
            rect(397, 21, 738, 558)
            image(img[i], 401, 26)
            fill('red')
        else:
            fill('orange')
        rect(x,y,l,h,command=click,name=jeux[i])
        textFont('Comic sans ms',35)
        text(jeux[i],x,y,l,h,allign_h="center",allign_v="center")
        y += h + 10


run(globals())