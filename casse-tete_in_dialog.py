from likeprocessing.processing import *

ihm = IhmScreen()


class CasseTete(Dialog):
    taillecase = 50
    nb_case_hauteur = 5
    nb_case_largeur = 5

    def __init__(self, parent, posx, posy):
        super().__init__(parent,
                         (posx, posy, CasseTete.taillecase * CasseTete.nb_case_largeur+4,
                          CasseTete.taillecase * (CasseTete.nb_case_hauteur + 2)))
        self.paint = Painter(self, (
            1, 0, CasseTete.taillecase * CasseTete.nb_case_largeur+1,
            CasseTete.taillecase * CasseTete.nb_case_hauteur+1))
        self.paint.draw_paint = self.draw_paint
        self.addObjet(self.paint)
        self.addObjet(Bouton(self, (111, 310, 30, 30), '||', command=self.pause), 'bouton_pause')
        self.addObjet(Bouton(self, (111, 310, 30, 30), '||', command=self.reprendre, visible=False), 'bouton_reprendre')
        self.addObjet(Bouton(self, (1, 300, 110, 50), 'Recommencer', command=self.init_puzzle, visible=False),
                      'bouton_recommencer_pause')
        self.addObjet(Bouton(self, (140, 300, 110, 50), 'Retour au menu', command=self.init_puzzle, visible=False),
                      'bouton_menu_pause')
        self.addObjet(Bouton(self, (2, 300, 125, 50), 'Recommencer', command=self.init_puzzle, visible=False),
                      'bouton_recommencer_fin')
        self.addObjet(Bouton(self, (126, 300, 125, 50), 'Retour au menu', command=self.reprendre, visible=False),
                      'bouton_menu_fin')
        self.ajuste(1)
        self.fini = 0
        self.plateau = []
        self.init_puzzle()
        textFont("Comic sans ms", 20)
        textAlign("center", "center")

    def mouse_x_paint(self):
        """retourne la position x de la souris dans le repère de paint"""
        return mouseX()-self.paint.absolute()[0]

    def mouse_y_paint(self):
        """retourne la position y de la souris dans le repère de paint"""
        return mouseY()-self.paint.absolute()[1]

    def init_puzzle(self):
        self.plateau = [[i * CasseTete.nb_case_largeur + j + 1 for j in range(CasseTete.nb_case_largeur)] for i in
                        range(CasseTete.nb_case_hauteur)]
        self.plateau[-1][-1] = 0
        self.melange()
        self.fini = 0
        self.title = f" progression {self.gagne()}%"
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause', 'bouton_recommencer_fin',
                        'bouton_menu_fin'])


    def move_case(self, case: tuple):
        i, j = case
        if i > CasseTete.nb_case_hauteur or j > CasseTete.nb_case_largeur:
            return False
        if i + 1 <= CasseTete.nb_case_hauteur - 1 and self.plateau[i + 1][j] == 0:
            self.plateau[i][j], self.plateau[i + 1][j] = self.plateau[i + 1][j], self.plateau[i][j]
            print("la case s'est déplacé en bas")
        elif i - 1 >= 0 and self.plateau[i - 1][j] == 0:
            self.plateau[i][j], self.plateau[i - 1][j] = self.plateau[i - 1][j], self.plateau[i][j]
            print("la case s'est déplacé en haut")
        elif j + 1 <= CasseTete.nb_case_largeur - 1 and self.plateau[i][j + 1] == 0:
            self.plateau[i][j], self.plateau[i][j + 1] = self.plateau[i][j + 1], self.plateau[i][j]
            print("la case s'est déplacé à droite")
        elif j - 1 >= 0 and self.plateau[i][j - 1] == 0:
            self.plateau[i][j], self.plateau[i][j - 1] = self.plateau[i][j - 1], self.plateau[i][j]
            print("la case s'est déplacé à gauche")
        else:
            return False
        return True

    def gagne(self):
        score = 0
        for i in range(CasseTete.nb_case_hauteur):
            for j in range(CasseTete.nb_case_largeur):
                if self.plateau[i][j] == i * CasseTete.nb_case_largeur + j + 1:
                    # return False
                    score+=1
        # self.fini = 2
        # self.objet_by_name('bouton_recommencer_fin').visible = True
        # self.objet_by_name('bouton_menu_fin').visible = True
        # self.objet_by_name('bouton_pause').visible = False
        # return True
        return int(score * 100 / (CasseTete.nb_case_hauteur * CasseTete.nb_case_largeur-1))

    def melange(self):
        c = 0
        while c < 10:
            i, j = randint(0, CasseTete.nb_case_hauteur - 1), randint(0, CasseTete.nb_case_largeur - 1)
            print(i, j)
            if self.move_case((i, j)):
                c += 1

    def pause(self):
        self.objet_by_name('bouton_pause').visible = False
        self.visibled(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause'])
        self.fini = 1

    def reprendre(self):
        self.objet_by_name('bouton_pause').visible = True
        self.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause'])
        self.fini = 0

    def scan_mouse(self):
        if mouse_button_pressed() == 0:
            i, j = ((self.mouse_y_paint() // CasseTete.taillecase), (self.mouse_x_paint() // CasseTete.taillecase))
            if self.fini == 0:
                if i <= CasseTete.nb_case_largeur - 1 and j <= CasseTete.nb_case_hauteur - 1:
                    self.move_case((i, j))
            score = self.gagne()
            self.title = f" progression {score}%"
            if score == 100:
                self.fini = 2
                self.objet_by_name('bouton_recommencer_fin').visible = True
                self.objet_by_name('bouton_menu_fin').visible = True
                self.objet_by_name('bouton_pause').visible = False
        super().scan_mouse()

    def draw_paint(self):
        for j in range(CasseTete.nb_case_largeur):
            for i in range(CasseTete.nb_case_hauteur):
                if self.plateau[j][i] != 0:
                    text(str(self.plateau[j][i]), CasseTete.taillecase * i, CasseTete.taillecase * j,
                         CasseTete.taillecase, CasseTete.taillecase)
        if self.fini == 2:
            text('Bravo, vous avez gagné!', 0, 250, 250, 50)


if __name__ == '__main__':
    ihm = IhmScreen()


    def setup():
        createCanvas(400, 400)
        background("grey")
        ihm.init()
        ihm.addObjet(CasseTete(ihm, 50, 10))


    def compute():
        ihm.scan_events()


    def draw():
        ihm.draw()


    run(globals())
