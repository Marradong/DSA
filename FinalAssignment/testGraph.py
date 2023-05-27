import graph

def __main__():
    testGraph = graph.DSAGraph()
    testGraph.addVertex("A", "A")
    testGraph.addVertex("B", "B")
    testGraph.addVertex("C", "C")
    testGraph.addVertex("D", "D")
    testGraph.addVertex("E", "E")
    testGraph.addVertex("F", "F")

    testGraph.addEdge("A", "B", 2)
    testGraph.addEdge("A", "C", 1)
    testGraph.addEdge("A", "D", 3)
    testGraph.addEdge("A", "E", 1)
    testGraph.addEdge("A", "F", 2)

    testGraph.addEdge("B", "F", 1)
    testGraph.addEdge("B", "E", 3)
    testGraph.addEdge("B", "D", 1)
    testGraph.addEdge("B", "C", 2)

    testGraph.addEdge("C", "F", 3)
    testGraph.addEdge("C", "E", 1)
    testGraph.addEdge("C", "D", 2)

    testGraph.addEdge("D", "F", 1)
    testGraph.addEdge("D", "E", 2)

    testGraph.addEdge("E", "F", 2)

    path = testGraph.nearestNeighbour()
    print(path)

if __name__ == "__main__":
    __main__()