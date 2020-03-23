class Edge:
    def __init__(self, con1, con2, substr):
        self.from = con1
        self.to = con2
        self.substr = substr

class Node:
    def __init__(self, isEnd):
        self.end = isEnd
        self.children = []
        self.childStrings = []

    def addChild(self, isEnd, childStr):
        self.children.append(Node(isEnd))
        self.childStrings.append(childStr)

    def findChild(self, poss):
        for cs in range(len(self.childStrings)):
            if poss.startswith(self.childStrings[cs]):
                return self.children[cs], self.childStrings[cs]
        return None, ""

class SuffixTree:
    def __init__(self):
        self.root = Node(False)
        self.nodes = [self.root]
        self.edges = []

    def add(self, toAdd):
        posChild, posStr = self.root.findChild(toAdd)
        if len(posStr) > 0:
            self.addToNode(toAdd[len(posStr):], posChild)
        else:
            self.root.addChild(True, toAdd)
            
    def addToNode(self, toAdd, node):

    def search(self, node, strSearch):
