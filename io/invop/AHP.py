import numpy as np

class AHP:
    RI = {
        3: 0.58,
        4: 0.90,
        5: 1.12,
        6: 1.24,
        7: 1.32,
        8: 1.31
    }

    @staticmethod
    def completaCompPareada(mat):
        for i in range(len(mat)):
            mat[i][i] = 1
            for j in range(i):
                mat[i][j] = 1 / mat[j][i]

    @staticmethod
    def priCriterio(mat):
        n = len(mat)
        pri = np.zeros(n)
        for j in range(n):
            suma = 0
            for i in range(n):
                suma += mat[i][j]
            for i in range(n):
                pri[i] += mat[i][j]/(suma*n)
        return pri

    @staticmethod
    def priGlobal(pris, priCriterios):
        aux = np.zeros(len(pris[0]))
        for j in range(len(pris[0])):
            for i in range(len(priCriterios)):
                aux[j] += pris[i][j]*priCriterios[i]
        return aux

    @staticmethod
    def relConsistencia(mat, pri):
        n = len(mat)
        aux = np.zeros(n)
        for i in range(n):
            aux[i] = sum(mat[i]*pri)
        prom = sum(aux/pri)/n
        ic = (prom - n)/(n-1)
        return ic/AHP.RI[n]

    @staticmethod
    def procArbol(nodo):
        hijos = nodo.getChildren()
        if len(hijos) == 0:
            return AHP.priCriterio(nodo.getValue())
        else:
            prioridades = np.array(list(map(AHP.procArbol, hijos)))
            return AHP.priGlobal(prioridades, AHP.priCriterio(nodo.getValue()))
