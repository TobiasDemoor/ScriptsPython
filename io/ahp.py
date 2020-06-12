import numpy as np

RI = {
    3: 0.58,
    4: 0.90,
    5: 1.12,
    6: 1.24,
    7: 1.32,
    8: 1.31
}


def completaCompPareada(mat):
    for i in range(len(mat)):
        mat[i][i] = 1
        for j in range(i):
            mat[i][j] = 1 / mat[j][i]


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


def priGlobal(pris, priCriterios):
    aux = np.zeros(len(pris[0]))
    for j in range(len(pris[0])):
        for i in range(len(priCriterios)):
            aux[j] += pris[i][j]*priCriterios[i]
    return aux


def relConsistencia(mat, pri):
    n = len(mat)
    aux = np.zeros(n)
    for i in range(n):
        aux[i] = sum(mat[i]*pri)
    prom = sum(aux/pri)/n
    ic = (prom - n)/(n-1)
    return ic/RI[n]


# region 1
# nombres = ["BsAs", "Rosario", "MdP"]
# mat = np.array([
#     [1, 3, 5],
#     [1, 1, 4],
#     [1, 1, 1]
# ], np.float)
# # a
# completaCompPareada(mat)
# print(mat)
# # b
# pri = priCriterio(mat)
# print(pri)
# # c
# print(relConsistencia(mat, pri))
# endregion

# region 2
# nombres = ["Computer Central", "Software Research"]
# matRendimiento = np.array([
#     [1, 3],
#     [1/3, 1],
# ], np.float)
# matRiesgo = np.array([
#     [1, 1/2],
#     [2, 1],
# ], np.float)
# criterios = ["Rendimiento", "Riesgo"]
# matCriterios = np.array([
#     [1, 2],
#     [1/2, 1],
# ], np.float)
# #b
# priRendimiento = priCriterio(matRendimiento)
# priRiesgo = priCriterio(matRiesgo)
# priCriterios = priCriterio(matCriterios)
# print(priRendimiento)
# print(priRiesgo)
# print(priCriterios)
# #c
# priGlobal = priGlobal([priRendimiento, priRiesgo], priCriterios)
# print(priGlobal)
# endregion

# region 3
# criterios = ["Precio", "Calidad", "Mant"]
# matCriterios = np.array([
#     [1, 3, 4],
#     [1/3, 1, 3],
#     [1/4, 1/3, 1],
# ], np.float)
# nombres = ["M1", "M2", "M3"]
# mats = np.array([
#     [
#         [1, 4, 2],
#         [1/4, 1, 1/3],
#         [1/2, 3, 1],
#     ], [
#         [1, 1/2, 1/4],
#         [2, 1, 1/3],
#         [4, 3, 1]
#     ], [
#         [1, 4, 2],
#         [1/4, 1, 1],
#         [1/2, 1, 1],
#     ]
# ], np.float)
# prioridades = np.array(list(map(lambda x: priCriterio(x), mats)))
# priCriterios = priCriterio(matCriterios)
# rcs = np.array(list(map(lambda x, y: relConsistencia(x, y), mats, prioridades)))
# prioridadGlobal = priGlobal(prioridades, priCriterios)
# print(rcs)
# print(prioridadGlobal)
# endregion

# region 4
# criterios = ["Entrega", "Calidad"]
# subcriterios = [
#     ["Fecha", "Cantidad"],
#     ["Conformidad", "Funcionalidad"],
# ]
# matCriterios = np.array([
#     [1, 3],
#     [1/3, 1],
# ], np.float)
# matsSubcriterios = np.array([
#     [
#         [1, 2],
#         [1/2, 1],
#     ], [
#         [1, 7],
#         [1/7, 1]
#     ]
# ], np.float)
# nombres = ["P1", "P2"]
# mats = np.array([
#     [
#         [
#             [1, 1/3],
#             [3, 1],
#         ],[
#             [1, 5],
#             [1/5, 1],
#         ]
#     ], [
#         [
#             [1,4],
#             [1/4,1],
#         ],[
#             [1, 2],
#             [1/2, 1],
#         ]
#     ]
# ], np.float)
# priSubcriterios = np.array(list(map(lambda x: priCriterio(x), matsSubcriterios)))
# priCriterios = priCriterio(matCriterios)
# prioridades = np.array(list(map(
#     lambda x: np.array(list(map(
#         lambda y: priCriterio(y), x
#     ))), mats
# )))
# priGlobalsubcriterios = np.array(list(map(lambda x, y: priGlobal(x, y), prioridades, priSubcriterios)))
# prioridadGlobal = priGlobal(priGlobalsubcriterios, priCriterios)
# print(prioridades)
# print(priGlobalsubcriterios)
# print(prioridadGlobal)
# endregion
