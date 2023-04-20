from likeprocessing.processing import*

grille=[[" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "]]


def setup():
    createCanvas(1200, 600)
    background('blue')


def draw():
    x = 15
    y = 4
    d=90
    tour = 0
    for i in grille:
        if tour%2==0:
            couleur = 'red'
        else:
            couleur = 'yellow'
        for cercle in grille[0]:
            circle(x,y,d,fill_mouse_on=couleur)
            x = x+120
        x = 15
        y = y+100





run(globals())
