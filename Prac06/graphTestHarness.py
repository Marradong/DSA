import graph

def __main__():
    DSAgraph = graph.DSAGraph()
    DSAgraph.addVertex("A","A")
    DSAgraph.addVertex("B","B")
    DSAgraph.addVertex("C","C")
    DSAgraph.addVertex("D","D")
    DSAgraph.addVertex("E","E")
    DSAgraph.addVertex("F","F")
    DSAgraph.addVertex("G","G")
    DSAgraph.addEdge("A","B","AB","AB")
    DSAgraph.addEdge("A","D","AD","AD")
    DSAgraph.addEdge("A","C","AC","AC")
    DSAgraph.addEdge("B","E","BE","BE")
    DSAgraph.addEdge("D","F","DF","DF")
    DSAgraph.addEdge("D","F","DF","DF")
    DSAgraph.addEdge("E","G","EG","EG")
    DSAgraph.addEdge("E","F","EF","EF")
    DSAgraph.addEdge("F","G","FG","FG")



if __name__ == "__main__":
    __main__()