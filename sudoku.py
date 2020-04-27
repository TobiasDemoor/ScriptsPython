# pylint: disable=no-member
import numpy
# from pandas import DataFrame

def ImprimirSudoku(mat):
    for i in range(3):
        print('-------------------------')
        for j in range(3):
            for k in range(3):
                print('| ', end = '')
                for l in range(3):
                    print( mat[j + i*3][l + k*3], end = ' ')
            print('|')
    print('-------------------------')

def BuscoVacio(matRes, pos):
    corte = False
    if pos['y'] < 8 :
        pos['y'] += 1
    elif pos['x'] < 8 :
        pos['y'] = 0
        pos['x'] += 1
    else:
        corte = True
    while matRes[pos['x']][pos['y']] != 0 and not corte:
        if pos['y'] < 8 :
            pos['y'] += 1
        elif pos['x'] < 8 :
            pos['y'] = 0
            pos['x'] += 1
        else:
            corte = True
    return corte

def EncuentroPosCuad(pos):
    posI = {}

    if pos['x'] < 3:
        posI['x'] = 0
    elif pos['x'] < 6:
        posI['x'] = 3
    else:
        posI['x'] = 6

    if pos['y'] < 3:
        posI['y'] = 0
    elif pos['y'] < 6:
        posI['y'] = 3
    else:   
        posI['y'] = 6

    return posI

def Horizontal1(matRes, vecAux, pos):
    for k in range(9):
        if matRes[pos['x']][k] != 0:
            vecAux[matRes[pos['x']][k] - 1] = 0

def Vertical1(matRes, vecAux, pos):
    for k in range(9):
        if matRes[k][pos['y']] != 0:
            vecAux[matRes[k][pos['y']] - 1] = 0

def Cuadrado1(matRes, vecAux, pos):
    posI = EncuentroPosCuad(pos)

    for i in range(3):
        for j in range(3):
            if matRes[posI['x'] + i][posI['y'] + j] != 0:
                vecAux[matRes[posI['x'] + i][posI['y'] + j] - 1] = 0

def Recorrido1(matRes, matAux):
    recorridos = {
        1: Horizontal1,
        2: Vertical1,
        3: Cuadrado1,
    }
    pos = {
        'x': 0,
        'y': -1,
    }
    meCai = BuscoVacio(matRes, pos)
    while not meCai:
        direc = 1
        while direc < 4 and not meCai:
            recorridos[direc](matRes, matAux[pos['x']][pos['y']], pos)
            cuenta = 0
            k = 0
            while k < 9 and cuenta < 2:
                if matAux[pos['x']][pos['y']][k] == 1:
                    cuenta += 1
                    n = k
                k += 1
            if cuenta == 1:
                matRes[pos['x']][pos['y']] = n + 1
                pos = {
                    'x': 0,
                    'y': -1,
                }
                direc = 1
                meCai = BuscoVacio(matRes, pos)
            else:
                direc += 1
        meCai = BuscoVacio(matRes, pos)

def Horizontal2(matRes, matAux, pos):
    k = 0
    while k < 9 and matRes[pos['x']][pos['y']] == 0:
        if matAux[pos['x']][pos['y']][k] == 1:
            corte = False
            j = 0
            while j < pos['y'] and not corte:
                corte = matAux[pos['x']][j][k] == 1
                j += 1
            j = pos['y'] + 1
            while j < 9 and not corte:
                corte = matAux[pos['x']][j][k] == 1
                j += 1
            if not corte:
                matRes[pos['x']][pos['y']] = k + 1
        k += 1

def Vertical2(matRes, matAux, pos):
    k = 0
    while k < 9 and matRes[pos['x']][pos['y']] == 0:
        if matAux[pos['x']][pos['y']][k] == 1:
            corte = False
            i = 0
            while i < pos['x'] and not corte:
                corte = matAux[i][pos['y']][k] == 1
                i += 1
            i = pos['x'] + 1
            while i < 9 and not corte:
                corte = matAux[i][pos['y']][k] == 1
                i += 1
            if not corte:
                matRes[pos['x']][pos['y']] = k + 1
        k += 1

def Cuadrado2(matRes, matAux, pos):
    posI = EncuentroPosCuad(pos)
    k = 0
    while k < 9 and matRes[pos['x']][pos['y']] == 0:
        if matAux[pos['x']][pos['y']][k] == 1:
            corte = False
            i = posI['x']
            while i < posI['x'] + 3 and not corte:
                j = posI['y']
                while j < posI['y'] + 3 and not corte:
                    corte = matAux[i][j][k] == 1 and (i != pos['x'] or j != pos['y'])
                    j += 1
                i += 1
            if not corte:
                matRes[pos['x']][pos['y']] = k + 1
        k += 1

def PreRecorrido2(matRes, matAux):
    for i in range(9):
        for j in range(9):
            if matRes[i][j] != 0:
                matAux[i][j] = numpy.zeros(9)

