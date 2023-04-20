"""programme de base"""
from likeprocessing.processing import *
from random import shuffle


class Snake:
    x, y, width, height = (405, 45, 735, 522)
    head_x, head_y = 100, 100
    tempo = Tempo(100)
    vitesse_x = 10
    vitesse_y = 0
    serpent = []
    perdu = False
    nourriture = []

    @classmethod
    def init_nourriture(cls, n=10) -> list:
        posx = [i for i in range(10, cls.width, 10)]
        shuffle(posx)
        posy = [i for i in range(10, cls.height, 10)]
        shuffle(posy)
        return [(posx[i], posy[i]) for i in range(n)]

    @classmethod
    def init_snake(cls):
        cls.nourriture = cls.init_nourriture(20)
        cls.serpent = [(cls.head_x - 10 * i, cls.head_y) for i in range(1)]

    @classmethod
    def compute(cls):

        # global x, y, vitesse_x, vitesse_y, serpent, perdu,nourriture
        if cls.tempo.fin() and cls.perdu == False:
            cls.head_x += cls.vitesse_x
            cls.head_y += cls.vitesse_y
            if (cls.head_x, cls.head_y) in cls.serpent[:-1]:
                cls.perdu = True
            elif (cls.head_x, cls.head_y) in cls.nourriture:
                cls.serpent = [(cls.head_x, cls.head_y)] + cls.serpent
                cls.nourriture.remove((cls.head_x, cls.head_y))
                if len(cls.nourriture) == 0:
                    cls.nourriture = cls.init_nourriture(20)
            else:
                cls.serpent = [(cls.head_x, cls.head_y)] + cls.serpent[:-1]
            if cls.vitesse_x != 0:
                if cls.head_x >= cls.width:
                    cls.head_x = 0
                elif cls.head_x <= 5:
                    cls.head_x = cls.width
            else:
                if cls.head_y >= cls.height:
                    cls.head_y = 0
                elif cls.head_y <= 5:
                    cls.head_y = cls.height

        if keyIsPressed():
            if keyIsDown(K_RIGHT) and cls.vitesse_x == 0:
                cls.vitesse_x = 10
                cls.vitesse_y = 0
            elif keyIsDown(K_LEFT) and cls.vitesse_x == 0:
                cls.vitesse_x = -10
                cls.vitesse_y = 0
            elif keyIsDown(K_DOWN) and cls.vitesse_y == 0:
                cls.vitesse_y = 10
                cls.vitesse_x = 0
            elif keyIsDown(K_UP) and cls.vitesse_y == 0:
                cls.vitesse_y = -10
                cls.vitesse_x = 0

    @classmethod
    def draw(cls):
        translate(cls.x, cls.y)
        rect(-5, 0, cls.width, cls.height, stroke_weight=5)
        for i in range(len(cls.nourriture)):
            circle(cls.nourriture[i][0], cls.nourriture[i][1], 10, fill="green", ellipse_mode="center")
        for i in range(len(cls.serpent)):
            rect(cls.serpent[i][0], cls.serpent[i][1], 10, 10, fill="red", rect_mode="center")
        if cls.perdu:
            text("Tu as perdu", 0, cls.height / 2 - 25, 400, 50, font_size=50, align_h="center", no_fill=True,
                 no_stroke=True)
        text(str(len(cls.serpent) * 10), 10, -45, no_stroke=True, no_fill=True,font_size=20)
        # rect(0, 0, cls.width, cls.height, stroke_weight=10,no_fill=True)


if __name__ == '__main__':
    def setup():
        createCanvas(800, 600)
        background("grey")
        Snake.init_snake()


    def compute():
        Snake.compute()


    def draw():
        Snake.draw()

    run(globals())
