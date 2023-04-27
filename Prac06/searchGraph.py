import graph


def __main__():
    print("Initialising graph 1")
    DSAgraph1 = graph.DSAGraph()
    DSAgraph1.addVertex("A", "A")
    DSAgraph1.addVertex("B", "B")
    DSAgraph1.addVertex("C", "C")
    DSAgraph1.addVertex("D", "D")
    DSAgraph1.addVertex("E", "E")
    DSAgraph1.addVertex("F", "F")
    DSAgraph1.addVertex("G", "G")

    DSAgraph1.addEdge("A","B")
    DSAgraph1.addEdge("A","D")
    DSAgraph1.addEdge("A","C")
    DSAgraph1.addEdge("B","E")
    DSAgraph1.addEdge("D","C")
    DSAgraph1.addEdge("D","F")
    DSAgraph1.addEdge("E","F")
    DSAgraph1.addEdge("E","G")
    DSAgraph1.addEdge("F","G")  

    DSAgraph1.displayAsList()
    DSAgraph1.displayAsMatrix()
    DSAgraph1.breadthFirstSearch()
    DSAgraph1.depthFirstSearch()


    print("\nInitialising graph 2")
    DSAgraph2 = graph.DSAGraph()
    DSAgraph2.addVertex("A", "A")
    DSAgraph2.addVertex("B", "B")
    DSAgraph2.addVertex("C", "C")
    DSAgraph2.addVertex("D", "D")
    DSAgraph2.addVertex("E", "E")
    DSAgraph2.addVertex("F", "F")
    DSAgraph2.addVertex("G", "G")
    DSAgraph2.addVertex("H", "H")
    DSAgraph2.addVertex("I", "I")
    DSAgraph2.addVertex("J", "J")

    DSAgraph2.addEdge("A","B")
    DSAgraph2.addEdge("A","D")
    DSAgraph2.addEdge("A","C")
    DSAgraph2.addEdge("B","E")
    DSAgraph2.addEdge("C","E")
    DSAgraph2.addEdge("D","E")
    DSAgraph2.addEdge("D","F")
    DSAgraph2.addEdge("D","H")
    DSAgraph2.addEdge("E","G")
    DSAgraph2.addEdge("F","I") 
    DSAgraph2.addEdge("H","I")
    DSAgraph2.addEdge("H","G")
    DSAgraph2.addEdge("H","J")
    DSAgraph2.addEdge("G","J")
    DSAgraph2.addEdge("I","J")

    DSAgraph2.displayAsList()
    DSAgraph2.displayAsMatrix()
    DSAgraph2.breadthFirstSearch()
    DSAgraph2.depthFirstSearch()


if __name__ == "__main__":
    __main__()