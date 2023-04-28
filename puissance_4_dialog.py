from likeprocessing.processing import *


class MyGame(Dialog):
    def __init__(self, parent, x, y):
        """parent : ihm
        x, y : position du jeu dans l'ihm"""
        super().__init__(parent, (x, y, 500, 500), cadre=False)
        # 500, 500 : largeur et hauteur de la fenêtre du jeu
        # cadre = False supprime la barre de titre de la fenêtre du jeu
        # self.paint : objet de dessin de la fenêtre du jeu
        # les commandes de dessin likeprocessing seront placées dans la méthode self.draw_paint
        self.paint = Painter(self, (0, 0, 500, 480))
        self.paint.draw_paint = self.draw_paint
        # ajout de self.paint à la fenêtre du jeu
        self.addObjet(self.paint, "paint")
        # ajout de deux boutons par exemple

        # variable du jeux
        self.grille = [[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]]

        self.couleurs = ['white', 'red', 'orange']
        self.joueur = 1
        self.fini = 0

    def compute(self):
        # ici ce trouve de code pour les calculs du jeu
        pass

    def scan_mouse(self):
        # cette méthode permet d'excuter la méthode compute à chaque fois que
        # l'instruction ihm.scan_events() sera exécutée
        super().scan_mouse()
        self.compute()

    def click_colonne(self, name):
        if self.fini == 0:
            if self.grille[0][name] == 0:
                for i in range(len(self.grille)):
                    if self.grille[i][name] > 0:
                        self.grille[i - 1][name] = self.joueur
                        self.gagne(i - 1, name)
                        break
                    elif i == len(self.grille) - 1:
                        self.grille[i][name] = self.joueur
                        self.gagne(i, name)
                        break
                self.joueur = (self.joueur % 2) + 1

    def gagne(self, i, j):
        nb_ligne = self.gagne_droite(i, j) + self.gagne_gauche(i, j) - 1
        nb_colonne = self.gagne_bas(i, j) + self.gagne_haut(i, j) - 1
        nb_bg_hd = self.gagne_bas_gauche(i, j) + self.gagne_haut_droite(i, j) - 1
        nb_bd_hg = self.gagne_bas_droite(i, j) + self.gagne_haut_gauche(i, j) - 1
        if nb_ligne >= 4 or nb_colonne >= 4 or nb_bg_hd >= 4 or nb_bd_hg >= 4:
            self.fini = self.joueur

    def gagne_bas(self, i, j):
        if self.grille[i][j] != self.joueur:
            return 0
        if i + 1 > 5:
            return 1
        return self.gagne_bas(i + 1, j) + 1

    def gagne_haut(self, i, j):
        if self.grille[i][j] != self.joueur:
            return 0
        if i - 1 < 0:
            return 1
        return self.gagne_haut(i - 1, j) + 1

    def gagne_droite(self, i, j):
        if self.grille[i][j] != self.joueur:
            return 0
        if j + 1 > 6:
            return 1
        return self.gagne_droite(i, j + 1) + 1

    def gagne_gauche(self, i, j):
        if self.grille[i][j] != self.joueur:
            return 0
        if j - 1 < 0:
            return 1
        return self.gagne_gauche(i, j - 1) + 1

    def gagne_bas_droite(self, i, j):
        if self.grille[i][j] != self.joueur:
            return 0
        if i + 1 > 5 or j + 1 > 6:
            return 1
        return self.gagne_bas_droite(i + 1, j + 1) + 1

    def gagne_haut_gauche(self, i, j):
        if self.grille[i][j] != self.joueur:
            return 0
        if i - 1 < 0 or j - 1 < 0:
            return 1
        return self.gagne_haut_gauche(i - 1, j - 1) + 1

    def gagne_bas_gauche(self, i, j):
        if self.grille[i][j] != self.joueur:
            return 0
        if i + 1 > 5 or j - 1 < 0:
            return 1
        return self.gagne_bas_gauche(i + 1, j - 1) + 1

    def gagne_haut_droite(self, i, j):
        if self.grille[i][j] != self.joueur:
            return 0
        if i - 1 < 0 or j + 1 > 5:
            return 1
        return self.gagne_haut_droite(i - 1, j + 1) + 1

    def draw_paint(self):
        rect(0, 0, 500, 500, fill="blue")
        x = 15
        y = 50
        d = 60
        pas = 70
        # colors()
        for j in range(len(self.grille[0])):
            circle(pas // 2 + j * pas, 10, 20, fill_mouse_on=self.couleurs[self.joueur], command=self.click_colonne,
                   name=j,
                   fill="white")
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):
                circle(15 + j * pas, y + pas * i, d, fill=self.couleurs[self.grille[i][j]])
        if self.fini


if __name__ == '__main__':
    ihm = IhmScreen()


    def setup():
        createCanvas(800, 600)
        background("grey")
        ihm.init()
        # ajout du jeu dans l'ihm
        ihm.addObjet(MyGame(ihm, 50, 30))


    def compute():
        ihm.scan_events()


    def draw():
        ihm.draw()


    run(globals())
