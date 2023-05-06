from likeprocessing.processing import *
from random import shuffle, randint

from likeprocessing.tempos import Monostable
from os import getcwd

class Memory(Dialog):

    def __init__(self, parent, x, y):
        super().__init__(parent, (x, y, 800, 575), cadre=False)
        self.images: list[Image] = []
        self.plateau: list[list[int]] = []
        self.carte1: tuple[int, int] = None
        self.carte2: tuple[int, int] = None
        self.montrer: bool = True
        self.tempo: Monostable = Monostable(2000)
        self.joueurs: list[list[Union[int, str]]] = [[0, "joueur 1 "], [0, "joueur 2 "]]
        self.joueur_courant: int = 0
        self.nombre_joueur: int = 1
        self.niveaux: list[tuple[int, int]] = [(2, 5), (4, 5), (5, 8)]
        self.niveau: int = 0
        self.ecran: int = 1
        self.init_ecran_1()
        self.fond = None
        self.charge_image((96, 96))
        self.pas = 100
        self.creer_background()

    def charge_image(self, taille: tuple[int, int]):
        """charge, redimensionne les images et les place dans une liste."""
        liste_image: list[Image] = []
        path = getcwd().replace("\\","/")
        last_dir = path.split("/")[-1]
        if last_dir !="memory":
            path+="/memory"
        for i in range(44):
            img = loadImage(f"{path}/memory/{i}.png")
            liste_image.append(resize_image(img, taille))
        self.images = liste_image

    def draw_plateau(self, lignes, colonnes):
        """affiche les cartes du jeu en fonction de l'état de carte1 et carte2."""
        noStroke()
        dx = (self.width - self.pas * colonnes)//2
        dy = (self.height - self.pas * lignes)//2
        for i in range(lignes):
            for j in range(colonnes):
                if self.carte1 == (i, j) or self.carte2 == (i, j):
                    img = self.images[self.plateau[i][j]]
                else:
                    img = self.images[0]
                if self.plateau[i][j] != 0:
                    if self.carte2 is None:
                        rect(dx + j * self.pas, dy + i * self.pas, self.pas-4, self.pas-4, image=img, name=(i, j), command=self.click_on,
                             allign_v="center", allign_h="center", no_stoke=True)
                    else:
                        rect(dx + j * self.pas, dy + i * self.pas, self.pas-4, self.pas-4, image=img, name=(i, j),
                             allign_v="center", allign_h="center", no_stoke=True)

    def init_plateau(self, lignes, colonnes) -> list[list[int]]:
        """créer un plateau de jeu de 5x8 dont les cartes sont mélangées."""
        maxi = lignes * colonnes//2
        p = [i for i in range(1, 44)]
        shuffle(p)
        p = p[:maxi]
        paires = []
        for i in range(maxi):
            paires.append(p[i])
            paires.append(p[i])
        shuffle(paires)
        # p = [max(i // 2, i % 2) for i in range(2, maxi)]

        p = [[paires[i * colonnes + j] for j in range(colonnes)] for i in range(lignes)]
        self.plateau = p
        return p

    def plateau_vide(self, lignes, colonnes) -> bool:
        """retourne True si le plateau est vide
        (toutes les cases de plateau sont égales à 0"""
        for i in range(lignes):
            for j in range(colonnes):
                if self.plateau[i][j] != 0:
                    return False
        return True

    def paire_gagnante(self, carte_une: [tuple, None], carte_deux: [tuple, None]) -> bool:
        """retourne True si les deux cartes sont identiques et False dans le cas contraire"""
        if carte_une is None or carte_deux is None:
            return False
        return self.plateau[carte_une[0]][carte_une[1]] == self.plateau[carte_deux[0]][carte_deux[1]]

    def draw_ecran2(self):
        """affiche l'écran 2"""
        image(self.fond, 1, 1)
        self.draw_plateau(*self.niveaux[self.niveau])

    def draw_ecran1(self):
        """ affiche l'écran 1"""
        image(self.fond, 1, 1)

    def creer_background(self):
        """crée un fond avec les cartes du memory placées au hasard"""
        rect(0, 0, self.width, self.height, fill="#F6DE7B", no_stroke=True)
        t = [i for i in range(1, 21)]
        shuffle(t)
        am = angleMode("deg")
        pos = []
        for i in range(20):
            x, y = randint(0, self.width // 100) * 100, randint(0, self.height // 100) * 100
            while (x, y) in pos:
                x, y = randint(1, self.width // 100 - 1) * 100, randint(1, self.height // 100 - 1) * 100
            pos.append((x, y))
            angle = (15 * i) % 360
            rotate(angle, (x, y))
            image(self.images[t[i]], x, y)
        angleMode(am)
        self.fond = screen.copy().subsurface((1, 1, self.width - 2, self.height - 2))

    def click_on(self, valeur):
        """Traite l'action du clic sur une carte"""
        # if montrer:
        if self.carte1 is None:
            self.carte1 = valeur
        elif valeur != self.carte1:
            self.carte2 = valeur
            self.montrer = False
            # quand deux carte ont été tirées une tempo de 2s secondes est lancée
            self.tempo.reset()

    def init_ecran_1(self):

        def bp_plus_moins(valeur):
            niveaux = ["facile", "moyen", "difficile"]
            if valeur[1] == 0:
                if valeur[0] == "+":
                    self.niveau = min(self.niveau + 1, 2)
                else:
                    self.niveau = max(self.niveau - 1, 0)
                self.objet_by_name("pm0").text(f"Difficulté : {niveaux[self.niveau]}")
            else:
                if valeur[0] == "+":
                    self.nombre_joueur = min(self.nombre_joueur + 1, 4)
                else:
                    self.nombre_joueur = max(self.nombre_joueur - 1, 1)
                self.objet_by_name("pm1").text(f"Nombre de joueurs : {self.nombre_joueur}")
                for i in range(4):
                    if i < self.nombre_joueur:
                        self.visibled(f"j{i}")
                    else:
                        self.unvisibleb(f"j{i}")
                self.aligne_h(["bp_start"], posy=self.objet_by_name(f"j{self.nombre_joueur - 1}").bottom + 20)

        def bp_start():
            self.joueur_courant = 0
            self.joueurs = []
            if self.niveau == 2:
                self.pas = 70
            else:
                self.pas = 100
            self.charge_image((self.pas - 4, self.pas - 4))
            for i in range(self.nombre_joueur):
                self.joueurs.append([0, self.objet_by_name(f"j{i}").text()])
            self.init_ecran_2()
            self.ecran = 2
            self.plateau = self.init_plateau(*self.niveaux[self.niveau])

        self.init()
        paint = Painter(self, (0, 0, self.width, self.height))
        paint.draw_paint = self.draw_ecran1
        self.addObjet(paint, "paint")
        self.addObjet(Label(self, (10, 10), "Memory", font="arial", font_color="black", font_size=72))
        for i, t in enumerate(["Difficulté : Facile    ", f"Nombre de joueurs : {self.nombre_joueur}"]):
            self.addObjet(Label(self, (10, 100, 340), t, font="arial", font_color="black", font_size=32), f"pm{i}")
            self.addObjet(Bouton(self, (10, 10, 40, 20), "-", font="arial", font_color="black", font_size=28,
                                 command=lambda v=("-", i): bp_plus_moins(v)))
            self.addObjet(Bouton(self, (10, 10, 40, 40), "+", font="arial", font_color="black", font_size=28,
                                 command=lambda v=("+", i): bp_plus_moins(v)))
        for i in range(4):
            self.addObjet(
                LineEdit(self, (0, 0, 424, 40), f"joueur {i + 1}", font="arial", font_color="black", font_size=20),
                f"j{i}")
        self.addObjet(Bouton(ihm, (0, 0, 200, 0), "Démarrer la partie",
                             font="arial", font_color="black", font_size=20, command=bp_start), "bp_start")
        self.pack(["obj_1",
                   ["pm0", "obj_2", "obj_3"],
                   ["pm1", "obj_4", "obj_5"],
                   "j0", "j1", "j2", "j3", "bp_start"])
        self.visibled("all")
        self.unvisibleb([f"j{i}" for i in range(self.nombre_joueur, 4)])
        self.aligne_h(["bp_start"], posy=self.objet_by_name(f"j{self.nombre_joueur - 1}").bottom + 20)

    def init_ecran_2(self):
        self.init()
        paint = Painter(self, (0, 0, self.width, self.height))
        paint.draw_paint = self.draw_ecran2
        self.addObjet(paint, "paint")
        for i in range(self.nombre_joueur):
            self.addObjet(Label(self, (10 + i * 200, 10, 200, 30),
                                f"{self.joueurs[i][1]}: {self.joueurs[i][0]}", font_size=20), f"j{i}")

    def init_ecran_3(self):

        def bp_rejouer():
            self.ecran = 1
            self.init_ecran_1()

        def bp_quitter():
            if AskYesNo(self.parent, "Voulez-vous Vraiment\nquitter le jeu").response() == 0:
                self.quitter()

        self.init()
        paint = Painter(self, (0, 0, self.width, self.height))
        paint.draw_paint = self.draw_ecran1
        self.addObjet(paint, "paint")
        self.addObjet(Label(ihm, (10, 10), "Memory", font_size=72))
        self.addObjet(Label(ihm, (10, 10), "Classement général", font_size=50))
        j = sorted(self.joueurs, reverse=True, key=lambda x: x[0])
        for i in range(self.nombre_joueur):
            self.addObjet(Label(self, (10 + i * 200, 10, 200, 30),
                                f"{j[i][1]}: {j[i][0]}", font_size=35, align_h="center"))
        self.pack([f"obj_{i + 1}" for i in range(2 + self.nombre_joueur)], pady=30)
        self.addObjet(Bouton(self, (0, 0, 100, 0), "Rejouer",
                             font_size=20, command=bp_rejouer), "bp_rejouer")
        self.addObjet(Bouton(self, (0, 0, 100, 0), "Quitter",
                             font_size=20, command=bp_quitter), "bp_quitter")
        self.aligne_h(["bp_rejouer", "bp_quitter"],
                      posy=self.objet_by_name(f"obj_{self.nombre_joueur + 2}").bottom + 20, padx=20)

    def refresh_score(self):
        for i in range(self.nombre_joueur):
            self.objet_by_name(f"j{i}").text(f"{self.joueurs[i][1]}: {self.joueurs[i][0]}")
            if i == self.joueur_courant:
                self.objet_by_name(f"j{i}").fill = "orange"
            else:
                self.objet_by_name(f"j{i}").fill = None

    def compute(self):
        if self.ecran == 2:
            if self.tempo.fin():
                if self.paire_gagnante(self.carte1, self.carte2):
                    self.plateau[self.carte1[0]][self.carte1[1]] = 0
                    self.plateau[self.carte2[0]][self.carte2[1]] = 0
                    self.joueurs[self.joueur_courant][0] += 1
                else:
                    self.joueur_courant = (self.joueur_courant + 1) % self.nombre_joueur
                self.carte1 = None
                self.carte2 = None
                self.montrer = True

            self.refresh_score()
            if self.plateau_vide(*self.niveaux[self.niveau]):
                self.ecran = 3
                self.init_ecran_3()


if __name__ == '__main__':
    ihm = IhmScreen()
    memory: Memory


    def exit():
        if AskYesNo(ihm, "Voulez-vous Vraiment\nquitter le jeu").response() == 0:
            set_quit(True)


    def setup():
        global memory
        createCanvas(1200, 900)
        ihm.init()
        memory = Memory(ihm, 200, 100)
        fill("#F6DE7B")
        noStroke()
        # fill_mouse_on("red")
        title("Memory")
        ihm.addObjet(memory)


    def compute():
        memory.compute()
        ihm.scan_events()


    def draw():
        ihm.draw()


    run(globals())
