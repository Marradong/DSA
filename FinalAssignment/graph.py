import linkedList as LL
import stackQueue as sq
import hash
import sys


class DSAGraphEdge():
    
    def __init__(self, toVertex, fromVertex, inValue):
        self._to = toVertex
        self._from = fromVertex
        self._value = inValue
    
    def getValue(self):
        return self._value

    def getTo(self):
        return self._to
    
    def getFrom(self):
        return self._from

class DSAGraphVertex():

    def __init__(self, inLabel, inValue):
        self._label = inLabel
        self._value = inValue
        self._links = LL.DSADoublyLinkedList()
        self._visited = False
        self._distance = sys.maxsize
        self._prev = None

    def getDist(self):
        return self._distance
    
    def getPrev(self):
        return self._prev

    def setDist(self, dist):
        self._distance = dist
        return
    
    def setPrev(self, prev):
        self._prev = prev
        return 

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
            new1Edge = DSAGraphEdge(vertex1, vertex2, value)
            self.edges.insertLast(new1Edge)
            new2Edge = DSAGraphEdge(vertex2, vertex1, value)
            self.edges.insertLast(new2Edge)
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
    
    def getEdge(self, fromLabel, toLabel):
        gotEdge = None
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        for node in self.edges:
            edge = node.getValue()
            if edge.getTo().getValue() == toVertex.getValue() and edge.getFrom().getValue() == fromVertex.getValue():
                gotEdge = edge.getValue()
            elif edge.getTo() == fromVertex and edge.getFrom() == toVertex:
                gotEdge = edge.getValue()
        return gotEdge

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

    
    def depthFirstSearch(self, startLabel):
        T = sq.DSAQueue()
        S = sq.DSAStack()
        for node in self.vertices:
            node.getValue().clearVisited()

        for vertex in self.vertices:
            if vertex.getValue().getLabel() == startLabel:
                v = vertex.getValue()
        
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
        path = ""
        for item in T:
            path = path + "->" + str(T.dequeue())
        path = path.lstrip("->")   
        return path


    def doBFS(self, startLabel):
        Q = sq.DSAQueue()

        for node in self.vertices:
            node.getValue().clearVisited()

        for vertex in self.vertices:
            if vertex.getValue().getLabel() == startLabel:
                v = vertex.getValue()
        
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
        startLength = len(startLabel)
        if shortestPath[0:startLength] != startLabel:
            shortestPath = "No path found"

        return shortestPath
    
    def breadthFirstSearch(self, startLabel, endLabel):
        prevVertices = self.doBFS(startLabel)
        shortestPath = self.buildPath(startLabel, endLabel, prevVertices)
        return shortestPath
            
    def dijkstraSearch(self, startLabel):
        Q = sq.DSAQueue()
        for node in self.vertices:
            node.getValue().clearVisited()
            node.getValue().setDist(sys.maxsize)
            node.getValue().setPrev(None)

        for vertex in self.vertices:
            if vertex.getValue().getLabel() == startLabel:
                v = vertex.getValue()
        
        v.setDist(0)
        Q.enqueue(v)
        while not Q.isEmpty():
            v = Q.dequeue()
            if v.getVisited() == False:
                v.setVisited()
                for w in v.getAdjacent():
                    newVertex = w.getValue()
                    if newVertex.getVisited() == False:
                        distance = float(v.getDist()) + float(self.getEdge(v.getLabel(), newVertex.getLabel()))
                        if distance < newVertex.getDist():
                            newVertex.setDist(distance)
                            newVertex.setPrev(v)
                            Q.enqueue(newVertex)
        return
    
    def doDijSearch(self, startLabel, endLabel):
        self.dijkstraSearch(startLabel)
        endVertex = self.getVertex(endLabel)

        endBuild = False
        path = str(endVertex.getLabel())

        for node in self.vertices:
            node.getValue().clearVisited()
        endVertex.setVisited()
        prevVertex = endVertex.getPrev()
        while prevVertex != None and prevVertex.getVisited() == False:
            prevVertex.setVisited()
            if prevVertex.getLabel() == startLabel:
                path = str(startLabel) + '->' + path
                endBuild = True
                distance = endVertex.getDist()
            else:
                path = str(prevVertex.getLabel()) + '->' + path
                prevVertex = prevVertex.getPrev()
        if not endBuild:
            path = "No path found"
            distance = 0
        return path, distance

    def nearestNeighbour(self):
        unvisited = LL.DSADoublyLinkedList()
        for node in self.vertices:
            unvisited.insertLast(node.getValue())
        
        v = unvisited.peekFirst().getValue()
        unvisited.remove(v.getValue())
        path = str(v.getLabel())
        while not unvisited.isEmpty():
            closest = None
            for u in unvisited:
                u = u.getValue()
                if closest == None:
                    closest = u
                elif float(self.getEdge(v.getLabel(), closest.getLabel())) > float(self.getEdge(v.getLabel(), u.getLabel())):
                    closest = u
            unvisited.remove(closest.getValue())
            v = closest
            path = path + "->" + str(closest.getLabel())
        return path


