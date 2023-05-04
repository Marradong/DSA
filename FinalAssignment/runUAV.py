import sys
import numpy as np
import graph
import hash

# region Global Variables
LocFileIDX = 1
DataFileIDX = 2
risk_matrix = np.array([[[0, 1, 2], [1, 3, 4], [2, 4, 5]], [[1, 3, 4], [3, 6, 7], [4, 7, 8]], [[2, 4, 5], [4, 7, 8], [5, 8, 9]]])
# endregion

# region Function Definitions
def usage():
    print(" Usage: py runUAV.py x y")
    print("        where")
    print("        x is the name of the file containing the locations")
    print("        y is the name of the file containing the UAV data")

def printCommands():
    print("\nHere is a list of valid commands (command - description): ")
    print("           ds - Display Map")
    print("           il - Insert Location")
    print("           dl - Delete Location")
    print("           sl - Search Location/s")
    print("           it - Provide Itinerary")
    print("           cm - Close Menu")


def getRisk(temperature, humidity, windSpeed):
    if (humidity < 0):
        print("Incorrect Humidity! Must be 0 or above")
    elif (windSpeed < 0):
        print("Incorrect Wind Speed! Must be 0 or above")
    elif temperature < 25:
        print("Incorrect Temperature! Must be 25 or above")
    else:
        return _getRisk(temperature, humidity, windSpeed)

def _getRisk(temperature, humidity, windSpeed):
    if(25 <= temperature <= 32):
        tIDX = 0
    elif(33 <= temperature <= 40):
        tIDX = 1
    elif(temperature >= 41):
        tIDX = 2
    
    if(humidity >= 51):
        hIDX = 0
    elif(31 <= humidity <= 50):
        hIDX = 1
    elif(humidity <= 30):
        hIDX = 2
    
    if(windSpeed <= 40):
        wIDX = 0
    elif(41 <= windSpeed <= 55):
        wIDX = 1
    elif(windSpeed >= 56):
        wIDX = 2
    
    return risk_matrix[tIDX][hIDX][wIDX]
# endregion

# region Main Method

def __main__():
    if len(sys.argv) != 3:
        usage()
    else:
        # region TASK1 - Location From File
        lfileName = sys.argv[LocFileIDX]
        try:
            locationFile = open(lfileName, "r")
            graphDimensions = locationFile.readline().split()
            numVerticies = graphDimensions[0]
            numEdges = graphDimensions[1]
            locationGraph = graph.DSAGraph() 
            for i in range(numEdges):
                newEdge = locationFile.readline().strip("\n").split()
                locationGraph.addVertex(newEdge[0], newEdge[2])
                locationGraph.addVertex(newEdge[1], newEdge[2])
                locationGraph.addEdge(newEdge[0],newEdge[1], newEdge[2])
        except IOError as e:
            print(e)
        # endregion
        # region TASK4 - Data From File
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
        # endregion
        # region Menu
        printCommands()
        userCommand = ""

        while (userCommand != "cm"):
            userCommand = str(input("\nPlease enter a valid command: "))

            # region TASK1 - display adjacency list
            if userCommand == "ds":
                locationGraph.displayAsList()
            # endregion
            # region TASK3 - insert operation
            elif userCommand == "il":
                ...
            # endregion
            # region TASK3 - delete operation
            elif userCommand == "dl":
                ...
            # endregion
            # region TASK3 - search operation
            elif userCommand == "sl":
                # 2 DFS explore entire graph
                # 2 BFS explore shortest path
                ...
            # endregion
            # region TASK6 - UAV itinerary
            elif userCommand == "it":
                ...
            # endregion
            else:
                print("Invalid command please see list below")
                printCommands()

        # endregion


if __name__ == "__main__":
    __main__()
# endregion