def ActualizoAux(matRes, matAux, pos):
    matAux[pos['x']][pos['y']] = numpy.zeros(9)
    for i in range(9):
        matAux[i][pos['y']][matRes[pos['x']][pos['y']] - 1] = 0
    for j in range(9):
        matAux[pos['x']][j][matRes[pos['x']][pos['y']] - 1] = 0

    posI = EncuentroPosCuad(pos)

    for i in range(3):
        for j in range(3):
            matAux[posI['x'] + i][posI['y'] + j][matRes[pos['x']][pos['y']] - 1] = 0

def Recorrido2(matRes, matAux):
    recorridos = {
        1: Horizontal2,
        2: Vertical2,
        3: Cuadrado2,
    }
    PreRecorrido2(matRes, matAux)
    pos = {
        'x': 0,
        'y': -1,
    }
    meCai = BuscoVacio(matRes, pos)
    while not meCai:
        direc = 1
        while direc < 4 and not meCai:
            recorridos[direc](matRes, matAux, pos)
            if matRes[pos['x']][pos['y']] != 0:
                ActualizoAux(matRes, matAux, pos)
                pos = {
                    'x': 0,
                    'y': -1,
                }
                direc = 1
                meCai = BuscoVacio(matRes, pos)
            else:
                direc += 1
        meCai = BuscoVacio(matRes, pos)

def main(matRes):
    matAux = numpy.ones((9, 9, 9))
    Recorrido1(matRes, matAux)
    Recorrido2(matRes, matAux)
    return matRes

# matRes = numpy.array([
#     [0, 0, 0, 8, 0, 5, 0, 1, 3],
#     [0, 0, 0, 2, 0, 3, 6, 0, 0],
#     [6, 0, 0, 0, 9, 0, 2, 0, 4],
#     [0, 0, 0, 0, 0, 0, 0, 0, 5],
#     [0, 4, 0, 1, 0, 0, 7, 0, 6],
#     [2, 5, 6, 3, 0, 4, 8, 9, 0],
#     [5, 9, 0, 0, 0, 7, 1, 0, 2],
#     [1, 0, 2, 0, 8, 0, 4, 7, 0],
#     [0, 0, 4, 9, 1, 0, 0, 3, 8],
# ])
# matRes = numpy.array([
#     [0, 3, 0, 0, 0, 0, 0, 7, 0],
#     [6, 0, 9, 0, 5, 0, 0, 3, 0],
#     [8, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 6, 0, 3, 7, 8, 4, 1, 0],
#     [3, 0, 0, 0, 0, 0, 0, 0, 8],
#     [1, 8, 5, 4, 2, 9, 0, 0, 0],
#     [0, 0, 8, 7, 4, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 2, 0, 0],
#     [0, 0, 0, 0, 3, 2, 0, 5, 7],
# ])
# matRes = numpy.array([
#     [6, 0, 0, 0, 0, 1, 0, 0, 0], 
#     [0, 0, 7, 0, 0, 0, 5, 0, 0], 
#     [0, 3, 0, 6, 0, 0, 9, 4, 0], 
#     [0, 0, 1, 0, 0, 0, 0, 0, 8], 
#     [0, 0, 0, 0, 4, 0, 0, 0, 0], 
#     [3, 0, 0, 0, 0, 0, 7, 0, 0], 
#     [0, 7, 2, 0, 0, 5, 0, 3, 0], 
#     [0, 0, 5, 0, 0, 0, 4, 0, 0], 
#     [0, 0, 0, 2, 0, 0, 0, 0, 1],
# ])
# matRes = numpy.array([
#     [0, 0, 1, 0, 0, 0, 0, 0, 0], 
#     [0, 8, 0, 0, 2, 0, 0, 4, 0], 
#     [0, 0, 9, 3, 0, 8, 2, 0, 7], 
#     [0, 0, 2, 0, 0, 0, 4, 0, 0], 
#     [0, 6, 0, 0, 8, 0, 0, 3, 0], 
#     [0, 0, 8, 0, 0, 0, 9, 0, 0], 
#     [9, 0, 3, 7, 0, 2, 5, 0, 0], 
#     [0, 5, 0, 0, 4, 0, 0, 6, 0], 
#     [0, 0, 0, 0, 0, 0, 7, 0, 0], 
# ])
# matRes = numpy.array([
#     [0, 0, 0, 0, 8, 0, 7, 0, 0], 
#     [8, 3, 2, 0, 5, 0, 0, 0, 0], 
#     [7, 0, 5, 3, 9, 0, 0, 1, 0], 
#     [0, 1, 3, 5, 0, 0, 8, 2, 0], 
#     [2, 0, 0, 0, 3, 0, 0, 4, 9], 
#     [9, 8, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 7, 0, 0, 0, 0, 0, 0, 0], 
#     [4, 0, 9, 0, 6, 0, 1, 8, 5], 
#     [0, 0, 1, 0, 0, 0, 0, 0, 0], 
# ])
# ImprimirSudoku(main(matRes))
