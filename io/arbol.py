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
