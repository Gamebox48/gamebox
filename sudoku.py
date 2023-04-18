hardest_sudoku = [[8,0,0,0,0,0,0,0,0], [0,0,3,6,0,0,0,0,0], [0,7,0,0,9,0,2,0,0],
                  [0,5,0,0,0,7,0,0,0], [0,0,0,0,4,5,7,0,0], [0,0,0,1,0,0,0,3,0],
                  [0,0,1,0,0,0,0,6,8], [0,0,8,5,0,0,0,1,0], [0,9,0,0,0,0,4,0,0]]

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


if __name__ == '__main__':
    solveSudoku(hardest_sudoku,0,0)
    print_sudoku(hardest_sudoku)
