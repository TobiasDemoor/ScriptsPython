class Node:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
    
    def addChild(self, child):
        self.children.append(child)
    
    def getChildren(self):
        return self.children
    
    def getChild(self, index):
        return self.children[index]
    
    def getValue(self):
        return self.value



def procArbol(nodo):
    hijos = nodo.getChildren()
    if hijos == None:
        return priCriterio(nodo.getValue())
    else:
        prioridades = []
        for h in hijos:
            prioridades.append(procArbol(h))
        return priGlobal(prioridades, nodo.getValue())

# raiz = Node(np.array([
#             [1, 3],
#             [1/3, 1],
#             ]), [
#     Node(np.array([
#         [1, 2],
#         [1/2, 1],
#     ]), [
#         Node(np.array([
#             [1, 1/3],
#             [3, 1],
#         ])),
#         Node(np.array([
#             [1, 5],
#             [1/5, 1],
#         ]))
#     ]),
#     Node(np.array([
#         [1, 7],
#         [1/7, 1]
#     ]), [
#         Node(np.array([
#             [1, 4],
#             [1/4, 1],
#         ])),
#         Node(np.array([
#             [1, 2],
#             [1/2, 1],
#         ]))
#     ])
# ])