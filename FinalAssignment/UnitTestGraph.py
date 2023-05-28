from ClassDefinitions import graph

def __main__():
    print("Initialising Graph")
    newGraph = graph.DSAGraph()

    print("\nAdding the following vertices to graph")
    print("A")
    newGraph.addVertex("A", "A")
    print("B")
    newGraph.addVertex("B", "B")
    print("C")
    newGraph.addVertex("C", "C")
    print("D")
    newGraph.addVertex("D", "D")

    print("\nAdding the following edges to graph")
    print("A<->B 1.5")
    newGraph.addEdge("A", "B", 1)
    print("A<->C 2")
    newGraph.addEdge("A", "C", 3)
    print("A<->D 1.5")
    newGraph.addEdge("A", "D", 1)
    print("B<->C 1.5")
    newGraph.addEdge("B", "C", 1)
    print("B<->D 2")
    newGraph.addEdge("B", "D", 0.5)
    print("C<->D 1.5")
    newGraph.addEdge("C", "D", 1)

    newGraph.displayAsList()

    print("\nDepth first search starting at A")
    print("Path: ", newGraph.depthFirstSearch("A"))

    print("\nUnweighted breadth first search from A to C")
    print("Path: ", newGraph.breadthFirstSearch("A", "C"))

    print("\nWeighted breadth first search from A to C")
    path, distance = newGraph.doDijSearch("A", "C")
    print("Path: ", path, " Distance: ", distance)

    print("\nNearest neighbour search")
    print("Path: ", newGraph.nearestNeighbour("A"), "\n")


if __name__ == "__main__":
    __main__()