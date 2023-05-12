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
    print("           ic - Insert Connection")
    print("           dl - Delete Location")
    print("           dc - Delete Connection")
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
            numEdges = int(graphDimensions[1])
            locationGraph = graph.DSAGraph() 
            for i in range(numEdges):
                newEdge = locationFile.readline().strip("\n").split()
                locationGraph.addVertex(newEdge[0], newEdge[0])
                locationGraph.addVertex(newEdge[1], newEdge[1])
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
                uavData.put(str(key), value)
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
            # region TASK3 - insert location operation
            elif userCommand == "il":
                newLocLbl = str(input("\nPlease enter a label for the new location: "))
                locationGraph.addVertex(newLocLbl, newLocLbl)

                print("Please provide location data below")
                temperature  = str(input("\nPlease enter the temperature: "))
                humidity  = str(input("\nPlease enter the humidity: "))
                windSpeed  = str(input("\nPlease enter the wind : "))
                value = str(temperature) + "," + str(humidity) + "," + str(windSpeed)
                uavData.put(newLocLbl, value)

                print("\nLocation Added!")

                edgeVertex = str(input("\nPlease enter an existing location to add a connection: "))
                edgeLength = str(input("\nPlease enter the distance between locations: "))
                locationGraph.addEdge(newLocLbl, edgeVertex, edgeLength)

                print("\nConnection Added!")

                addAnotherEdge = str(input("\nWould you like to add another connection? (Yes/No): "))
                while addAnotherEdge == "Yes":
                    edgeVertex = str(input("\nPlease enter an existing location to add a connection: "))
                    edgeLength = str(input("\nPlease enter the distance between locations: "))
                    locationGraph.addEdge(newLocLbl, edgeVertex, edgeLength)
                    addAnotherEdge = str(input("\nWould you like to add another connection? (Yes/No): "))
            # endregion
            # region TASK3 - insert connection operation
            elif userCommand == "ic":
                fromVertex = str(input("\nPlease enter the first location of the connection: "))
                toVertex = str(input("\nPlease enter the second location of the connection: "))
                edgeLength = str(input("\nPlease enter the distance between locations: "))
                locationGraph.addEdge(toVertex, fromVertex, edgeLength)

                print("\nConnection Added!")
            # endregion
            # region TASK3 - delete location
            elif userCommand == "dl":
                locationLbl = str(input("\nPlease enter a location to delete: "))
                locationGraph.deleteVertex(locationLbl)
                uavData.remove(str(ord(locationLbl)))
            # endregion
            # region TASK3 - delete connection
            elif userCommand == "dc":
                fromLabel = str(input("\nPlease enter the first location of connection: "))
                toLabel = str(input("\nPlease enter the second location of connection: "))
                locationGraph.deleteEdge(toLabel, fromLabel)
                locationGraph.deleteEdge(fromLabel, toLabel)
            # endregion
            # region TASK3 - search operation
            elif userCommand == "sl":
                dfsOrbfs = str(input("\nWould you like to search the entire map or between 2 locations? (entire/between): "))
                # 2 DFS explore entire graph
                if dfsOrbfs == "entire":
                    startLbl = str(input("\nPlease enter the starting location: "))
                    try:
                        graphQueue = locationGraph.depthFirstSearch(startLbl)
                    except ValueError:
                        print("Starting location does not exist")
                # 2 BFS explore shortest path
                elif dfsOrbfs == "between":
                    startLbl = str(input("\nPlease enter the starting location: "))
                    endLbl = str(input("\nPlease enter the end location: "))
                    shortestPath = locationGraph.breadthFirstSearch(startLbl, endLbl)
                else:
                    print("Incorrect search method please enter either 'entire' or 'between'")
            # endregion
            # region TASK6 - UAV itinerary
            elif userCommand == "it":
                ...
            # endregion
            elif userCommand == "cm":
                print("Closing Menu")
            else:
                print("Invalid command please see list below")
                printCommands()

        # endregion


if __name__ == "__main__":
    __main__()
# endregion
