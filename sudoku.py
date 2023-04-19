from likeprocessing.processing import *
from copy import deepcopy

taillecase = 30
textFont("Comic sans ms", 20)
ihm = IhmScreen()


hardest_sudoku = [[8,0,0,0,0,0,0,0,0], [0,0,3,6,0,0,0,0,0], [0,7,0,0,9,0,2,0,0],
                  [0,5,0,0,0,7,0,0,0], [0,0,0,0,4,5,7,0,0], [0,0,0,1,0,0,0,3,0],
                  [0,0,1,0,0,0,0,6,8], [0,0,8,5,0,0,0,1,0], [0,9,0,0,0,0,4,0,0]]

plateau = deepcopy(hardest_sudoku)
plateau_depart = deepcopy(hardest_sudoku)
liste_chiffres = [1,2,3,4,5,6,7,8,9]

def setup():
    createCanvas(taillecase * 9, taillecase * (9 + 2))
    background("grey")
    textAlign("center", "center")

def place(case:tuple):
    global plateau
    i,j=case
    if plateau_depart[i][j] != 0:
        return False
    if keyIsPressed():
        if keyIsDown(K_1):
            plateau[i][j]=1
        if keyIsDown(K_2):
            plateau[i][j]=2
        if keyIsDown(K_3):
            plateau[i][j]=3
        if keyIsDown(K_4):
            plateau[i][j]=4
        if keyIsDown(K_5):
            plateau[i][j]=5
        if keyIsDown(K_6):
            plateau[i][j]=6
        if keyIsDown(K_7):
            plateau[i][j]=7
        if keyIsDown(K_8):
            plateau[i][j]=8
        if keyIsDown(K_9):
            plateau[i][j]=9
        if keyIsDown(K_BACKSPACE):
            plateau[i][j] = 0



def solveSudoku(grid : list[list], i : int=0, j : int=0):
    i, j = findNextCellToFill(grid)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
         # Undo the current cell for backtracking
    grid[i][j] = 0
    return False

def findNextCellToFill(grid: list[list],idebut:int=0, jdebut:int=0)-> tuple:
    for i in  range(idebut, len(grid)):
        for j in range(jdebut,len(grid[0])):
            if grid[i][j]== 0:
                return i,j
    return -1, -1

def rowOK(grid:list,i:int,e:int)->bool:
    for k in range(0,9):
        if grid[i][k]==e:
            return False
    return True

def columnOK(grid:list,j:int,e:int)->bool:
    for k in range(0,9):
        if grid[k][j]==e:
            return False
    return True

def sectorOK(grid:list,i:int,j:int,e:int)->bool:
    id=(i//3)*3
    jd=(j//3)*3
    for k in range(id,id+3):
        for l in range(jd,jd+3):
            if grid[k][l] == e:
                return False
    return True

def isValid(grid:list,i:int,j:int,e:int)->bool:
     return rowOK(grid,i,e) and columnOK(grid,j,e) and sectorOK(grid,i,j,e)

def print_sudoku(grid):
    ligne = "-"*25
    for i in range(9):
        if i%3==0:
            print(ligne)
        l="| "
        for j in range(9):
            l+=str(grid[i][j])+" "
            if j%3==2:
                l+="| "
        print(l)
    print(ligne)

def compute():
    if mouse_click_up() == 1:
        i, j = ((mouseY() // taillecase), (mouseX() // taillecase))
        if i <= 8 and j <= 8:
            place((i,j))


def draw():
    for j in range(9):
        for i in range(9):
            strokeWeight(1)
            if plateau[j][i] != 0:

                text(str(plateau[j][i]), taillecase * i, taillecase * j, taillecase, taillecase)
            else:
                text("", taillecase * i, taillecase * j, taillecase, taillecase)
    for i in range(3):
        strokeWeight(4)
        line(90*(i+1),0,90*(i+1),270)
        line(0, 90 * (i + 1), 270, 90 * (i + 1))

run(globals())

if __name__ == '__main__':
    solveSudoku(hardest_sudoku,0,0)
    print_sudoku(hardest_sudoku)
