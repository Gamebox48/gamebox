from likeprocessing.processing import *
from copy import deepcopy
from time import sleep


taillecase = 30
textFont("Comic sans ms", 20)
ihm = IhmScreen()

facile_1=[[0,6,0,4,2,0,0,0,1],[1,9,0,0,8,3,0,2,0],[0,0,2,0,1,0,7,0,0],
          [0,0,0,8,7,0,5,0,0],[0,5,1,3,4,9,0,0,2],[4,0,3,0,5,0,0,8,0],
          [6,0,5,1,3,2,0,0,0],[7,0,4,0,0,8,0,1,0],[0,1,0,0,6,0,8,5,0]]

facile_2=[[0,7,3,2,5,0,8,9,0],[8,0,1,0,0,9,0,0,0],[9,0,0,8,0,0,0,4,0],
          [0,1,9,0,6,4,5,0,8],[0,0,0,1,0,0,0,7,9],[0,3,4,0,0,8,0,6,0],
          [0,6,8,4,2,0,0,1,0],[0,4,0,0,1,0,6,8,7],[1,0,0,0,0,0,0,5,4]]

facile_3=[[0,7,0,0,0,5,0,0,0],[1,0,0,0,3,0,5,0,8],[0,0,0,2,0,9,0,6,0],
          [9,1,0,5,0,0,4,2,0],[6,8,0,3,0,0,0,1,0],[2,5,4,0,9,0,0,0,3],
          [7,0,6,8,0,1,0,4,0],[3,4,5,0,0,6,0,7,1],[0,0,1,0,7,0,2,0,6]]

moyen_1=[[0,0,9,0,0,1,6,7,0],[6,4,0,8,0,0,0,9,2],[0,0,0,9,0,0,3,0,0],
         [0,0,0,4,0,7,5,0,6],[0,5,6,0,0,0,4,3,0],[4,0,1,6,0,0,0,0,0],
         [5,6,7,0,0,0,9,8,1],[0,1,0,0,8,9,0,0,0],[0,9,0,0,0,0,0,0,0]]

moyen_2=[[6,0,0,5,3,1,9,0,0],[0,0,0,0,0,0,0,0,7],[5,4,9,0,0,0,0,0,0],
         [2,0,0,7,0,0,0,0,0],[0,0,7,0,9,0,0,3,2],[0,9,0,0,1,8,0,4,5],
         [0,2,0,0,7,4,5,0,1],[4,0,0,9,0,0,3,0,0],[0,0,3,0,0,0,0,2,0]]

moyen_3=[[0,0,0,3,2,4,7,8,5],[0,8,5,0,7,0,0,0,0],[0,0,0,0,5,0,0,0,0],
         [8,0,0,0,6,2,9,5,0],[0,0,7,5,0,0,0,3,2],[5,0,0,0,0,0,0,0,1],
         [6,0,3,0,0,0,2,0,4],[0,0,0,2,4,0,0,1,6],[2,0,0,7,0,6,0,0,0]]

difficile_1=[[0,0,0,4,0,0,5,0,6],[0,0,0,0,0,0,4,3,0],[0,6,0,5,0,0,0,1,0],
             [0,0,3,0,5,0,0,9,0],[4,0,7,0,0,0,8,0,0],[9,0,0,0,8,7,2,0,0],
             [0,7,1,0,0,5,0,0,0],[0,0,0,0,0,6,0,0,0],[0,5,0,0,0,1,0,0,4]]

difficile_2=[[0,4,0,2,0,0,0,8,0],[2,0,0,0,7,0,0,3,0],[1,0,7,0,0,0,0,0,0],
             [0,2,0,0,0,6,3,0,0],[0,0,0,0,0,0,0,0,0],[0,5,0,4,0,0,0,9,0],
             [0,3,0,9,0,0,5,0,0],[0,0,0,7,0,0,1,0,0],[0,1,5,0,4,0,6,0,0]]

difficile_3=[[8,0,0,0,0,5,0,2,9],[2,0,6,0,0,1,3,0,4],[0,4,0,7,0,0,1,0,8],
             [0,0,0,0,0,0,8,0,5],[9,0,5,0,0,0,0,0,0],[0,0,0,2,0,0,0,9,1],
             [0,0,0,1,0,2,4,0,0],[0,0,4,0,3,0,9,0,0],[0,0,0,0,0,0,0,8,6]]

