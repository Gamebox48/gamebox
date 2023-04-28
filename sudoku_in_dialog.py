from likeprocessing.processing import *
from copy import deepcopy


class Sudoku(Dialog):
    textAlign("center", "center")
    textFont("Comic sans ms", 30)
    taillecase = 50

    def __init__(self, parent, posx, posy):
        super().__init__(parent,
                         (posx, posy, Sudoku.taillecase * 9,
                          Sudoku.taillecase * 9 + (30 * 4)), cadre=False)
        self.paint = Painter(self, (
            0, 0, Sudoku.taillecase * 9,
            Sudoku.taillecase * 9))
        self.paint.draw_paint = self.draw_paint
        self.addObjet(self.paint)
        self.addObjet(Bouton(ihm, (210, 465, 30, 30), '||', command=self.pause, visible=False), 'bouton_pause')
        self.addObjet(Bouton(ihm, (240, 450, 120, 60), 'Continuer', command=self.reprendre, visible=False),
                      'bouton_reprendre')
        self.addObjet(Bouton(ihm, (90, 450, 120, 60), 'Recommencer', command=self.init_sudoku, visible=False),
                      'bouton_recommencer_pause')
        self.addObjet(Bouton(ihm, (225, 510, 135, 60), 'Corriger', command=self.corrige, visible=False),
                      'bouton_corrige')
        self.addObjet(Bouton(ihm, (75, 510, 135, 60), 'Verifier', command=self.compare, visible=False),
                      'bouton_verifie')
        self.addObjet(Bouton(ihm, (30, 305, 110, 70), 'Facile', command=self.commence_facile),
                      'bouton_facile')
        self.addObjet(Bouton(ihm, (170, 305, 110, 70), 'Moyen', command=self.commence_moyen),
                      'bouton_moyen')
        self.addObjet(Bouton(ihm, (310, 305, 110, 70), 'Difficile', command=self.commence_difficile),
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

    def paint_mouse_x(self):
        # retourne la position de la souris dans le repère de paint
        return mouseX() - self.paint.absolute().x

    def paint_mouse_y(self):
        # retourne la position de la souris dans le repère de paint
        return mouseY() - self.paint.absolute().y

# initialise le jeu
    def init_sudoku(self):
        global fini
        self.fini = 0
        self.visibled(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
        self.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause',
                         'bouton_corrige', 'bouton_verifie', 'bouton_pause'])

# commence le jeu avec un sudoku facile
    def commence_facile(self):
        self.fini = 1
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
        x = randint(0, 2)
        self.plateau = deepcopy(self.l_faciles[x])
        self.plateau_depart = deepcopy(self.l_faciles[x])
        self.plateau_corige = deepcopy(self.l_faciles[x])
        self.solveSudoku(self.plateau_corige)

# commence le jeu avec un sudoku moyen
    def commence_moyen(self):
        self.fini = 1
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
        x = randint(0, 2)
        self.plateau = deepcopy(self.l_moyens[x])
        self.plateau_depart = deepcopy(self.l_moyens[x])
        self.plateau_corige = deepcopy(self.l_moyens[x])
        self.solveSudoku(self.plateau_corige)

# commence le jeu avec un sudoku difficile
    def commence_difficile(self):
        self.fini = 1
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_facile', 'bouton_moyen', 'bouton_difficile'])
        x = randint(0, 2)
        self.plateau = deepcopy(self.l_difficiles[x])
        self.plateau_depart = deepcopy(self.l_difficiles[x])
        self.plateau_corige = deepcopy(self.l_difficiles[x])
        self.solveSudoku(self.plateau_corige)

# fait reprendre le jeu
    def reprendre(self):
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause'])
        self.fini = 1

# met en pause le jeu
    def pause(self):
        self.objet_by_name('bouton_pause').visible = False
        self.visibled(['bouton_reprendre', 'bouton_recommencer_pause'])
        self.unvisibleb(['bouton_verifie', 'bouton_corrige'])
        self.fini = 2

# corrige le sudoku grâce à la solution
    def corrige(self):
        self.plateau = deepcopy(self.plateau_corige)
        self.liste_faux = []
        self.unvisibleb(['bouton_corrige', 'bouton_verifie', 'bouton_pause'])
        self.fini = 5

# Vérifie si le sudoku est résolu, si non il fait la liste des cases fausses
    def compare(self):
        self.liste_faux = []
        for i in range(9):
            for j in range(9):
                if self.plateau_corige[i][j] != self.plateau[i][j]:
                    self.liste_faux.append([i, j])
        if self.liste_faux != []:
            self.fini = 3
            return False
        elif self.fini != 5:
            self.unvisibleb(['bouton_pause', 'bouton_verifie', 'bouton_pause'])
            self.fini = 4
            print("gagné")
            return True

