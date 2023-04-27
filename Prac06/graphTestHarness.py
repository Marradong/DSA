import graph


def __main__():

    print("\nCreating the Below Graph\n")
    print("\tA - B")
    print("\t|   |")
    print("\tD - C")


    DSAgraph = graph.DSAGraph()
    print("\nAdding Vertex A with value 1")
    DSAgraph.addVertex("A",1)
    print("Adding Vertex B with value 2")
    DSAgraph.addVertex("B",2)
    print("Adding Vertex C with value 3")
    DSAgraph.addVertex("C",3)
    print("Adding Vertex D with value 4")
    DSAgraph.addVertex("D",4)

    print("\nAdding edge between A and B")
    DSAgraph.addEdge("A","B")
    print("Adding edge between B and C")
    DSAgraph.addEdge("B","C")
    print("Adding edge between C and D")
    DSAgraph.addEdge("C","D")
    print("Adding edge between D and A")
    DSAgraph.addEdge("D","A")

    DSAgraph.displayAsList()
    DSAgraph.displayAsMatrix()

    print("\nDoes Graph have vertex A: ",DSAgraph.hasVertex("A"))
    print("Does Graph have vertex E: ",DSAgraph.hasVertex("E"))

    print("\nIs vertex A adjacent to vertex B: ",DSAgraph.isAdjacent("A","B"))
    print("Is vertex A adjacent to vertex C: ",DSAgraph.isAdjacent("A","C"))

    print("\nVertex Count: ", DSAgraph.getVertexCount())
    print("Edge Count: ", DSAgraph.getEdgeCount())

    print("\nGet vertex A then get label: ", DSAgraph.getVertex("A").getLabel())
    print("Get vertex A then get value: ", DSAgraph.getVertex("A").getValue())

    print("\nConvert vertex A to string: ", DSAgraph.getVertex("A").toString())

    adjacencyList = str(DSAgraph.getVertex("A").getLabel()) + " | "
    for item in DSAgraph.getVertex("A").getAdjacent():
        adjacencyList = adjacencyList + str(item.getValue().getLabel()) + " "
    print("\nGet vertex A adjacency list: ", adjacencyList)

    print("\nHas vertex A been visited: ", DSAgraph.getVertex("A").getVisited())
    print("Visit vertex A")
    DSAgraph.getVertex("A").setVisited()
    print("Has vertex A been visited: ", DSAgraph.getVertex("A").getVisited())
    print("Unvisit vertex A")
    DSAgraph.getVertex("A").clearVisited()
    print("Has vertex A been visited: ", DSAgraph.getVertex("A").getVisited(), "\n")


if __name__ == "__main__":
    __main__()