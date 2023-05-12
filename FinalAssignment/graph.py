import linkedList as LL
import stackQueue as sq
import hash


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
        
        for linkNode in vertexToDelete.getAdjacent():
            self.deleteEdge(vertexToDelete.getLabel(), linkNode.getValue().getLabel())

        self.vertices.remove(vertexToDelete.getValue())
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
        if toVertex != None and fromVertex != None:
            for toNode in toVertex.getAdjacent():
                if toNode.getValue().getValue() == fromVertex.getValue():
                    toNode.getValue().getAdjacent().remove(toVertex.getValue())
                    toVertex.getAdjacent().remove(toNode.getValue().getValue())
            
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

    
    def depthFirstSearch(self, label):
        T = sq.DSAQueue()
        S = sq.DSAStack()
        for node in self.vertices:
            node.getValue().clearVisited()

        for vertex in self.vertices:
            if vertex.getValue().getLabel() == label:
                v = vertex.getValue()
        if v == None:
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
        return T


    def doBFS(self, startLabel):
        Q = sq.DSAQueue()

        for node in self.vertices:
            node.getValue().clearVisited()

        for vertex in self.vertices:
            if vertex.getValue().getLabel() == startLabel:
                v = vertex.getValue()
        
        try:
            v.setVisited()
            Q.enqueue(v)
            prevVertices = hash.DSADoubleHashTable(self.vertices._count)
            i = 0
            while not Q.isEmpty():
                v = Q.dequeue()
                i == i + 1
                for w in v.getAdjacent():
                    if w.getValue().getVisited() == False:
                        w.getValue().setVisited()
                        Q.enqueue(w.getValue())
                        prevVertices.put(w.getValue().getLabel(), v.getLabel())
        except UnboundLocalError: 
            print("Starting location does not exist")
            prevVertices = -1
        return prevVertices        
    
    def buildPath(self, startLabel, endLabel, prevVertices: hash.DSADoubleHashTable):
        endBuild = False
        shortestPath = str(endLabel)
        prevVertex = endLabel
        while not endBuild:
            try:
                prevVertex = prevVertices.get(prevVertex)
                shortestPath = str(prevVertex) + "->" + shortestPath
            except ValueError:
                endBuild = True
        if shortestPath == endLabel:
            shortestPath = "End location not found"
        elif shortestPath[0] != startLabel:
            shortestPath = "No path found"

        return shortestPath
    
    def breadthFirstSearch(self, startLabel, endLabel):
        prevVertices = self.doBFS(startLabel)
        if prevVertices != -1:
            shortestPath = self.buildPath(startLabel, endLabel, prevVertices)
            print("Shortest Path between: ", startLabel, " and ", endLabel, ": ", shortestPath)
        return
            

