
# read in graph from file:
# - Input file in command line
# - First line has number of verticies and edges
# - Each line has one edge, two verticies and a value

# CODE:
import sys
import numpy as np
from Prac06 import graph
from Prac07 import hash

LocFileIDX = 1
DataFileIDX = 2

lfileName = sys.argv[LocFileIDX]
try:
    locationFile = open(LocFileIDX, "r")
    graphDimensions = locationFile.readline().split()
    numVerticies = graphDimensions[0]
    numEdges = graphDimensions[1]
    locationGraph = graph.DSAGraph() 
    for i in range(numEdges):
        newEdge = locationFile.readline().split()
        locationGraph.addVertex(newEdge[0])
        locationGraph.addVertex(newEdge[1])
        # TODO: EDIT GRAPH TO INCLUDE EDGE
        locationGraph.addEdge(newEdge[0],newEdge[1])
except IOError as e:
    print(e)

# Identify shortest path
# - Input two verticies
# - Use Breadth First Search
# - Output data of each vertex and the distance

# Interactive Menu
# - Allow Insert, Remove and Delete of verticies in the graph

# Storing UAV data
# - Use a hash table
# - Compare the use of a Hash table instead of an array
# - read in data from file
#     . Input file in command line
#     . Each line has one vertex, one temperature, one humitity and one wind speed

dfileName = sys.argv[DataFileIDX]
try:
    dataFile = open(dfileName, "r")
    uavData = hash.DSADoubleHashTable(10)
    locationData = dataFile.readline()
    while locationData:
        vertex = locationData.split()[0]
        temperature = locationData.split()[1]
        humidity = locationData.split()[2]
        windSpeed = locationData.split()[3]
        key = ord(vertex)
        value = str(temperature) + "," + str(humidity) + "," + str(windSpeed)
        uavData.put(key, value)
        locationData = dataFile.readline()
except IOError as e:
    print(e)

# Track high risk areas
# - Use Heap with the location (graph vertex) and risk factor (priority)
# - Replace locations with updated risk value
# - Risk Thresholds:
#     . Temperature
#         + 25 to 32 = LOW
#         + 33 to 40 = MEDIUM
#         + 41 or more = HIGH
#     . Humidity
#         + 51 or more = LOW
#         + 31 to 50 = MEDIUM
#         + 30 or less = HIGH
#     . Wind Speed
#         + 40 or less = LOW
#         + 41 to 55 = MEDIUM
#         + 56 or more = HIGH
# LOW LOW LOW = 0
# LOW LOW MED = 1
# LOW LOW HIGH = 2
# LOW MED MED = 3
# LOW MED HIGH = 4
# LOW HIGH HIGH = 5
# MED MED MED = 6
# MED MED HIGH = 7
# MED HIGH HIGH = 8
# HIGH HIGH HIGH = 9
# 
# 2 4 5 | 4 7 8 | 5 8 9
# 1 3 4 | 3 6 7 | 4 7 8
# 0 1 2 | 1 3 4 | 2 4 5 
# 
# Provide itinerary
# - Provide distances and time between locations for UAV
# - Use other algorithms (not BFS or DFS)
