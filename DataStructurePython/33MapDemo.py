class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedVertices = {}  # Store connected vertices

    def addConnected(self, connected, weight):
        self.connectedVertices[connected] = weight

    def __str__(self):
        return str(self.id) + ' connected to ' + str([x.id for x in self.connectedVertices])

    def getConnections(self):
        return self.connectedVertices.keys()

    def getId(self):
        return self.id

    def getWeight(self, connected):
        return self.connectedVertices[connected]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        vertex = Vertex(key)
        self.numVertices = self.numVertices + 1
        self.vertList[key] = vertex
        return vertex

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, fromKey, toKey, weight):
        if fromKey not in self.vertList:
            self.addVertex(fromKey)
        if toKey not in self.vertList:
            self.addVertex(toKey)
        self.vertList[fromKey].addConnected(self.vertList[toKey], weight)

    def __iter__(self):
        return iter(self.vertList.values())


if __name__ == "__main__":
    graph = Graph()
    for i in range(6):
        graph.addVertex(i)
    print(graph.vertList)
    graph.addEdge(0, 1, 5)
    graph.addEdge(0, 5, 2)
    graph.addEdge(1, 2, 4)
    graph.addEdge(2, 3, 9)
    graph.addEdge(3, 4, 7)
    graph.addEdge(3, 5, 3)
    graph.addEdge(4, 0, 1)
    graph.addEdge(5, 4, 8)
    graph.addEdge(5, 2, 1)
    for v in graph:
        for w in v.getConnections():
            print('(%s,%s)' % (v.getId(), w.getId()))
