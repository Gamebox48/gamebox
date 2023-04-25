from copy import deepcopy

from likeprocessing.processing import *
from random import shuffle


class Sudoku(Dialog):

    def __init__(self, parent, x, y):
        super().__init__(parent, (x, y, 800, 575), cadre=False)
        self.difficult = 0
        self.paint = Painter(self, (0, 0, 270, 270))
        self.paint.draw_paint = self.draw_sudoku
        self.addObjet(self.paint, "paint")
        self.addObjet(Label(self, (0, 0, 150, 30), "niveau: facile", font_size=20), "niveau")
        self.addObjet(Bouton(self, (0, 0, 30, 30), "-", command=self.moins), "bp_moins")
        self.addObjet(Bouton(self, (0, 0, 30, 30), "+", command=self.plus), "bp_plus")
        self.addObjet(Bouton(self, (0, 0, 50, 30), "Start", command=self.start), "bp_start")
        self.addObjet(Bouton(self, (0, 0, 50, 30), "<<", command=self.undo), "bp_undo")
        self.addObjet(Bouton(self, (0, 0, 50, 30), ">>", command=self.redo), "bp_redo")
        self.pack(["paint", ["niveau", "bp_moins", "bp_plus"], ["bp_start", "bp_undo", "bp_redo"]])
        self.plateau_depart = [[7, 6, 1, 8, 5, 9, 4, 3, 2],
                               [5, 4, 8, 2, 3, 6, 7, 9, 1],
                               [9, 3, 2, 4, 1, 7, 6, 5, 8],
                               [1, 7, 3, 6, 4, 5, 2, 8, 9],
                               [4, 2, 9, 1, 7, 8, 3, 6, 5],
                               [6, 8, 5, 9, 2, 3, 1, 4, 7],
                               [3, 5, 4, 7, 8, 1, 9, 2, 6],
                               [8, 9, 7, 3, 6, 2, 5, 1, 4],
                               [2, 1, 6, 5, 9, 4, 8, 7, 3]]
        self.niveau_str = ["facile", "moyen", "difficile"]
        self.niveau = 0
        self.jeu_en_cours = False
        print(self.plateau_depart)
        self.plateau = []
        self.taillecase = 30
        self.coups = []
        self.index_coup = -1
        self.bravo = False

    def plus(self):
        self.niveau = borner(self.niveau + 1, 0, 2)
        self.objet_by_name("niveau").text(f"niveau: {self.niveau_str[self.niveau]}")

    def moins(self):
        self.niveau = borner(self.niveau - 1, 0, 2)
        self.objet_by_name("niveau").text(f"niveau: {self.niveau_str[self.niveau]}")

    def start(self):
        self.plateau_depart = self.creer_plateau(self.plateau_depart, self.niveau)
        self.plateau = deepcopy(self.plateau_depart)
        self.coups = []
        self.bravo = False
        self.index_coup = -1
        self.jeu_en_cours = True
        self.objet_by_name("bp_start").disabled = True

    def undo(self):
        i, j, v = self.coups[self.index_coup]
        if not self.isValid(self.plateau, i, j, v):
            self.plateau[i][j] = 0
            self.coups.pop(self.index_coup)
        else:
            self.plateau[i][j] = 0
        self.index_coup = borner(self.index_coup - 1, -1, len(self.coups) - 1)

    def redo(self):
        self.index_coup = borner(self.index_coup + 1, -1, len(self.coups) - 1)
        i, j, v = self.coups[self.index_coup]
        self.plateau[i][j] = v

    def creer_plateau(self, grille: list[list], niveau=0) -> list[list]:
        """crée plateau de départ à partir d'une grille valide"""
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        niveaux = [1, 6, 7]
        grille_depart = grille.copy()
        for i in range(9):
            shuffle(indices)
            for j in range(niveaux[niveau]):
                grille_depart[i][indices[j]] = 0
        return grille_depart

    def rowOK(self, grid: list, i: int, j: int, e: int) -> bool:
        for k in range(0, 9):
            if k != j and grid[i][k] == e:
                return False
        return True

    def columnOK(self, grid: list, i: int, j: int, e: int) -> bool:
        for k in range(0, 9):
            if k != i and grid[k][j] == e:
                return False
        return True

    def sectorOK(self, grid: list, i: int, j: int, e: int) -> bool:
        id = (i // 3) * 3
        jd = (j // 3) * 3
        for k in range(id, id + 3):
            for l in range(jd, jd + 3):
                if k != i and l != j and grid[k][l] == e:
                    return False
        return True

    def isValid(self, grid: list, i: int, j: int, e: int) -> bool:
        if e == 0 and self.plateau[i][j] == 0:
            return True
        return self.rowOK(grid, i, j, e) and self.columnOK(grid, i, j, e) and self.sectorOK(grid, i, j, e)

    def is_finish(self):
        for l in self.plateau:
            if 0 in l:
                return False
        return True

    def gagner(self):
        for i in range(9):
            for j in range(9):
                if not self.isValid(self.plateau, i, j, self.plateau[i][j]):
                    return False
        return True

    def draw_sudoku(self):
        textAlign("center", "center")
        textFont("Comic sans ms", 20)
        if self.jeu_en_cours:
            if len(self.coups) == 0 or self.isValid(self.plateau, *self.coups[self.index_coup]):
                fc = "grey"
            else:
                fc = "red"
            for i in range(9):
                for j in range(9):
                    strokeWeight(1)
                    if self.plateau_depart[i][j] != 0:
                        text(str(self.plateau_depart[i][j]), self.taillecase * j, self.taillecase * i, self.taillecase,
                             self.taillecase, font_color="black")
                    elif self.plateau[i][j] != 0:
                        text(str(self.plateau[i][j]), self.taillecase * j, self.taillecase * i, self.taillecase,
                             self.taillecase, font_color="red", fill_mouse_on=fc)
                    else:
                        rect(self.taillecase * j, self.taillecase * i, self.taillecase, self.taillecase,
                             fill_mouse_on=fc)
        for i in range(3):
            strokeWeight(4)
            line(3 * self.taillecase * (i + 1), 0, 3 * self.taillecase * (i + 1), 9 * self.taillecase)
            line(0, 3 * self.taillecase * (i + 1), 9 * self.taillecase, 3 * self.taillecase * (i + 1))
        if self.bravo:
            text("Bravo vous avez gagné !", 0, self.paint.height // 2, self.paint.width, 30)

    def ajoute_coup(self, i, j, v):
        if self.index_coup != len(self.coups) - 1:
            self.coups = self.coups[0:self.index_coup + 1]
        self.coups.append((i, j, v))
        self.index_coup = len(self.coups) - 1

    def place(self, case: tuple):
        i, j = case
        if self.plateau_depart[i][j] != 0:
            return False
        if keyIsPressed():
            if keyIsDown(K_1):
                self.plateau[i][j] = 1
                self.ajoute_coup(i, j, 1)
            elif keyIsDown(K_2):
                self.plateau[i][j] = 2
                self.ajoute_coup(i, j, 2)
            elif keyIsDown(K_3):
                self.plateau[i][j] = 3
                self.ajoute_coup(i, j, 3)
            elif keyIsDown(K_4):
                self.plateau[i][j] = 4
                self.ajoute_coup(i, j, 4)
            elif keyIsDown(K_5):
                self.plateau[i][j] = 5
                self.ajoute_coup(i, j, 5)
            elif keyIsDown(K_6):
                self.plateau[i][j] = 6
                self.ajoute_coup(i, j, 6)
            elif keyIsDown(K_7):
                self.plateau[i][j] = 7
                self.ajoute_coup(i, j, 7)
            elif keyIsDown(K_8):
                self.plateau[i][j] = 8
                self.ajoute_coup(i, j, 8)
            elif keyIsDown(K_9):
                self.plateau[i][j] = 9
                self.ajoute_coup(i, j, 9)
            elif keyIsDown(K_BACKSPACE) or keyIsDown(K_SPACE):
                self.plateau[i][j] = 0
                self.ajoute_coup(i, j, 0)

    def scan_mouse(self):
        if mouse_click_down() == 1:
            j, i = ((self.paint.mouse_x() // self.taillecase), (self.paint.mouse_y() // self.taillecase))
            if i <= 8 and j <= 8:
                self.place((i, j))
                if self.is_finish():
                    if self.gagner():
                        self.bravo = True
                        self.objet_by_name("bp_start").disabled = False

        super().scan_mouse()
        if self.index_coup == -1:
            self.objet_by_name("bp_undo").disabled = True
        else:
            self.objet_by_name("bp_undo").disabled = False
        if self.index_coup == len(self.coups) - 1 or len(self.coups) == 0:
            self.objet_by_name("bp_redo").disabled = True
        else:
            self.objet_by_name("bp_redo").disabled = False


if __name__ == '__main__':
    ihm = IhmScreen()
    sudoku: Sudoku


    def setup():
        global sudoku
        createCanvas(1200, 900)
        ihm.init()
        sudoku = Sudoku(ihm, 200, 100)
        ihm.addObjet(sudoku)


    def compute():
        ihm.scan_events()


    def draw():
        ihm.draw()


    run(globals())
