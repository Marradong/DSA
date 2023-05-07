import linkedList as LL
import stackQueue as sq


class DSAGraphEdge():
    
    def __init__(self, toVertex, fromVertex, inValue):
        self._to = toVertex
        self._from = fromVertex
        self._value = inValue
    
    def getValue(self):
        return self._value

    def getTo(self):
        return self._value
    
    def getFrom(self):
        return self._value

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
        return
    

    def deleteVertex(self, delLabel):
        vertexToDelete = self.getVertex(delLabel)
        for node in self.vertices:
            if (node.getValue() == vertexToDelete):
                self.vertices.remove(node.getValue())
        
        for linkNode in vertexToDelete.getAdjacent():
            self.deleteEdge(vertexToDelete.getLabel(), linkNode.getValue().getLabel())
        return
    
    def addEdge(self, label1, label2, value=None):
        vertex1 = self.getVertex(label1)
        vertex2 = self.getVertex(label2)
        if (vertex1 == None) or (vertex2 == None):
            print("One vertex does not exist ")
        else:
            vertex1.addEdge(vertex2)
            vertex2.addEdge(vertex1)
            newEdge = DSAGraphEdge(vertex1, vertex2, value)
            self.edges.insertLast(newEdge)
        return
    
    def deleteEdge(self, toLabel, fromLabel):
        toVertex = self.getVertex(toLabel)
        fromVertex = self.getVertex(fromLabel)
        # Remove link between vertices
        for toNode in toVertex.getAdjacent():
            if toNode.getValue() == fromVertex:
                toVertex.getAdjacent().remove(toNode.getValue())
        
        for fromNode in fromVertex.getAdjacent():
            if fromNode.getValue() == toVertex:
                fromNode.getAdjacent().remove(fromNode.getValue())
        
        # Remove from Edge list
        for edgeNode in self.edges:
            if (edgeNode.getValue().getTo() == toVertex) and (edgeNode.getValue().getFrom() == fromVertex):
                self.edges.remove(edgeNode.getValue())
            elif (edgeNode.getValue().getTo() == fromVertex) and (edgeNode.getValue().getFrom() == toVertex):
                self.edges.remove(edgeNode.getValue())
        return

        
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
        return
            

    def displayAsMatrix(self):
        print("\nAdjacency Matrix: ")
        print(" ", end="")
        copyOfList = LL.DSADoublyLinkedList()
        for v in self.vertices:
            print(" ", v.getValue().getLabel(), end="")
            copyOfList.insertLast(v.getValue())
        print("")
        
        for v in self.vertices:
            print(v.getValue().getLabel(), " ", end="")
            for v2 in copyOfList:
                if self.isAdjacent(v.getValue().getLabel(), v2.getValue().getLabel()):
                    print("1  ", end="")
                else:
                    print("0  ", end="")
            print("")
        print("")


    def breadthFirstSearch(self, label):
        T = sq.DSAQueue()
        Q = sq.DSAQueue()
        for node in self.vertices:
            node.getValue().clearVisited()
        for vertex in self.vertices:
            if vertex.getValue().getLabel() == label:
                v = vertex.getValue()
            else:
                raise ValueError("Starting vertex does not exist")
        v.setVisited()
        Q.enqueue(v)
        while not Q.isEmpty():
            v = Q.dequeue()
            for w in v.getAdjacent():
                if w.getValue().getVisited() == False:
                    T.enqueue(v.getLabel())
                    T.enqueue(w.getValue().getLabel())
                    w.getValue().setVisited()
                    Q.enqueue(w.getValue())
        print("\nBreadth First Search:")
        while not T.isEmpty():
            print(T.dequeue())

    def depthFirstSearch(self, label):
        T = sq.DSAQueue()
        S = sq.DSAStack()
        for node in self.vertices:
            node.getValue().clearVisited()
        for vertex in self.vertices:
            if vertex.getValue().getLabel() == label:
                v = vertex.getValue()
            else:
                raise ValueError("Starting vertex does not exist")
        v.setVisited()
        S.push(v)
        while not S.isEmpty():
            for w in v.getAdjacent():
                if w.getValue().getVisited() == False:
                    T.enqueue(v.getLabel())
                    T.enqueue(w.getValue().getLabel())
                    w.getValue().setVisited()
                    S.push(w.getValue())
                    v = w.getValue()
            v = S.pop()
        print("\nDepth First Search:")
        while not T.isEmpty():
            print(T.dequeue())
