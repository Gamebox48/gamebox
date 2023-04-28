from likeprocessing.processing import *

class Morpion(Dialog):
    textAlign("center","center")
    taillecase = 100
    textFont("Comic sans ms")
    def __init__(self, parent, posx, posy):
        super().__init__(parent,
                         (posx, posy, Morpion.taillecase * 3,
                          Morpion.taillecase * 4),cadre=False)
        self.paint = Painter(self, (
            0, 0, Morpion.taillecase * 3,
            Morpion.taillecase * 4))
        self.paint.draw_paint = self.draw_paint
        self.addObjet(self.paint)
        self.tour = 1
        self.gagnant = 0
        self.fini = 0
        self.plateau = [["", "", ""], ["", "", ""], ["", "", ""]]

# initialise le jeu
    def init_morpion(self):
        self.plateau = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.fini = 0
        self.gagnant = 0

# renvoie si le plateau possède au moins un espace vide:
    def recherche(self):
        for i in range(3):
            for j in range(3):
                if self.plateau[i][j] == "":
                    return True
        return False

# vérifie si le joueur actuel gagne
    def gagne(self):
        for j in range(len(self.plateau)):
            if self.plateau[j][0] == self.tour and self.plateau[j][1] == self.tour and self.plateau[j][2] == self.tour \
                    or self.plateau[0][j] == self.tour and self.plateau[1][j] == self.tour and self.plateau[2][j] == self.tour:
                self.gagnant = self.tour
                return True
        if self.plateau[0][0] == self.tour and self.plateau[1][1] == self.tour and self.plateau[2][2] == self.tour \
                or self.plateau[2][0] == self.tour and self.plateau[1][1] == self.tour and self.plateau[0][2] == self.tour:
            self.gagnant = self.tour
            return True
        return False

# place une forme dans le plateau et modifie la valeur de tour pour changer de personne qui doit jouer
    def place(self, name):
        if self.fini == 0:
            self.plateau[name[1]][name[0]] = self.tour
            self.gagne()
            self.tour = self.tour % 2 + 1

# dessine l'interface de jeu
    def draw_paint(self):
        for i in range(3):
            for j in range(3):
                if self.tour == 1:
                    self.couleur = "red"
                    text('Au joueur 1 de jouer.', 0, 300, 300, 100, font_size=30)
                else:
                    self.couleur = "blue"
                    text('Au joueur 2 de jouer.', 0, 300, 300, 100, font_size=30)
                if self.plateau[j][i] == "":
                    rect(self.taillecase * i, self.taillecase * j, self.taillecase, self.taillecase, fill_mouse_on=self.couleur, command=self.place,
                         name=(i, j))
                elif self.plateau[j][i] == 1:
                    rect(self.taillecase * i, self.taillecase * j, self.taillecase, self.taillecase, fill="white")
                    circle(10 + self.taillecase * i, 10 + self.taillecase * j, self.taillecase - 20, no_fill=True, stroke="red",
                           stroke_weight=5)
                else:
                    rect(self.taillecase * i, self.taillecase * j, self.taillecase, self.taillecase, fill="white")
                    strokeWeight(5)
                    line(self.taillecase * i + 10, self.taillecase * j + 10, self.taillecase * (i + 1) - 10, self.taillecase * (j + 1) - 10,
                         stroke="blue")
                    line(self.taillecase * (i + 1) - 10, self.taillecase * j + 10, self.taillecase * i + 10, self.taillecase * (j + 1) - 10,
                         stroke="blue")
                    strokeWeight(1)
                if self.gagnant == 1:
                    text('Le joueur 1 a gagné!', 0, 300, 300, 100, font_size=30)
                    self.fini = 2
                elif self.gagnant == 2:
                    text('Le joueur 2 a gagné!', 0, 300, 300, 100, font_size=30)
                    self.fini = 2
                if self.recherche() == False and self.fini != 2:
                    text('Match nul', 0, 300, 300, 100, font_size=30)
                    self.fini = 1

if __name__ == '__main__':
    ihm = IhmScreen()


    def setup():
        createCanvas(300,400)
        background("grey")
        ihm.init()
        ihm.addObjet(Morpion(ihm, 0, 0))


    def compute():
        ihm.scan_events()


    def draw():
        ihm.draw()


    run(globals())