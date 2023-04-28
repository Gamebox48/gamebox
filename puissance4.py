from likeprocessing.processing import*

grille=[[0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]]

couleurs = ['white','red','orange']
joueur = 1
def setup():
    createCanvas(1200, 600)
    background('blue')

# def colors():
#     global couleur
#     textFont('comic_sans_ms',30)
#     if couleur == 'yellow':
#         text('à "joueur 2" de jouer', 850, 280)
#     if couleur == 'red':
#         text('à "joueur 1" de jouer', 850, 280)
#         if mouse_click_down():
#             couleur = 'yellow'
#     else:
#         if mouse_click_down():
#             couleur = 'red'
    # fill_mouse_on(couleur)

def click_colonne(name):
    global grille,joueur
    print(name)
    for i in range(len(grille)):
        if grille[i][name]>0:
            grille[i-1][name]=joueur
            break
        elif i==len(grille)-1:
            grille[i][name]=joueur
            break
    joueur = (joueur%2)+1

def draw():
    x = 15
    y = 50
    d = 80
    pas = 90
    # colors()
    for j in range(len(grille[0])):
        circle(pas//2 + j * pas, 10, 20, fill_mouse_on=couleurs[joueur], command=click_colonne, name=j, fill="white")
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            circle(15+j*pas,y+pas*i,d,fill=couleurs[grille[i][j]])






run(globals())