# renvoie si la liste est finie
    def rempli(self):
        for i in range(9):
            for j in range(9):
                if self.plateau[i][j] == 0:
                    self.unvisibleb(['bouton_verifie', 'bouton_corrige'])
                    return False
        self.fini = 1
        self.visibled(['bouton_verifie', 'bouton_corrige'])
        return True

# place le chiffre tapé dans la case si la case ne possèdait pas de chiffre au départ
    def place(self, case: tuple):
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

# résout le sudoku en utilisant une méthode récursive
# sert à la correction
    def solveSudoku(self, grid: list[list], i: int = 0, j: int = 0):
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

# cherche la prochaine case à remplir
# sert à la correction
    def findNextCellToFill(self, grid: list[list], idebut: int = 0, jdebut: int = 0) -> tuple:
        for i in range(idebut, len(grid)):
            for j in range(jdebut, len(grid[0])):
                if grid[i][j] == 0:
                    return i, j
        return -1, -1

# renvoie si le chiffre que l'on veut placer n'est pas déja sur la ligne {i} où l'on veut placer le chiffre {e}
# sert à la correction
    def rowOK(self, grid: list, i: int, e: int) -> bool:
        for k in range(0, 9):
            if grid[i][k] == e:
                return False
        return True

# renvoie si le chiffre {e} que l'on veut placer n'est pas déja sur la colonne {j} où l'on veut placer le chiffre{e}
# sert à la correction
    def columnOK(self, grid: list, j: int, e: int) -> bool:
        for k in range(0, 9):
            if grid[k][j] == e:
                return False
        return True

# renvoie si le chiffre {e} que l'on veut placer n'est pas déja dans le secteur 3x3 où l'on veut placer le chiffre {e}
    def sectorOK(self, grid: list, i: int, j: int, e: int) -> bool:
        id = (i // 3) * 3
        jd = (j // 3) * 3
        for k in range(id, id + 3):
            for l in range(jd, jd + 3):
                if grid[k][l] == e:
                    return False
        return True

# renvoie si le chiffre {e} peut être placé à l'emplacement {i}{j}
# sert à la correction
    def isValid(self, grid: list, i: int, j: int, e: int) -> bool:
        return self.rowOK(grid, i, e) and self.columnOK(grid, j, e) and self.sectorOK(grid, i, j, e)

    def compute(self):
        if mouse_button_pressed() == 0:
            i, j = ((self.paint_mouse_y() // self.taillecase), (self.paint_mouse_x() // self.taillecase))
            if i <= 8 and j <= 8 and i >= 0 and j >= 0:
                if self.fini == 1:
                    self.place((i, j))
                if self.fini == 3:
                    self.reprendre()

    def scan_mouse(self):
        super().scan_mouse()
        self.compute()

# dessine l'interface de jeu
    def draw_paint(self):
        if self.fini != 0:
            for i in range(9):
                for j in range(9):
                    strokeWeight(1)
                    if self.plateau[j][i] != 0:
                        if self.plateau_depart[j][i] == 0:
                            if self.fini == 3:
                                for k in self.liste_faux:
                                    text(str(self.plateau[k[0]][k[1]]), self.taillecase * k[1], self.taillecase * k[0],
                                         self.taillecase,
                                         self.taillecase, font_color="red")
                            text(str(self.plateau[j][i]), self.taillecase * i, self.taillecase * j, self.taillecase,
                                 self.taillecase,
                                 font_color="blue")
                            if self.fini == 5:
                                text(str(self.plateau[j][i]), self.taillecase * i, self.taillecase * j, self.taillecase,
                                     self.taillecase,
                                     font_color="green")
                        else:
                            text(str(self.plateau[j][i]), self.taillecase * i, self.taillecase * j, self.taillecase,
                                 self.taillecase,
                                 fontcolor="black")
                    else:
                        text("", self.taillecase * i, self.taillecase * j, self.taillecase, self.taillecase)
            for i in range(2):
                strokeWeight(4)
                line(150 * (i + 1), 0, 150 * (i + 1), 450)
                line(0, 150 * (i + 1), 450, 150 * (i + 1))
            if self.fini == 1 and self.rempli() == False:
                text(
                    "Appuyez sur une touche de chiffre (ou sur\nretour pour effacer) de votre clavier et cliquez\navec votre souris sur une case en même temps",
                    0, 495, 450, 75, font_color="black", no_stroke=True, font_size=15)
        else:
            text('Choisissez la difficulté.', 0, 0, 450, 450)


if __name__ == '__main__':
    ihm = IhmScreen()


    def setup():
        createCanvas(450, 570)
        background("grey")
        ihm.init()
        ihm.addObjet(Sudoku(ihm, 0, 0))


    def compute():
        ihm.scan_events()


    def draw():
        ihm.draw()


    run(globals())
