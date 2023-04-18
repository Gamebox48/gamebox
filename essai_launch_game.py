"""programme de base"""
from likeprocessing.processing import *
from snake import Snake
ihm = IhmScreen()

def compute_jeu():
    pass

def draw_jeu():
    pass

def demarrer(name):
    global compute_jeu, draw_jeu
    if name =="snake":
        Snake.init_snake()
        compute_jeu = Snake.compute
        draw_jeu = Snake.draw


def setup():
    createCanvas(800, 600)
    background("grey")
    ihm.addObjet(Bouton(ihm,(10,10,13,20),"Snake",command=demarrer, name="snake"),"snake")

def compute():
    ihm.scan_events()
    compute_jeu()


def draw():
    ihm.draw()
    draw_jeu()


run(globals())