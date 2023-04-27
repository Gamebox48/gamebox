from likeprocessing.processing import *


class MyGame(Dialog):
    def __init__(self, parent, x, y):
        """parent : ihm
        x, y : position du jeu dans l'ihm"""
        super().__init__(parent, (x, y, 500, 500), cadre=False)
        # 800, 575 : largeur et hauteur de la fenêtre du jeu
        # cadre = False supprime la barre de titre de la fenêtre du jeu
        # self.paint : objet de dessin de la fenêtre du jeu
        # les commandes de dessin likeprocessing seront placées dans la méthode self.draw_paint
        self.paint = Painter(self, (0, 0, 400, 300))
        self.paint.draw_paint = self.draw_paint
        # ajout de self.paint à la fenêtre du jeu
        self.addObjet(self.paint, "paint")
        # ajout de deux boutons par exemple
        self.addObjet(Bouton(self, (0, 0, 30, 20), "bp1", command=self.click_bp1), "bp1")
        self.addObjet(Bouton(self, (0, 0, 30, 20), "bp2", command=self.click_bp2), "bp2")
        self.pack(["paint", ["bp1", "bp2"]])

        # variable du jeux
        self.compteur = 0

    def click_bp1(self):
        # code à exécuter lors de l'appuie sur bp1
        print("bp1")

    def click_bp2(self):
        # code à exécuter lors de l'appuie sur bp2
        print("bp2")

    def compute(self):
        # ici ce trouve de code pour les calculs du jeu
        self.compteur += 1
        if self.compteur >= 1000:
            self.compteur = 0

    def scan_mouse(self):
        # cette méthode permet d'excuter la méthode compute à chaque fois que
        # l'instruction ihm.scan_events() sera exécutée
        super().scan_mouse()
        self.compute()

    def draw_paint(self):
        text(f"valeur du compteur {self.compteur}", 30, 50)


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
