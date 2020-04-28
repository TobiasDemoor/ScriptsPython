import numpy


class Pos:
    def __init__(self, xInit: int = 0, yInit: int = 0):
        self.xInit = xInit
        self.yInit = yInit
        self.x = xInit
        self.y = yInit

    def getX(self) -> int:
        return self.x

    def getY(self) -> int:
        return self.y

    def setX(self, x: int):
        self.x = x

    def setY(self, y: int):
        self.y = y

    def incrX(self):
        self.x += 1

    def incrY(self):
        self.y += 1

    def reset(self):
        self.x = self.xInit
        self.y = self.yInit


class Sudoku:
    def __init__(self, mat: numpy.ndarray):
        self.matRes = mat

    def getVal(self, x: int = None, y: int = None, pos: Pos = None) -> int:
        if not (x is None or y is None):
            ret = self.matRes[x][y]
        elif pos is not None:
            ret = self.matRes[pos.getX()][pos.getY()]
        else:
            raise TypeError(
                "Faltan parametros x:{}, y:{}, pos:{}".format(x, y, pos))
        return ret

    def setVal(self, val: int, pos: Pos = None, x: int = None, y: int = None):
        if not (x is None or y is None):
            self.matRes[x][y] = val
        elif pos is not None:
            self.matRes[pos.getX()][pos.getY()] = val
        else:
            raise TypeError(
                "Faltan parametros x:{}, y:{}, pos:{}".format(x, y, pos))

    def estaVacio(self, pos: Pos) -> bool:
        return self.getVal(pos = pos) != 0

    def encuentroCuadPos(self, pos: Pos) -> Pos:
        ret = Pos()
        if pos.getX() < 3:
            ret.setX(0)
        elif pos.getX() < 6:
            ret.setX(3)
        else:
            ret.setX(6)

        if pos.getY() < 3:
            ret.setY(0)
        elif pos.getY() < 6:
            ret.setY(3)
        else:
            ret.setY(6)

        return ret


class ResuelveSudoku:
    def __init__(self, sudoku: Sudoku):
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

    def __buscoVacio(self, pos: Pos) -> bool:
        corte = False
        if pos.getY() < 8:
            pos.incrY()
        elif pos.getX() < 8:
            pos.setY(0)
            pos.incrX()
        else:
            corte = True
        while self.sudoku.estaVacio(pos) and not corte:
            if pos.getY() < 8:
                pos.incrY()
            elif pos.getX() < 8:
                pos.setY(0)
                pos.incrX()
            else:
                corte = True
        return corte

    def __horizontal1(self, pos: Pos):
        for k in range(9):
            if self.sudoku.getVal(pos.getX(), k) != 0:
                self.matPosb[pos.getX()][pos.getY()][self.sudoku.getVal(
                    pos.getX(), k) - 1] = 0

    def __vertical1(self, pos: Pos):
        for k in range(9):
            if self.sudoku.getVal(k, pos.getY()) != 0:
                self.matPosb[pos.getX()][pos.getY()][self.sudoku.getVal(
                    k, pos.getY()) - 1] = 0

    def __cuadrado1(self, pos: Pos):
        posCuad = self.sudoku.encuentroCuadPos(pos)
        for i in range(3):
            for j in range(3):
                if self.sudoku.getVal(posCuad.getX() + i, posCuad.getY() + j) != 0:
                    self.matPosb[pos.getX()][pos.getY()][self.sudoku.getVal(
                        posCuad.getX() + i, posCuad.getY() + j) - 1] = 0

    def __actualizoAux(self, pos: Pos):
        posCuad = self.sudoku.encuentroCuadPos(pos)
        self.matPosb[pos.getX()][pos.getY()] = numpy.zeros(9)
        for i in range(9):
            self.matPosb[i][pos.getY()][self.sudoku.getVal(
                pos.getX(), pos.getY()) - 1] = 0
        for j in range(9):
            self.matPosb[pos.getX()][j][self.sudoku.getVal(
                pos.getX(), pos.getY()) - 1] = 0

        for i in range(3):
            for j in range(3):
                self.matPosb[posCuad.getX() + i][posCuad.getY() +
                                                 j][self.sudoku.getVal(pos=pos) - 1] = 0

    def __horizontal2(self, pos: Pos):
        k = 0
        while k < 9 and self.sudoku.getVal(pos=pos) == 0:
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
                    self.sudoku.setVal(k + 1, pos=pos)
            k += 1

    def __vertical2(self, pos: Pos):
        k = 0
        while k < 9 and self.sudoku.getVal(pos=pos) == 0:
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
                    self.sudoku.setVal(k + 1, pos=pos)
            k += 1

    def __cuadrado2(self, pos: Pos):
        k = 0
        posCuad: Pos = self.sudoku.encuentroCuadPos(pos)
        while k < 9 and self.sudoku.getVal(pos=pos) == 0:
            if self.matPosb[pos.getX()][pos.getY()][k] == 1:
                corte = False
                i = posCuad.getX()
                while i < posCuad.getX() + 3 and not corte:
                    j = posCuad.getY()
                    while j < posCuad.getY() + 3 and not corte:
                        corte = self.matPosb[i][j][k] == 1 and (
                            i != pos.getX() or j != pos.getY())
                        j += 1
                    i += 1
                if not corte:
                    self.sudoku.setVal(k + 1, pos=pos)
            k += 1

    def __preRecorrido2(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku.getVal(i, j) != 0:
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
                    self.sudoku.setVal(n + 1, pos=pos)
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

    def main(self):
        self.__recorrido1()
        self.__preRecorrido2()
        self.__recorrido2()

