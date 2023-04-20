from likeprocessing.processing import *
from copy import deepcopy

taillecase = 30
textFont("Comic sans ms", 20)
ihm = IhmScreen()

hardest_sudoku = [[8, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 6, 0, 0, 0, 0, 0], [0, 7, 0, 0, 9, 0, 2, 0, 0],
                  [0, 5, 0, 0, 0, 7, 0, 0, 0], [0, 0, 0, 0, 4, 5, 7, 0, 0], [0, 0, 0, 1, 0, 0, 0, 3, 0],
                  [0, 0, 1, 0, 0, 0, 0, 6, 8], [0, 0, 8, 5, 0, 0, 0, 1, 0], [0, 9, 0, 0, 0, 0, 4, 0, 0]]

plateau = deepcopy(hardest_sudoku)
plateau_depart = deepcopy(hardest_sudoku)
plateau_corige = deepcopy(hardest_sudoku)



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
        # Undo the current cell for backtracking
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
    createCanvas(taillecase * 9, taillecase * (9 + 2))
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
    solveSudoku(plateau_corige)
    plateau=deepcopy(plateau_corige)
    ihm.visibled(['bouton_recommencer_fin','bouton_menu_fin'])
    ihm.unvisibleb(['bouton_corrige'])


def compare():
    global liste_faux,fini
    liste_faux = []
    for i in range(9):
        for j in range(9):
            if plateau_corige[i][j] != plateau[i][j]:
                liste_faux += [i, j]
    if liste_faux!=[]:
        ihm.visibled(['bouton_corrige'])
        ihm.unvisibleb(['bouton_pause','bouton_verifie'])
        fini=4
        return False
    if fini !=4:
        ihm.unvisibleb(['bouton_pause', 'bouton_verifie'])
        print("gagné")
        return True


def rempli():
    global fini
    for i in range(9):
        for j in range(9):
            if plateau[i][j] == 0:
                return False
    fini = 1
    ihm.visibled(['bouton_verifie'])
    return True

def reprendre():
    global fini
    ihm.objet_by_name('bouton_pause').visible = True
    ihm.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause'])
    fini = 0

def pause():
    global fini
    ihm.objet_by_name('bouton_pause').visible = False
    ihm.visibled(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause'])
    fini = 3

def init_sudoku():
    global plateau, plateau_corige, plateau_depart, fini
    fini = 0
    ihm.objet_by_name('bouton_pause').visible = True
    ihm.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause', 'bouton_recommencer_fin',
                    'bouton_menu_fin','bouton_corrige','bouton_verifie'])
    plateau = deepcopy(hardest_sudoku)
    plateau_depart = deepcopy(hardest_sudoku)
    plateau_corige = deepcopy(hardest_sudoku)

ihm.addObjet(Bouton(ihm, (120, 285, 30, 30), '||', command=pause), 'bouton_pause')
ihm.addObjet(Bouton(ihm, (120, 285, 30, 30), '||', command=reprendre, visible=False), 'bouton_reprendre')
ihm.addObjet(Bouton(ihm, (0, 270, 120, 60), 'Recommencer', command=init_sudoku, visible=False),
             'bouton_recommencer_pause')
ihm.addObjet(Bouton(ihm, (150, 270, 120, 60), 'Retour au menu', command=init_sudoku, visible=False),
             'bouton_menu_pause')
ihm.addObjet(Bouton(ihm, (0, 270, 135, 60), 'Recommencer', command=init_sudoku, visible=False),
             'bouton_recommencer_fin')
ihm.addObjet(Bouton(ihm, (135, 270, 140, 60), 'Retour au menu', command=reprendre, visible=False),
             'bouton_menu_fin')
ihm.addObjet(Bouton(ihm, (135, 270, 140, 60), 'Corriger', command=corrige, visible=False),
             'bouton_corrige')
ihm.addObjet(Bouton(ihm, (135, 270, 140, 60), 'Verifier', command=compare, visible=False),
             'bouton_verifie')



def compute():
    if mouse_button_pressed() == 0:
        i, j = ((mouseY() // taillecase), (mouseX() // taillecase))
        if i <= 8 and j <= 8:
            place((i, j))
    ihm.scan_events()


def draw():
    if fini == 4:
        for i in liste_faux:
            text(str(plateau[i[0]][i[1]]),taillecase*i[0],taillecase*i[1],taillecase,taillecase, font_color="red")
    for i in range(9):
        for j in range(9):
            strokeWeight(1)
            if plateau[j][i] != 0:
                if plateau_depart[j][i] == 0:
                    text(str(plateau[j][i]), taillecase * i, taillecase * j, taillecase, taillecase, font_color="blue")
                else: text(str(plateau[j][i]), taillecase * i, taillecase * j, taillecase, taillecase, fontcolor="black")
            else:
                text("", taillecase * i, taillecase * j, taillecase, taillecase)
    for i in range(2):
        strokeWeight(4)
        line(90 * (i + 1), 0, 90 * (i + 1), 270)
        line(0, 90 * (i + 1), 270, 90 * (i + 1))
    ihm.draw()


run(globals())

if __name__ == '__main__':
    solveSudoku(hardest_sudoku, 0, 0)
    print_sudoku(hardest_sudoku)
