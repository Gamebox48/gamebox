from likeprocessing.processing import *

class Cassetete:
    taillecase = 50
    nb_case_hauteur = 5
    nb_case_largeur = 5
    textFont("Comic sans ms", 20)
     = IhmScreen()

    @classmethod
    def setup(cls):
        createCanvas(cls.taillecase * cls.nb_case_largeur, cls.taillecase * (cls.nb_case_hauteur + 2))
        background("grey")
        textAlign("center", "center")
        cls.init_puzzle()

    @classmethod
    def move(case: tuple):
        i, j = case
        if i > cls.nb_case_hauteur or j > cls.nb_case_largeur:
            return False
        if i + 1 <= cls.nb_case_hauteur - 1 and cls.plateau[i + 1][j] == 0:
            plateau[i][j], plateau[i + 1][j] = plateau[i + 1][j], plateau[i][j]
            print("la case s'est déplacé en bas")
        elif i - 1 >= 0 and plateau[i - 1][j] == 0:
            plateau[i][j], plateau[i - 1][j] = plateau[i - 1][j], plateau[i][j]
            print("la case s'est déplacé en haut")
        elif j + 1 <= cls.nb_case_largeur - 1 and plateau[i][j + 1] == 0:
            cls.plateau[i][j], cls.plateau[i][j + 1] = cls.plateau[i][j + 1], cls.plateau[i][j]
            print("la case s'est déplacé à droite")
        elif j - 1 >= 0 and cls.plateau[i][j - 1] == 0:
            cls.plateau[i][j], cls.plateau[i][j - 1] = cls.plateau[i][j - 1], cls.plateau[i][j]
            print("la case s'est déplacé à gauche")
        else:
            return False
        cls.gagne()
        return True

    @classmethod
    def gagne(cls):
        global fini
        for i in range(cls.nb_case_hauteur):
            for j in range(cls.nb_case_largeur):
                if plateau[i][j] != i * cls.nb_case_largeur + j + 1 and cls.plateau[i][j] != 0:
                    return False
        fini = 2
        cls.objet_by_name('bouton_recommencer_fin').visible = True
        cls.objet_by_name('bouton_menu_fin').visible = True
        cls.objet_by_name('bouton_pause').visible = False
        return True


    def melange(self):
        c = 0
        while c < 100:
            i, j = randint(0, cls.nb_case_hauteur - 1), randint(0, cls.nb_case_largeur - 1)
            print(i, j)
            if cls.move((i, j)):
                c += 1

    @classmethod
    def pause(cls):
        global fini
        cls.objet_by_name('bouton_pause').visible = False
        cls.visibled(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause'])
        fini = 1

    @classmethod
    def reprendre(cls):
        global fini
        cls.objet_by_name('bouton_pause').visible = True
        cls.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause'])
        fini = 0

    @classmethod
    def init_puzzle(cls):
        cls.plateau = [[i * cls.nb_case_largeur + j + 1 for j in range(cls.nb_case_largeur)] for i in range(nb_case_hauteur)]
        cls.plateau[-1][-1] = 0
        cls.melange()
        cls.fini = 0

        cls.objet_by_name('bouton_pause').visible = True
        cls.unvisibleb(['bouton_reprendre', 'bouton_recommencer_pause', 'bouton_menu_pause', 'bouton_recommencer_fin',
                        'bouton_menu_fin'])


    cls.addObjet(Bouton(cls, (110, 310, 30, 30), '||', command=pause), 'bouton_pause')
    cls.addObjet(Bouton(cls, (110, 310, 30, 30), '||', command=reprendre, visible=False), 'bouton_reprendre')
    cls.addObjet(Bouton(cls, (0, 300, 110, 50), 'Recommencer', command=init_puzzle, visible=False),
                 'bouton_recommencer_pause')
    cls.addObjet(Bouton(cls, (140, 300, 110, 50), 'Retour au menu', command=init_puzzle, visible=False),
                 'bouton_menu_pause')
    cls.addObjet(Bouton(cls, (0, 300, 125, 50), 'Recommencer', command=init_puzzle, visible=False),
                 'bouton_recommencer_fin')
    cls.addObjet(Bouton(cls, (125, 300, 125, 50), 'Retour au menu', command=reprendre, visible=False), 'bouton_menu_fin')

    cls.fini = 0


    def compute(cls):
        if mouse_button_pressed() == 0:
            i, j = ((mouseY() // cls.taillecase), (mouseX() // cls.taillecase))
            if fini == 0:
                if i <= cls.nb_case_largeur - 1 and j <= cls.nb_case_hauteur - 1:
                    cls.move((i, j))
        cls.scan_events()


    def draw(cls):
        for j in range(cls.nb_case_largeur):
            for i in range(cls.nb_case_hauteur):
                if cls.plateau[j][i] != 0:
                    text(str(cls.plateau[j][i]), cls.taillecase * i, cls.taillecase * j, cls.taillecase, cls.taillecase)
        if cls.fini == 2:
            text('Bravo, vous avez gagné!', 0, 250, 250, 50)
        cls.draw()


    run(globals())
