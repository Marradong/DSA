import linkedList as LL


class DSAGraphVertex():

    def __init__(self, inLabel, inValue):
        self._label = inLabel
        self._value = inValue
        self._visited = False
        self._links = LL.DSADoublyLinkedList()
        self._edges = LL.DSADoublyLinkedList()


    def getLabel(self):
        return self._label
    

    def getValue(self):
        return self._value
    
    def getAdjacent(self):
        return self._links
    
    def getAdjacentE(self):
        return self._edges

    def addLink(self, vertex):
        self._links.insertLast(vertex)
        return


    def addEdge(self, edge):
        if edge.getFrom().getLabel() == self.getLabel():
            self.addLink(edge.getTo())
        else:
            self.addLink(edge.getFrom())
        self._edges.insertLast(edge)
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
        stringToReturn = "Vertex: " + str(self.getLabel()) + " value = " + str(self.getValue())
        return stringToReturn
        



class DSAGraphEdge():
    

    def __init__(self, fromVertex, toVertex, inLabel, inValue):
        self._from = fromVertex
        self._to = toVertex
        self._label = inLabel
        self._value = inValue

    
    def getLabel(self):
        return self._label
    

    def getValue(self):
        return self._value
    

    def getFrom(self):
        return self._from


    def getTo(self):
        return self._to
    

    def isDirected(self):
        hasDirection = False
        return hasDirection
    

    def toString(self):
        stringToReturn = "Edge: " + str(self.getLabel()) + " value = " + str(self.getValue())
        return stringToReturn


class DSAGraph():


    def __init__(self):
        self.vertices = LL.DSADoublyLinkedList()
        self.edges = LL.DSADoublyLinkedList()


    def addVertex(self, label, value):
        if not self.hasVertex(label):
            newVertex = DSAGraphVertex(label, value)
            self.vertices.insertLast(newVertex)
        else:
            print("Vertex label already exists!")
        return
    

    def addEdge(self, fromLabel, toLabel, edgeLabel, value):
        if not self.hasEdge(edgeLabel):
            fromVertex = self.getVertex(fromLabel)
            toVertex = self.getVertex(toLabel)
            newEdge = DSAGraphEdge(fromVertex, toVertex, edgeLabel, value)
            fromVertex.addEdge(newEdge)
            toVertex.addEdge(newEdge)
            self.edges.insertLast(newEdge)
        else:
            print("Edge label already exists!")
        return


    def hasVertex(self, label):
        vertexExists = False
        for vertex in self.vertices:
            if vertex.getValue().getLabel() == label:
                vertexExists = True
        return vertexExists
    

    def hasEdge(self, label):
        edgeExists = False
        for edge in self.edges:
            if edge.getValue().getLabel() == label:
                edgeExists = True
        return edgeExists

    
    def getVertexCount(self):
        vertexCount = 0
        for vertex in self.vertices:
            vertexCount = vertexCount + 1
        return vertexCount


    def getEdgeCount(self):
        edgeCount = 0
        for edge in self.edges:
            edgeCount = edgeCount + 1
        return edgeCount
    

    def getVertex(self, label):
        vertexGot = None
        for vertex in self.vertices:
            if vertex.getValue().getLabel() == label:
                vertexGot = vertex.getValue()
        if vertexGot == None:
            print("Vertex with label: " + str(label) + " does not exist!")
        else:
            return vertexGot
        
    

    def getEdge(self, label):
        edgeGot = None
        for edge in self.edges:
            if edge.getValue().getLabel() == label:
                edgeGot = edge.getValue()
        if edgeGot == None:
            print("Edge with label: " + str(label) + " does not exist!")
        else:
            return edgeGot
    

    def getAdjacent(self, label):
        vertex:DSAGraphVertex = self.getVertex(label)
        return vertex.getAdjacent()
    
    
    def getAdjacentE(self, label):
        vertex:DSAGraphVertex = self.getVertex(label)
        return vertex.getAdjacentE()