l_faciles=[facile_1,facile_2,facile_3]
l_moyens=[moyen_1,moyen_2,moyen_3]
l_difficiles=[difficile_1,difficile_2,difficile_3]


fini = 0
liste_faux = []


def solveSudoku(grid: list[list], i: int = 0, j: int = 0):
    i, j = findNextCellToFill(grid)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
    grid[i][j] = 0
    return False


def findNextCellToFill(grid: list[list], idebut: int = 0, jdebut: int = 0) -> tuple:
    for i in range(idebut, len(grid)):
        for j in range(jdebut, len(grid[0])):
            if grid[i][j] == 0:
                return i, j
    return -1, -1


def rowOK(grid: list, i: int, e: int) -> bool:
    for k in range(0, 9):
        if grid[i][k] == e:
            return False
    return True


def columnOK(grid: list, j: int, e: int) -> bool:
    for k in range(0, 9):
        if grid[k][j] == e:
            return False
    return True


def sectorOK(grid: list, i: int, j: int, e: int) -> bool:
    id = (i // 3) * 3
    jd = (j // 3) * 3
    for k in range(id, id + 3):
        for l in range(jd, jd + 3):
            if grid[k][l] == e:
                return False
    return True


def isValid(grid: list, i: int, j: int, e: int) -> bool:
    return rowOK(grid, i, e) and columnOK(grid, j, e) and sectorOK(grid, i, j, e)


def print_sudoku(grid):
    ligne = "-" * 25
    for i in range(9):
        if i % 3 == 0:
            print(ligne)
        l = "| "
        for j in range(9):
            l += str(grid[i][j]) + " "
            if j % 3 == 2:
                l += "| "
        print(l)
    print(ligne)


def setup():
    createCanvas(taillecase * 9, taillecase * (9 + 4))
    background("grey")
    textAlign("center", "center")


def place(case: tuple):
    global plateau
    i, j = case
    if plateau_depart[i][j] != 0:
        return False
    if keyIsDown(K_1):
        plateau[i][j] = 1
    if keyIsDown(K_2):
        plateau[i][j] = 2
    if keyIsDown(K_3):
        plateau[i][j] = 3
    if keyIsDown(K_4):
        plateau[i][j] = 4
    if keyIsDown(K_5):
        plateau[i][j] = 5
    if keyIsDown(K_6):
        plateau[i][j] = 6
    if keyIsDown(K_7):
        plateau[i][j] = 7
    if keyIsDown(K_8):
        plateau[i][j] = 8
    if keyIsDown(K_9):
        plateau[i][j] = 9
    if keyIsDown(K_BACKSPACE):
        plateau[i][j] = 0
    rempli()


def corrige():
    global plateau, plateau_corige
    plateau = deepcopy(plateau_corige)
    ihm.visibled(['bouton_recommencer_fin', 'bouton_menu_fin'])
    ihm.unvisibleb(['bouton_corrige'])


def compare():
    global liste_faux, fini
    liste_faux = []
    for i in range(9):
        for j in range(9):
            if plateau_corige[i][j] != plateau[i][j]:
                liste_faux.append([i, j])
    if liste_faux != []:
        fini = 3
        return False
    if fini != 3:
        ihm.unvisibleb(['bouton_pause', 'bouton_verifie'])
        ihm.visibled(['bouton_recommencer_fin','bouton_menu_fin'])
        print("gagné")
        return True


def rempli():
    global fini
    for i in range(9):
        for j in range(9):
            if plateau[i][j] == 0:
                ihm.unvisibleb(['bouton_verifie','bouton_corrige'])
                return False
    fini = 1
    ihm.visibled(['bouton_verifie','bouton_corrige'])
    return True


def reprendre():
    global fini
    ihm.objet_by_name('bouton_pause').visible = True
    ihm.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause',])
    fini = 1


def pause():
    global fini
    ihm.objet_by_name('bouton_pause').visible = False
    ihm.visibled(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause','bouton_verifie'])
    fini = 2


def init_sudoku():
    global fini
    fini = 0
    ihm.visibled(['bouton_facile','bouton_moyen','bouton_dificile'])
    ihm.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause', 'bouton_recommencer_fin',
                    'bouton_menu_fin', 'bouton_corrige', 'bouton_verifie', 'bouton_pause'])


def commence_facile():
    global plateau, plateau_corige, plateau_depart, fini
    fini = 1
    ihm.objet_by_name('bouton_pause').visible = True
    ihm.unvisibleb(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
    x = randint(0, 2)
    plateau = deepcopy(l_faciles[x])
    plateau_depart = deepcopy(l_faciles[x])
    plateau_corige = deepcopy(l_faciles[x])
    solveSudoku(plateau_corige)


def commence_moyen():
    global plateau, plateau_corige, plateau_depart, fini
    fini = 1
    ihm.objet_by_name('bouton_pause').visible = True
    ihm.unvisibleb(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
    x = randint(0, 2)
    plateau = deepcopy(l_moyens[x])
    plateau_depart = deepcopy(l_moyens[x])
    plateau_corige = deepcopy(l_moyens[x])
    solveSudoku(plateau_corige)


def commence_difficile():
    global plateau, plateau_corige, plateau_depart, fini
    fini = 1
    ihm.objet_by_name('bouton_pause').visible = True
    ihm.unvisibleb(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
    x = randint(0, 2)
    plateau = deepcopy(l_difficiles[x])
    plateau_depart = deepcopy(l_difficiles[x])
    plateau_corige = deepcopy(l_difficiles[x])
    solveSudoku(plateau_corige)


ihm.addObjet(Bouton(ihm, (120, 285, 30, 30), '||', command=pause), 'bouton_pause')
ihm.addObjet(Bouton(ihm, (120, 285, 30, 30), '||', command=reprendre, visible=False), 'bouton_reprendre')
ihm.addObjet(Bouton(ihm, (0, 270, 120, 60), 'Recommencer', command=init_sudoku, visible=False),
             'bouton_recommencer_pause')
ihm.addObjet(Bouton(ihm, (150, 270, 120, 60), 'Retour au menu', command=init_sudoku, visible=False),
             'bouton_menu_pause')
ihm.addObjet(Bouton(ihm, (0, 270, 135, 60), 'Recommencer', command=init_sudoku, visible=False),
             'bouton_recommencer_fin')
ihm.addObjet(Bouton(ihm, (135, 270, 135, 60), 'Retour au menu', command=reprendre, visible=False),
             'bouton_menu_fin')
ihm.addObjet(Bouton(ihm, (135, 330, 135, 60), 'Corriger', command=corrige, visible=False),
             'bouton_corrige')
ihm.addObjet(Bouton(ihm, (0, 330, 135, 60), 'Verifier', command=compare, visible=False),
             'bouton_verifie')
ihm.addObjet(Bouton(ihm, (15, 270, 70, 50), 'Facile', command=commence_facile),
             'bouton_facile')
ihm.addObjet(Bouton(ihm, (100, 270, 70, 50), 'Moyen', command=commence_moyen),
             'bouton_moyen')
ihm.addObjet(Bouton(ihm, (185, 270, 70, 50), 'Difficile', command=commence_difficile),
             'bouton_difficile')
ihm.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause', 'bouton_recommencer_fin',
                'bouton_menu_fin', 'bouton_corrige', 'bouton_verifie'])


def compute():
    if mouse_button_pressed() == 0:
        i, j = ((mouseY() // taillecase), (mouseX() // taillecase))
        if i <= 8 and j <= 8:
            if fini == 1:
                place((i, j))
            if fini == 3:
                reprendre()
    ihm.scan_events()


def draw():
    if fini != 0:
        for i in range(9):
            for j in range(9):
                strokeWeight(1)
                if plateau[j][i] != 0:
                    if plateau_depart[j][i] == 0:
                        if fini == 3:
                            for k in liste_faux:
                                text(str(plateau[k[0]][k[1]]), taillecase * k[1], taillecase * k[0], taillecase,
                                     taillecase,
                                     font_color="red")
                            sleep(5)
                            reprendre()
                        text(str(plateau[j][i]), taillecase * i, taillecase * j, taillecase, taillecase,
                             font_color="blue")
                    else:
                        text(str(plateau[j][i]), taillecase * i, taillecase * j, taillecase, taillecase,
                             fontcolor="black")
                else:
                    text("", taillecase * i, taillecase * j, taillecase, taillecase)
        for i in range(2):
            strokeWeight(4)
            line(90 * (i + 1), 0, 90 * (i + 1), 270)
            line(0, 90 * (i + 1), 270, 90 * (i + 1))
    else:
        text('Choisissez la difficulté.',0,0,270,270)
    ihm.draw()


run(globals())

