from likeprocessing.processing import *
from pendu import *

ihm = IhmScreen()

def draw_pendu(nb_essai):
    pendu = [(100, 430, 700, 430),
             (200, 430, 200, 50),
             (200, 50, 450, 50),
            (200, 140, 300, 50),
            (450, 50, 450, 130),
            (450, 130, 85),
            (450, 172, 450, 300),
            (450, 300, 515, 380),
            (450, 300, 385, 380),
            (450, 200, 515, 250),
            (450, 200, 385, 250)]
    for i in range(nb_essai):
        if i !=5:
            line(*pendu[i])
        else:
            circle(*pendu[5])

def creation_interface():
    touches = ["AZERTYUIOP","QSDFGHJKLM","WXCVBN"]
    for i in range(len(touches)):
        for j in range(len(touches[i])):
            ihm.addObjet(Bouton(ihm, (200 + i * 20 + 40 * j, 450 + i * 40, 40, 40), touches[i][j]))



def setup():
    createCanvas(800,600)
    background('white')
    ihm.init()
    creation_interface()
    textAlign("right", "center")
    ellipseMode('Center')
    strokeWeight(3)

def compute():
    ihm.scan_events()

def draw():
    title(str(mouseXY()))
    ihm.draw()
    draw_pendu(11)







run(globals())