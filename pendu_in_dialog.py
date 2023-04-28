from likeprocessing.processing import *
import random

ihm = IhmScreen()


class Pendu(Dialog):
    def __init__(self, parent, x, y):
        """parent : ihm
        x, y : position du jeu dans l'ihm"""
        super().__init__(parent, (x, y, 600, 600), cadre=False)
        # 800, 575 : largeur et hauteur de la fenêtre du jeu
        # cadre = False supprime la barre de titre de la fenêtre du jeu
        # variable du programme
        self.nb_essai = 0
        informatique = ["python", "ordinateur", "programmation", "algorithmique", "intelligence"]
        nature = ["paysage", "environnement", "arbre", "fleur", "montagne"]
        self.themes = [informatique, nature, ]
        self.mots = random.choice(self.themes)
        self.mot_secret = random.choice(self.mots).upper()
        self.vies = 11
        self.lettres_utilisees = []
        self.perdu = False
        self.gagne = False


        # self.paint : objet de dessin de la fenêtre du jeu
        # les commandes de dessin likeprocessing seront placées dans la méthode self.draw_paint
        self.paint = Painter(self, (0, 0, 600, 400))
        self.paint.draw_paint = self.draw_pendu
        # ajout de self.paint à la fenêtre du jeu
        self.addObjet(self.paint, "paint")
        self.creation_interface()

    def draw_pendu(self):
        textAlign("center", "center")
        ellipseMode('Center')
        pendu = [(100*0.9, 430*0.9, 700*0.9, 430*0.9),
                 (200*0.9, 430*0.9, 200*0.9, 50*0.9),
                 (200*0.9, 50*0.9, 450*0.9, 50*0.9),
                 (200*0.9, 140*0.9, 300*0.9, 50*0.9),
                 (450*0.9, 50*0.9, 450*0.9, 130*0.9),
                 (450*0.9, 130*0.9, 85*0.9),
                 (450*0.9, 172*0.9, 450*0.9, 300*0.9),
                 (450*0.9, 300*0.9, 515*0.9, 380*0.9),
                 (450*0.9, 300*0.9, 385*0.9, 380*0.9),
                 (450*0.9, 200*0.9, 515*0.9, 250*0.9),
                 (450*0.9, 200*0.9, 385*0.9, 250*0.9)]

        # déplace le dessin de 40px vers la droite et 50 pixels vers le bas
        translate(-60, 0)
        for i in range(self.nb_essai):
            if i != 5:
                line(*pendu[i])
            else:
                circle(*pendu[5])
        translate(90, 0)
        if self.gagne:
            text("Bravo, vous avez gagné !", 0, 300, 600, 40, align_v="center", align_h="center", font="consolas",
                 font_size=20)
        if self.perdu:
            text("Dommage, vous avez perdu !", 0, 300, 600, 40, align_v="center", align_h="center", font="consolas",
                 font_size=20)

    def creation_interface(self):
        touches = ["AZERTYUIOP", "QSDFGHJKLM", "WXCVBN"]
        # label mot secret
        self.addObjet(
            Label(self, (0, 0, 400, 30), "_ " * len(self.mot_secret), font="consolas", font_size=20, align_h="center"),
            "mot_secret")
        for i in range(len(touches)):
            for j in range(len(touches[i])):
                self.addObjet(Bouton(self, (100 + i * 20 + 40 * j, 420 + i * 40, 40, 40), touches[i][j],
                                     command=self.click_touche, name=touches[i][j]), touches[i][j])

    def click_touche(self, name):
        if name not in self.lettres_utilisees:
            self.lettres_utilisees.append(name)
        affiche_mot = ""
        for c in self.mot_secret:
            if c in self.lettres_utilisees:
                affiche_mot += f"{c} "
            else:
                affiche_mot += f"_ "
        self.objet_by_name("mot_secret").text(affiche_mot)
        for c in self.lettres_utilisees:
            self.objet_by_name(c).disabled = True
        if name not in self.mot_secret:
            self.nb_essai = borner(self.nb_essai + 1, 0, self.vies)
        if affiche_mot.replace(" ", "") == self.mot_secret:
            self.gagne = True
        if self.nb_essai == self.vies:
            self.perdu = True

    def scan_mouse(self):
        # cette méthode permet d'excuter la méthode compute à chaque fois que
        # l'instruction ihm.scan_events() sera exécutée
        super().scan_mouse()
        self.compute()

    def compute(self):
        pass


if __name__ == '__main__':
    ihm = IhmScreen()


    def setup():
        createCanvas(800, 600)
        background("grey")
        ihm.init()
        # ajout du jeu dans l'ihm
        ihm.addObjet(Pendu(ihm, 50, 30))


    def compute():
        ihm.scan_events()


    def draw():
        ihm.draw()


    run(globals())
