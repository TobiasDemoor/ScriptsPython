import numpy as np
from invop.AHP import AHP, NodoArbol

# region 1
nombres = ["BsAs", "Rosario", "MdP"]
mat = np.array([
    [1, 3, 5],
    [1, 1, 4],
    [1, 1, 1]
], np.float)
# a
AHP.completaCompPareada(mat)
print(mat)
# b
pri = AHP.priCriterio(mat)
print(pri)
# c
print(AHP.relConsistencia(mat, pri))
# endregion

# region 2
nombres = ["Computer Central", "Software Research"]
matRendimiento = np.array([
    [1, 3],
    [1/3, 1],
], np.float)
matRiesgo = np.array([
    [1, 1/2],
    [2, 1],
], np.float)
criterios = ["Rendimiento", "Riesgo"]
matCriterios = np.array([
    [1, 2],
    [1/2, 1],
], np.float)
#b
priRendimiento = AHP.priCriterio(matRendimiento)
priRiesgo = AHP.priCriterio(matRiesgo)
priCriterios = AHP.priCriterio(matCriterios)
print(priRendimiento)
print(priRiesgo)
print(priCriterios)
#c
priGlobal = AHP.priGlobal([priRendimiento, priRiesgo], priCriterios)
print(priGlobal)
# endregion

# region 3
criterios = ["Precio", "Calidad", "Mant"]
matCriterios = np.array([
    [1, 3, 4],
    [1/3, 1, 3],
    [1/4, 1/3, 1],
], np.float)
nombres = ["M1", "M2", "M3"]
mats = np.array([
    [
        [1, 4, 2],
        [1/4, 1, 1/3],
        [1/2, 3, 1],
    ], [
        [1, 1/2, 1/4],
        [2, 1, 1/3],
        [4, 3, 1]
    ], [
        [1, 4, 2],
        [1/4, 1, 1],
        [1/2, 1, 1],
    ]
], np.float)
prioridades = np.array(list(map(AHP.priCriterio, mats)))
priCriterios = AHP.priCriterio(matCriterios)
rcs = np.array(list(map(AHP.relConsistencia, mats, prioridades)))
prioridadGlobal = AHP.priGlobal(prioridades, priCriterios)
print(rcs)
print(prioridadGlobal)
# endregion

# region 4
fecha = NodoArbol(np.array([  # Subcriterio Fecha
    [1, 1/3],
    [3, 1],
]))

cantidad = NodoArbol(np.array([  # Subcriterio Cantidad
    [1, 5],
    [1/5, 1],
]))

entrega = NodoArbol(np.array([  # Criterio Entrega
    [1, 2],
    [1/2, 1],
]), [fecha, cantidad])

conform = NodoArbol(np.array([  # Subcriterio Conformidad
    [1, 4],
    [1/4, 1],
]))

funcion = NodoArbol(np.array([  # Subcriterio Funcionalidad
    [1, 2],
    [1/2, 1],
]))

calidad = NodoArbol(np.array([  # Criterio Calidad
    [1, 7],
    [1/7, 1]
]), [conform, funcion])

crit = NodoArbol(np.array([  # Criterios
    [1, 3],
    [1/3, 1],
]), [entrega, calidad])

print(AHP.procArbol(crit))
# endregion
