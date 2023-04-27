from likeprocessing.processing import *
from snake import Snake
from casse_tete_in_dialog import CasseTete
from memory.memory_file import Memory
from morpion_in_dialog import Morpion
# from sudoku.sudoku import Sudoku

jeux = ['Morpion', 'Puissance 4', 'Snake', 'Démineur', 'Casse-tête', 'Pendu', 'Memory', 'Sudoku']
img = [loadImage('img/Morpion.jpg'), loadImage('img/Puissance4.jpg'), loadImage('img/Snake.jpg'),
       loadImage('img/Démineur.jpg'), loadImage('img/Casse_tete.jpg'), loadImage('img/Pendu.jpg'),
       loadImage('img/Memory.jpg'), loadImage('img/Sudoku.jpg')]
fond = loadImage('img/logo.png')
boite = loadImage('img/boite.jpg')
index_jeu = -1
jeu_en_cours = False
index_dessin_jeu = -1
quitter_jeu_en_cours = False
ihm = IhmScreen()


def click(name):
    """Traite le click sur les boutons de menu"""
    global index_jeu, jeu_en_cours, quitter_jeu_en_cours
    if jeu_en_cours:
        if name != index_jeu:
            quitter_jeu_en_cours = True
    else:
        if name == 0:
            ihm.init()
            ihm.addObjet(Morpion(ihm, 620, 100), "morpion")
            index_jeu=0
            jeu_en_cours = True
        if name == 2:
            index_jeu = 2
            Snake.init_snake()
            jeu_en_cours = True
        elif name == 4:
            ihm.init()
            ihm.addObjet(CasseTete(ihm, 620, 100), "casse_tete")
            index_jeu = 4
            jeu_en_cours = True
        elif name == 6:
            ihm.init()
            ihm.addObjet(Memory(ihm, 375, 0), "memory")
            index_jeu = 6
            jeu_en_cours = True


def setup():
    createCanvas(1200, 600)
    background('white')
    ihm.init()


def compute():
    global jeu_en_cours, index_jeu, quitter_jeu_en_cours
    if quitter_jeu_en_cours:
        # demander si le joueur veut quitter le jeux en cours
        if AskYesNo(ihm, "Voulez-vous Vraiment\nquitter le jeu en cours").response() == 0:
            ihm.init()
            jeu_en_cours = False
            index_jeu = -2
        quitter_jeu_en_cours = False
    elif index_jeu == 0:
        if ihm.objet_by_name("morpion").destroy:
            jeu_en_cours = False
    elif index_jeu == 2:
        # calculs pour le jeu snake
        if Snake.perdu:
            if AskYesNo(ihm, "Voulez-vous\nrejouer").response() == 0:
                index_jeu = 2
                Snake.init_snake()
                jeu_en_cours = True
            else:
                jeu_en_cours = False
                index_jeu = -2
        Snake.compute()
    elif index_jeu == 4:
        # est ce la fin du jeu casse tete
        if ihm.objet_by_name("casse_tete").destroy:
            jeu_en_cours = False
    elif index_jeu == 6:
        # calculs et fin du jeu memory
        ihm.objet_by_name("memory").compute()
        if ihm.objet_by_name("memory").destroy:
            jeu_en_cours = False
    ihm.scan_events()


def draw():
    global index_dessin_jeu
    x = 25
    y = 60
    l = 300
    h = 50
    # affichage image
    index_dessin_jeu = -1

    def mouse_over(name):
        global index_dessin_jeu
        index_dessin_jeu = name

    rect(0, 0, 350, 600, fill="black")

    # bouton de gauche

    for i in range(len(jeux)):
        textFont('Comic sans ms', 35)
        text(jeux[i], x, i * (h + 10) + 60, l, h, allign_h="center", allign_v="center", fill="orange", padx=5,
             fill_mouse_on="red", command=click, name=i, command_mouse_over=mouse_over)

    # affichage image jeux
    if not jeu_en_cours:
        if index_dessin_jeu != -1:
            rect(397, 21, 738, 558, fill="black")
            image(img[index_dessin_jeu], 401, 26)
        else:
            rect(516, 46, 533, 98, fill="black")
            image(boite, 533, 200)
            image(fond, 520, 50)

    if index_jeu == 2:
        Snake.draw()
    ihm.draw()


run(globals())
