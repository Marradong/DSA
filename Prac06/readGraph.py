import graph
import sys


def usage():
    print(" Usage: py readGraph.py x")
    print("        where")
    print("        x is  the file to be read in")


def __main__():
    if len(sys.argv) != 2:
        usage()
    else:
        try:
            fileOpen = open(sys.argv[1], "r")
            fileLines = fileOpen.readlines()
            DSAgraph = graph.DSAGraph()
            for line in fileLines:
                line = line.rstrip("\n")
                vertices = line.split(" ")
                if not DSAgraph.hasVertex(vertices[0]):
                    DSAgraph.addVertex(vertices[0], vertices[0])
                
                if not DSAgraph.hasVertex(vertices[1]):
                    DSAgraph.addVertex(vertices[1], vertices[1])
                
                DSAgraph.addEdge(vertices[0], vertices[1])
            DSAgraph.displayAsList()
            DSAgraph.displayAsMatrix()
            fileOpen.close()
        except:
                print("file could not be opened!")
    


if __name__ == "__main__":
    __main__()