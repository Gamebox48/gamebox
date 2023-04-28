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
        self.addObjet(Bouton(self, (0, 0, 30, 20), "bp1", command=self.click_bp1), "bp1")
        self.addObjet(Bouton(self, (0, 0, 30, 20), "bp2", command=self.click_bp2), "bp2")
        self.pack(["paint", ["bp1", "bp2"]])

        # variable du jeux
        self.grille = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]

        self.couleurs = ['white', 'red', 'orange']
        self.joueur = 1

    def click_bp1(self):
        # code à exécuter lors de l'appuie sur bp1
        print("bp1")

    def click_bp2(self):
        # code à exécuter lors de l'appuie sur bp2
        print("bp2")

    def compute(self):
        # ici ce trouve de code pour les calculs du jeu
        pass

    def scan_mouse(self):
        # cette méthode permet d'excuter la méthode compute à chaque fois que
        # l'instruction ihm.scan_events() sera exécutée
        super().scan_mouse()
        self.compute()

    def click_colonne(self,name):
        for i in range(len(self.grille)):
            if self.grille[i][name] > 0:
                self.grille[i - 1][name] = self.joueur
                break
            elif i == len(self.grille) - 1:
                self.grille[i][name] = self.joueur
                break
        self.joueur = (self.joueur % 2) + 1

    def draw_paint(self):
        rect(0,0,500,500,fill="blue")
        x = 15
        y = 50
        d = 60
        pas = 70
        # colors()
        for j in range(len(self.grille[0])):
            circle(pas // 2 + j * pas, 10, 20, fill_mouse_on=self.couleurs[self.joueur], command=self.click_colonne, name=j,
                   fill="white")
        for i in range(len(self.grille)):
            for j in range(len(self.grille[0])):
                circle(15 + j * pas, y + pas * i, d, fill=self.couleurs[self.grille[i][j]])


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
