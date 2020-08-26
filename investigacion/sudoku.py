import numpy as np

def possible(y, x, n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def solve() :
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        yield from solve()
                        grid[y][x] = 0
                return
    yield np.matrix(grid)
    
grid = [
    [0, 0, 0, 0, 8, 0, 7, 0, 0], 
    [8, 3, 2, 0, 5, 0, 0, 0, 0], 
    [7, 0, 5, 3, 9, 0, 0, 1, 0], 
    [0, 1, 3, 5, 0, 0, 8, 2, 0], 
    [2, 0, 0, 0, 3, 0, 0, 4, 9], 
    [9, 8, 0, 0, 0, 0, 0, 0, 0], 
    [0, 7, 0, 0, 0, 0, 0, 0, 0], 
    [4, 0, 9, 0, 6, 0, 1, 8, 5], 
    [0, 0, 1, 0, 0, 0, 0, 0, 0], 
]

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
]

s = solve()
print(next(s))