import linkedList as LL

class DSAGraphVertex():

    def __init__(self, inLabel, inValue):
        self._label = inLabel
        self._value = inValue
        self._links = LL.DSADoublyLinkedList()
        self._visited = False

    def getLabel(self):
        return self._label
    
    def getValue(self):
        return self._value
    
    def getAdjacent(self):
        return self._links
    
    def addEdge(self, vertex):
        self._links.insertLast(vertex)
        return
    
    def setVisited(self):
        self._visited = True
        return
    
    def clearVisited(self):
        self._visited = False
        return
    
    def getVisited(self):
        return self._visited
    
    def toString(self):
        stringVertex = "Label: " + str(self.getLabel()) + " Value: " + str(self.getValue())
        return stringVertex

class DSAGraph():

    def __init__(self):
        self.vertices = LL.DSADoublyLinkedList()
        self.edges = LL.DSADoublyLinkedList()

    def addVertex(self, label, value):
        if not self.hasVertex(label):
            newVertex = DSAGraphVertex(label, value)
            self.vertices.insertLast(newVertex)
        else:
            print("Vertex already exists")
    
    def addEdge(self, label1, label2):
        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)
        if (vertex1 == None) or (vertex2 == None):
            print("One vertex does not exist")
        else:
            vertex1.addEdge(vertex2)
            vertex2.addEdge(vertex1)
            edgeLabel = str(vertex1.getLabel()) + str(vertex2.getLabel())
            self.edges.insertLast(edgeLabel)


    def hasVertex(self, label):
        vertexFound = False
        for node in self.vertices:
            vertex = node.getValue()
            if vertex.getLabel() == label:
                vertexFound = True
        return vertexFound
    
    def getVertexCount(self):
        count = 0
        for node in self.vertices:
            count = count + 1
        return count
    
    def getEdgeCount(self):
        count = 0
        for node in self.edges:
            count = count + 1
        return count
    
    def getVertex(self, label):
        gotVertex = None
        for node in self.vertices:
            vertex = node.getValue()
            if vertex.getLabel() == label:
                gotVertex = vertex
        return gotVertex
    
    def getAdjacent(self, label):
        vertexList = None
        for node in self.vertices:
            vertex = node.getValue()
            if vertex.getLabel() == label:
                vertexList = vertex.getAdjacent()
        return vertexList
    
    def isAdjacent(self, label1, label2):
        adjacentFound = False
        for node in self.getAdjacent(label1):
            vertex = node.getValue()
            if vertex.getLabel() == label2:
                adjacentFound = True
        return adjacentFound
    
    def displayAsList(self):
        print("\nAdjacency List: ")
        for node in self.vertices:
            vertex = node.getValue()
            stringToPrint = str(vertex.getLabel()) + " | "
            for item in vertex.getAdjacent():
                stringToPrint = stringToPrint + str(item.getValue().getLabel()) + " "
            print(stringToPrint)
            

    def displayAsMatrix(self):
        ...