plateau=[["","",""],["","",""],["","",""]]

def recherche(liste):
    for i in liste:
        for j in liste[i]:
            if j=="":
                return True
    return False


def morpion(x,y,tour):
    global taillecase,plateau
    for i in range(4):
        jouer=0
        while jouer!=1:
            print(f'{plateau[0]}\n{plateau[1]}\n{plateau[2]}')
            print(f'Au joueur {tour} de jouer.')
            v = y,x
            if plateau[int(y)][int(x)] =="":
                plateau[int(y)][int(x)] = tour
                jouer=1
                if tour == 1:
                    fill("blue")
                    rect((x+1)*taillecase//2,(y+1)*taillecase//2,80,80)
                else:
                    fill("red")
                    circle((x+1)*taillecase//2,(y+1)*taillecase//2,80)
            else:
                print("Cette case est déja prise")
        for j in range(len(plateau)):
            if plateau[j][0]==tour and plateau[j][1]==tour and plateau[j][2]==tour or plateau[0][j] == tour and plateau[1][j] == tour and plateau[2][j] == tour:
                print(f"joueur {tour} à gagné")
                return True
        if plateau[0][0]==tour and plateau[1][1]==tour and plateau[2][2]==tour or plateau[2][0]==tour and plateau[1][1]==tour and plateau[0][2]==tour:
            print(f"joueur {tour} à gagné")
            return True



while recherche(plateau)==True:
    morpion(,)
