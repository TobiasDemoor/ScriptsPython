import numpy

class Pos:
    def __init__(self, xInit=0, yInit=0):
        self.xInit = xInit
        self.yInit = yInit
        self.x = xInit
        self.y = yInit
        self.xCuad = None
        self.yCuad = None

    def __encuentroXCuad(self):
        if self.x < 3:
            self.xCuad = 0
        elif self.x < 6:
            self.xCuad = 3
        else:
            self.xCuad = 6

    def __encuentroYCuad(self):
        if self.y < 3:
            self.yCuad = 0
        elif self.y < 6:
            self.yCuad = 3
        else:
            self.yCuad = 6

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def incrX(self):
        self.x += 1

    def incrY(self):
        self.y += 1

    def getXCuad(self):
        if self.xCuad is None:
            self.__encuentroXCuad()
        return self.xCuad

    def getYCuad(self):
        if self.yCuad is None:
            self.__encuentroYCuad()
        return self.yCuad

    def reset(self):
        self.x = self.xInit
        self.y = self.yInit


class Sudoku:
    def __init__(self, mat):
        self.matRes = mat

    def getVal(self, x, y):
        return self.matRes[x][y]

    def setVal(self, x, y, val):
        self.matRes[x][y] = val


class ResuelveSudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.matPosb = numpy.ones((9, 9, 9))
        self.recorridos = {
            1: self.__horizontal1,
            2: self.__vertical1,
            3: self.__cuadrado1,
            4: self.__horizontal2,
            5: self.__vertical2,
            6: self.__cuadrado2,
        }

    def __buscoVacio(self, pos):
        corte = False
        if pos.getY() < 8:
            pos.incrY()
        elif pos.getX() < 8:
            pos.setY(0)
            pos.incrX()
        else:
            corte = True
        while self.sudoku.getVal(pos.getX(), pos.getY()) != 0 and not corte:
            if pos.getY() < 8:
                pos.incrY()
            elif pos.getX() < 8:
                pos.setY(0)
                pos.incrX()
            else:
                corte = True
        return corte

    def __horizontal1(self, pos):
        for k in range(9):
            if self.sudoku.getVal(pos.getX(), k) != 0:
                self.matPosb[pos.getX()][pos.getY()][self.sudoku.getVal(
                    pos.getX(), k) - 1] = 0

    def __vertical1(self, pos):
        for k in range(9):
            if self.sudoku.getVal(k, pos.getY()) != 0:
                self.matPosb[pos.getX()][pos.getY()][self.sudoku.getVal(
                    k, pos.getY()) - 1] = 0

    def __cuadrado1(self, pos):
        for i in range(3):
            for j in range(3):
                if self.sudoku.getVal(pos.getXCuad() + i, pos.getYCuad() + j) != 0:
                    self.matPosb[pos.getX()][pos.getY()][self.sudoku.getVal(
                        pos.getXCuad() + i, pos.getYCuad() + j) - 1] = 0

    def __actualizoAux(self, pos):
        self.matPosb[pos.getX()][pos.getY()] = numpy.zeros(9)
        for i in range(9):
            self.matPosb[i][pos.getY()][self.sudoku.getVal(
                pos.getX(), pos.getY()) - 1] = 0
        for j in range(9):
            self.matPosb[pos.getX()][j][self.sudoku.getVal(
                pos.getX(), pos.getY()) - 1] = 0

        for i in range(3):
            for j in range(3):
                self.matPosb[pos.getXCuad() + i][pos.getYCuad() +
                                                 j][self.sudoku.getVal(pos.getX(), pos.getY()) - 1] = 0

    def __horizontal2(self, pos):
        k = 0
        while k < 9 and self.sudoku.getVal(pos.getX(), pos.getY()) == 0:
            if self.matPosb[pos.getX()][pos.getY()][k] == 1:
                corte = False
                j = 0
                while j < pos.getY() and not corte:
                    corte = self.matPosb[pos.getX()][j][k] == 1
                    j += 1
                j = pos.getY() + 1
                while j < 9 and not corte:
                    corte = self.matPosb[pos.getX()][j][k] == 1
                    j += 1
                if not corte:
                    self.sudoku.setVal(pos.getX(), pos.getY(), k + 1)
            k += 1

    def __vertical2(self, pos):
        k = 0
        while k < 9 and self.sudoku.getVal(pos.getX(), pos.getY()) == 0:
            if self.matPosb[pos.getX()][pos.getY()][k] == 1:
                corte = False
                i = 0
                while i < pos.getX() and not corte:
                    corte = self.matPosb[i][pos.getY()][k] == 1
                    i += 1
                i = pos.getX() + 1
                while i < 9 and not corte:
                    corte = self.matPosb[i][pos.getY()][k] == 1
                    i += 1
                if not corte:
                    self.sudoku.setVal(pos.getX(), pos.getY(), k + 1)
            k += 1

    def __cuadrado2(self, pos):
        k = 0
        while k < 9 and self.sudoku.getVal(pos.getX(), pos.getY()) == 0:
            if self.matPosb[pos.getX()][pos.getY()][k] == 1:
                corte = False
                i = pos.getXCuad()
                while i < pos.getXCuad() + 3 and not corte:
                    j = pos.getYCuad()
                    while j < pos.getYCuad() + 3 and not corte:
                        corte = self.matPosb[i][j][k] == 1 and (
                            i != pos.getX() or j != pos.getY())
                        j += 1
                    i += 1
                if not corte:
                    self.sudoku.setVal(pos.getX(), pos.getY(), k + 1)
            k += 1

    def __preRecorrido2(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku.getVal(i,j) != 0:
                    self.matPosb[i][j] = numpy.zeros(9)

    def __recorrido1(self):
        pos = Pos(0, -1)
        meCai = self.__buscoVacio(pos)
        while not meCai:
            direc = 1
            while direc < 4 and not meCai:
                self.recorridos[direc](pos)
                cuenta = 0
                k = 0
                while k < 9 and cuenta < 2:
                    if self.matPosb[pos.getX()][pos.getY()][k] == 1:
                        cuenta += 1
                        n = k
                    k += 1
                if cuenta == 1:
                    self.sudoku.setVal(pos.getX(), pos.getY(), n + 1)
                    pos.reset()
                    direc = 1
                    meCai = self.__buscoVacio(pos)
                else:
                    direc += 1
            meCai = self.__buscoVacio(pos)

    def __recorrido2(self):
        pos = Pos(0, -1)
        meCai = self.__buscoVacio(pos)
        while not meCai:
            direc = 4
            while direc < 7 and not meCai:
                self.recorridos[direc](pos)
                if self.sudoku.getVal([pos.getX()][pos.getY()]) != 0:
                    self.__actualizoAux(pos)
                    pos.reset()
                    direc = 4
                    meCai = self.__buscoVacio(pos)
                else:
                    direc += 1
            meCai = self.__buscoVacio(pos)

    def main(self, matRes):
        self.__recorrido1()
        self.__preRecorrido2()
        self.__recorrido2()
        return matRes
