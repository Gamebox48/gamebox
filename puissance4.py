from likeprocessing.processing import*

grille=[["0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0"]]

couleur = 'red'

def setup():
    createCanvas(1200, 600)
    background('blue')

def colors():
    global couleur
    textFont('comic_sans_ms',30)
    if couleur == 'yellow':
        text('à "joueur 2" de jouer', 850, 280)
    if couleur == 'red':
        text('à "joueur 1" de jouer', 850, 280)
        if mouse_click_down():
            couleur = 'yellow'
    else:
        if mouse_click_down():
            couleur = 'red'
    fill_mouse_on(couleur)

def draw():
    x = 15
    y = 4
    d = 90
    colors()
    for i in grille:
        for cercle in grille[0]:
            circle(x,y,d)
            x = x+120
        x = 15
        y = y+100





run(globals())
