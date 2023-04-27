from likeprocessing.processing import *
from copy import deepcopy

class Sudoku(Dialog):
    taillecase = 30
    textFont("Comic sans ms", 20)




    def __init__(self,parent,posx,posy):
        super().__init__(parent,
                         (posx, posy, Sudoku.taillecase * 9,
                          Sudoku.taillecase * (9 + 2)))
        self.paint = Painter(self, (
            0, 0, Sudoku.taillecase * 9 + 1,
            Sudoku.taillecase * 9 + 1))
        self.paint.draw_paint = self.draw_paint
        self.addObjet(self.paint)
        self.addObjet(Bouton(ihm, (120, 285, 30, 30), '||', command=self.pause, visible=False), 'bouton_pause')
        self.addObjet(Bouton(ihm, (120, 285, 30, 30), '||', command=self.reprendre, visible=False), 'bouton_reprendre')
        self.addObjet(Bouton(ihm, (0, 270, 120, 60), 'Recommencer', command=self.init_sudoku, visible=False),
                     'bouton_recommencer_pause')
        self.addObjet(Bouton(ihm, (150, 270, 120, 60), 'Retour au menu', command=self.init_sudoku, visible=False),
                     'bouton_menu_pause')
        self.addObjet(Bouton(ihm, (0, 270, 135, 60), 'Recommencer', command=self.init_sudoku, visible=False),
                     'bouton_recommencer_fin')
        self.addObjet(Bouton(ihm, (135, 270, 135, 60), 'Retour au menu', command=self.reprendre, visible=False),
                     'bouton_menu_fin')
        self.addObjet(Bouton(ihm, (135, 330, 135, 60), 'Corriger', command=self.corrige, visible=False),
                     'bouton_corrige')
        self.addObjet(Bouton(ihm, (0, 330, 135, 60), 'Verifier', command=self.compare, visible=False),
                     'bouton_verifie')
        self.addObjet(Bouton(ihm, (15, 305, 70, 50), 'Facile', command=self.commence_facile),
                     'bouton_facile')
        self.addObjet(Bouton(ihm, (100, 305, 70, 50), 'Moyen', command=self.commence_moyen),
                     'bouton_moyen')
        self.addObjet(Bouton(ihm, (185, 305, 70, 50), 'Difficile', command=self.commence_difficile),
                     'bouton_difficile')

        facile_1 = [[0, 6, 0, 4, 2, 0, 0, 0, 1], [1, 9, 0, 0, 8, 3, 0, 2, 0], [0, 0, 2, 0, 1, 0, 7, 0, 0],
                    [0, 0, 0, 8, 7, 0, 5, 0, 0], [0, 5, 1, 3, 4, 9, 0, 0, 2], [4, 0, 3, 0, 5, 0, 0, 8, 0],
                    [6, 0, 5, 1, 3, 2, 0, 0, 0], [7, 0, 4, 0, 0, 8, 0, 1, 0], [0, 1, 0, 0, 6, 0, 8, 5, 0]]

        facile_2 = [[0, 7, 3, 2, 5, 0, 8, 9, 0], [8, 0, 1, 0, 0, 9, 0, 0, 0], [9, 0, 0, 8, 0, 0, 0, 4, 0],
                    [0, 1, 9, 0, 6, 4, 5, 0, 8], [0, 0, 0, 1, 0, 0, 0, 7, 9], [0, 3, 4, 0, 0, 8, 0, 6, 0],
                    [0, 6, 8, 4, 2, 0, 0, 1, 0], [0, 4, 0, 0, 1, 0, 6, 8, 7], [1, 0, 0, 0, 0, 0, 0, 5, 4]]

        facile_3 = [[0, 7, 0, 0, 0, 5, 0, 0, 0], [1, 0, 0, 0, 3, 0, 5, 0, 8], [0, 0, 0, 2, 0, 9, 0, 6, 0],
                    [9, 1, 0, 5, 0, 0, 4, 2, 0], [6, 8, 0, 3, 0, 0, 0, 1, 0], [2, 5, 4, 0, 9, 0, 0, 0, 3],
                    [7, 0, 6, 8, 0, 1, 0, 4, 0], [3, 4, 5, 0, 0, 6, 0, 7, 1], [0, 0, 1, 0, 7, 0, 2, 0, 6]]

        moyen_1 = [[0, 0, 9, 0, 0, 1, 6, 7, 0], [6, 4, 0, 8, 0, 0, 0, 9, 2], [0, 0, 0, 9, 0, 0, 3, 0, 0],
                   [0, 0, 0, 4, 0, 7, 5, 0, 6], [0, 5, 6, 0, 0, 0, 4, 3, 0], [4, 0, 1, 6, 0, 0, 0, 0, 0],
                   [5, 6, 7, 0, 0, 0, 9, 8, 1], [0, 1, 0, 0, 8, 9, 0, 0, 0], [0, 9, 0, 0, 0, 0, 0, 0, 0]]

        moyen_2 = [[6, 0, 0, 5, 3, 1, 9, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 7], [5, 4, 9, 0, 0, 0, 0, 0, 0],
                   [2, 0, 0, 7, 0, 0, 0, 0, 0], [0, 0, 7, 0, 9, 0, 0, 3, 2], [0, 9, 0, 0, 1, 8, 0, 4, 5],
                   [0, 2, 0, 0, 7, 4, 5, 0, 1], [4, 0, 0, 9, 0, 0, 3, 0, 0], [0, 0, 3, 0, 0, 0, 0, 2, 0]]

        moyen_3 = [[0, 0, 0, 3, 2, 4, 7, 8, 5], [0, 8, 5, 0, 7, 0, 0, 0, 0], [0, 0, 0, 0, 5, 0, 0, 0, 0],
                   [8, 0, 0, 0, 6, 2, 9, 5, 0], [0, 0, 7, 5, 0, 0, 0, 3, 2], [5, 0, 0, 0, 0, 0, 0, 0, 1],
                   [6, 0, 3, 0, 0, 0, 2, 0, 4], [0, 0, 0, 2, 4, 0, 0, 1, 6], [2, 0, 0, 7, 0, 6, 0, 0, 0]]

        difficile_1 = [[0, 0, 0, 4, 0, 0, 5, 0, 6], [0, 0, 0, 0, 0, 0, 4, 3, 0], [0, 6, 0, 5, 0, 0, 0, 1, 0],
                       [0, 0, 3, 0, 5, 0, 0, 9, 0], [4, 0, 7, 0, 0, 0, 8, 0, 0], [9, 0, 0, 0, 8, 7, 2, 0, 0],
                       [0, 7, 1, 0, 0, 5, 0, 0, 0], [0, 0, 0, 0, 0, 6, 0, 0, 0], [0, 5, 0, 0, 0, 1, 0, 0, 4]]

        difficile_2 = [[0, 4, 0, 2, 0, 0, 0, 8, 0], [2, 0, 0, 0, 7, 0, 0, 3, 0], [1, 0, 7, 0, 0, 0, 0, 0, 0],
                       [0, 2, 0, 0, 0, 6, 3, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 5, 0, 4, 0, 0, 0, 9, 0],
                       [0, 3, 0, 9, 0, 0, 5, 0, 0], [0, 0, 0, 7, 0, 0, 1, 0, 0], [0, 1, 5, 0, 4, 0, 6, 0, 0]]

        difficile_3 = [[8, 0, 0, 0, 0, 5, 0, 2, 9], [2, 0, 6, 0, 0, 1, 3, 0, 4], [0, 4, 0, 7, 0, 0, 1, 0, 8],
                       [0, 0, 0, 0, 0, 0, 8, 0, 5], [9, 0, 5, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 0, 9, 1],
                       [0, 0, 0, 1, 0, 2, 4, 0, 0], [0, 0, 4, 0, 3, 0, 9, 0, 0], [0, 0, 0, 0, 0, 0, 0, 8, 6]]

        self.l_faciles = [facile_1, facile_2, facile_3]
        self.l_moyens = [moyen_1, moyen_2, moyen_3]
        self.l_difficiles = [difficile_1, difficile_2, difficile_3]

        self.fini = 0
        self.liste_faux = []

    def init_sudoku(self):
        global fini
        self.fini = 0
        self.visibled(['bouton_facile', 'bouton_moyen', 'bouton_dificile'])
        self.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause', 'bouton_recommencer_fin',
                        'bouton_menu_fin', 'bouton_corrige', 'bouton_verifie', 'bouton_pause'])

    def commence_facile(self):
        self.fini = 1
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
        x = randint(0, 2)
        self.plateau = deepcopy(self.l_faciles[x])
        self.plateau_depart = deepcopy(self.l_faciles[x])
        self.plateau_corige = deepcopy(self.l_faciles[x])
        self.solveSudoku(self.plateau_corige)

    def commence_moyen(self):
        self.fini = 1
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
        x = randint(0, 2)
        self.plateau = deepcopy(self.l_moyens[x])
        self.plateau_depart = deepcopy(self.l_moyens[x])
        self.plateau_corige = deepcopy(self.l_moyens[x])
        self.solveSudoku(self.plateau_corige)

    def commence_difficile(self):
        self.fini = 1
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
        x = randint(0, 2)
        self.plateau = deepcopy(self.l_difficiles[x])
        self.plateau_depart = deepcopy(self.l_difficiles[x])
        self.plateau_corige = deepcopy(self.l_difficiles[x])
        self.solveSudoku(self.plateau_corige)

    def reprendre(self):
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause', ])
        self.fini = 1

    def pause(self):
        self.objet_by_name('bouton_pause').visible = False
        self.visibled(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause'])
        self.fini = 2

    def corrige(self):
        self.plateau = deepcopy(self.plateau_corige)
        self.visibled(['bouton_recommencer_fin', 'bouton_menu_fin'])
        self.unvisibleb(['bouton_corrige', 'bouton_verifie'])

    def compare(self):
        self.liste_faux = []
        for i in range(9):
            for j in range(9):
                if self.plateau_corige[i][j] != self.plateau[i][j]:
                    self.liste_faux.append([i, j])
        if self.liste_faux != []:
            self.fini = 3
            return False
        if self.fini != 3:
            self.unvisibleb(['bouton_pause', 'bouton_verifie'])
            self.visibled(['bouton_recommencer_fin', 'bouton_menu_fin'])
            print("gagné")
            return True

    def rempli(self):
        for i in range(9):
            for j in range(9):
                if self.plateau[i][j] == 0:
                    self.unvisibleb(['bouton_verifie', 'bouton_corrige'])
                    return False
        self.fini = 1
        self.visibled(['bouton_verifie', 'bouton_corrige'])
        return True

    def place(self,case: tuple):
        i, j = case
        if self.plateau_depart[i][j] != 0:
            return False
        if keyIsDown(K_1):
            self.plateau[i][j] = 1
        if keyIsDown(K_2):
            self.plateau[i][j] = 2
        if keyIsDown(K_3):
            self.plateau[i][j] = 3
        if keyIsDown(K_4):
            self.plateau[i][j] = 4
        if keyIsDown(K_5):
            self.plateau[i][j] = 5
        if keyIsDown(K_6):
            self.plateau[i][j] = 6
        if keyIsDown(K_7):
            self.plateau[i][j] = 7
        if keyIsDown(K_8):
            self.plateau[i][j] = 8
        if keyIsDown(K_9):
            self.plateau[i][j] = 9
        if keyIsDown(K_BACKSPACE):
            self.plateau[i][j] = 0
        self.rempli()

    def solveSudoku(self,grid: list[list], i: int = 0, j: int = 0):
        i, j = self.findNextCellToFill(grid)
        if i == -1:
            return True
        for e in range(1, 10):
            if self.isValid(grid, i, j, e):
                grid[i][j] = e
                if self.solveSudoku(grid, i, j):
                    return True
        grid[i][j] = 0
        return False

    def findNextCellToFill(self,grid: list[list], idebut: int = 0, jdebut: int = 0) -> tuple:
        for i in range(idebut, len(grid)):
            for j in range(jdebut, len(grid[0])):
                if grid[i][j] == 0:
                    return i, j
        return -1, -1

    def rowOK(self,grid: list, i: int, e: int) -> bool:
        for k in range(0, 9):
            if grid[i][k] == e:
                return False
        return True

    def columnOK(self,grid: list, j: int, e: int) -> bool:
        for k in range(0, 9):
            if grid[k][j] == e:
                return False
        return True

    def sectorOK(self,grid: list, i: int, j: int, e: int) -> bool:
        id = (i // 3) * 3
        jd = (j // 3) * 3
        for k in range(id, id + 3):
            for l in range(jd, jd + 3):
                if grid[k][l] == e:
                    return False
        return True

    def isValid(self,grid: list, i: int, j: int, e: int) -> bool:
        return self.rowOK(grid, i, e) and self.columnOK(grid, j, e) and self.sectorOK(grid, i, j, e)