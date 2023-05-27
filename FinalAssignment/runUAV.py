import sys
import numpy as np
import graph
import hash
import heap

# region Global constants
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

def createKey(lbl):
    return str(ord(lbl))

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

def loadLocations(fileName):
    with open(fileName, "r") as locationFile:
        graphDimensions = locationFile.readline().split()
        numVerticies = graphDimensions[0]
        numEdges = int(graphDimensions[1])
        locationGraph = graph.DSAGraph() 
        for i in range(numEdges):
            newEdge = locationFile.readline().strip("\n").split()
            locationGraph.addVertex(newEdge[0], newEdge[0])
            locationGraph.addVertex(newEdge[1], newEdge[1])
            locationGraph.addEdge(newEdge[0],newEdge[1], newEdge[2])
    return locationGraph

def loadData(fileName):
    with open(fileName, "r") as dataFile:
        uavData = hash.DSADoubleHashTable(10)
        locationData = dataFile.readline()
        while locationData:
            vertex = locationData.split()[0]
            temperature = locationData.split()[1]
            humidity = locationData.split()[2]
            windSpeed = locationData.split()[3]
            value = str(temperature) + "," + str(humidity) + "," + str(windSpeed)
            uavData.put(createKey(vertex), value)
            locationData = dataFile.readline()
    return uavData


def getData(uavData, riskHeap, path):
    locations = path.split("->")
    print("Location : Temperature, Humidity, Wind Speed")
    for i in range(len(locations)):
        data = uavData.get(createKey(locations[i]))
        splitData = data.split(",")
        risk = getRisk(int(splitData[0]), int(splitData[1]), int(splitData[2]))
        value = str(locations[i]) + ":" + str(splitData[0]) + "," + str(splitData[1]) + "," + str(splitData[2])
        riskHeap.add(risk, locations[i])
        print(value, " risk: ", risk)
    return riskHeap

# endregion

def runMenu(locationGraph, uavData, userCommand):
    ...


# region Main Method

def __main__():
    if len(sys.argv) != 3:
        usage()
    else:
        
        lfileName = sys.argv[LocFileIDX]
        dfileName = sys.argv[DataFileIDX]
        try:
            # region TASK1 - Location From File
            locationGraph = loadLocations(lfileName)
            # endregion
            # region TASK4 - Data From File
            uavData = loadData(dfileName)
            # endregion
            riskheap = heap.DSAHeap()
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
                    while locationGraph.hasVertex(newLocLbl):
                        print("Location already exists!")
                        newLocLbl = str(input("Please enter a label for the new location: "))

                    locationGraph.addVertex(newLocLbl, newLocLbl)

                    print("\nPlease provide location data below")
                    temperature = 0.0
                    while temperature < 25.0:
                        try:
                            temperature  = float(input("Please enter the temperature (must be >= 25.0): "))
                        except ValueError:
                            print("Please enter a floating point value!")
                            temperature = 0.0

                    humidity = -1.0
                    while humidity < 0.0 or humidity > 100.0:
                        try:
                            humidity  = float(input("Please enter the humidity (0-100 inclusive): "))
                        except ValueError:
                            print("Please enter a floating point value!")
                            humidity = -1.0

                    windSpeed = -1.0
                    while windSpeed < 0.0:
                        try:
                            windSpeed  = float(input("Please enter the wind (must be >= 0): "))
                        except ValueError:
                            print("Please enter a floating point value!")
                            windSpeed = -1.0

                    value = str(temperature) + "," + str(humidity) + "," + str(windSpeed)
                    uavData.put(createKey(newLocLbl), value)

                    print("\nLocation Added!")

                    edgeVertex = str(input("\nPlease enter an existing location to add a connection: "))
                    while not locationGraph.hasVertex(edgeVertex):
                        print("Location does not exists!")
                        edgeVertex = str(input("Please enter an existing location to add a connection: "))

                    isFloat = False
                    while not isFloat:
                        try:
                            edgeLength = float(input("\nPlease enter the distance between locations: "))
                            isFloat = True
                        except ValueError:
                            print("Please enter a floating point value!")
                            isFloat = False

                    locationGraph.addEdge(newLocLbl, edgeVertex, edgeLength)

                    print("\nConnection Added!")

                    addAnotherEdge = str(input("\nWould you like to add another connection? (Yes/No): "))
                    while addAnotherEdge == "Yes":
                        edgeVertex = str(input("\nPlease enter an existing location to add a connection: "))
                        while not locationGraph.hasVertex(edgeVertex):
                            print("Location does not exists!")
                            edgeVertex = str(input("Please enter an existing location to add a connection: "))

                        isFloat = False
                        while not isFloat:
                            try:
                                edgeLength = float(input("\nPlease enter the distance between locations: "))
                                isFloat = True
                            except ValueError:
                                print("Please enter a floating point value!")
                                isFloat = False

                        locationGraph.addEdge(newLocLbl, edgeVertex, edgeLength)
                        addAnotherEdge = str(input("\nWould you like to add another connection? (Yes/No): "))
                # endregion
                # region TASK3 - insert connection operation
                elif userCommand == "ic":
                    fromVertex = str(input("\nPlease enter the first existing location of the connection: "))
                    while not locationGraph.hasVertex(fromVertex):
                        print("Location does not exists!")
                        fromVertex = str(input("Please enter the first existing location of the connection: "))

                    toVertex = str(input("Please enter the second existing location of the connection: "))
                    while not locationGraph.hasVertex(toVertex):
                        print("\nLocation does not exists!")
                        toVertex = str(input("Please enter the second existing location of the connection: "))

                    isFloat = False
                    while not isFloat:
                        try:
                            edgeLength = float(input("Please enter the distance between locations: "))
                            isFloat = True
                        except ValueError:
                            print("Please enter a floating point value!")
                            isFloat = False

                    locationGraph.addEdge(toVertex, fromVertex, edgeLength)

                    print("\nConnection Added!")
                # endregion
                # region TASK3 - delete location
                elif userCommand == "dl":
                    locationLbl = str(input("\nPlease enter a location to delete: "))
                    while not locationGraph.hasVertex(locationLbl):
                        print("Location does not exists!")
                        locationLbl = str(input("Please enter a location to delete: "))

                    locationGraph.deleteVertex(locationLbl)
                    uavData.remove(createKey(locationLbl))
                    print("\nLocation and Data Deleted!")
                # endregion
                # region TASK3 - delete connection
                elif userCommand == "dc":
                    fromLabel = str(input("\nPlease enter the first existing location of connection: "))
                    while not locationGraph.hasVertex(fromLabel):
                        print("Location does not exists!")
                        fromLabel = str(input("Please enter the first existing location of connection: "))

                    toLabel = str(input("\nPlease enter the second existing location of connection: "))
                    while not locationGraph.hasVertex(toLabel):
                        print("\nLocation does not exists!")
                        toLabel = str(input("\nPlease enter the second existing location of connection: "))

                    locationGraph.deleteEdge(toLabel, fromLabel)
                    locationGraph.deleteEdge(fromLabel, toLabel)
                # endregion
                # region TASK3 - search operation
                elif userCommand == "sl":
                    dfsOrbfs = str(input("\nWould you like to search the entire map or between 2 locations? (entire/between): "))
                    # 2 DFS explore entire graph
                    if dfsOrbfs == "entire":
                        startLbl = str(input("\nPlease enter the starting location: "))
                        while not locationGraph.hasVertex(startLbl):
                            print("\nLocation does not exists!")
                            startLbl = str(input("\nPlease enter the starting location: "))
                        try:
                            entirePath = locationGraph.depthFirstSearch(startLbl)
                            if entirePath != "Starting vertex does not exist":
                                riskheap = getData(uavData, riskheap, entirePath)
                            else:
                                print(entirePath)
                        except ValueError:
                            print("Starting location does not exist")
                    # 2 BFS explore shortest path
                    elif dfsOrbfs == "between":
                        startLbl = str(input("\nPlease enter the starting location: "))
                        while not locationGraph.hasVertex(startLbl):
                            print("\nLocation does not exists!")
                            startLbl = str(input("\nPlease enter the starting location: "))

                        endLbl = str(input("\nPlease enter the end location: "))
                        while not locationGraph.hasVertex(endLbl):
                            print("\nLocation does not exists!")
                            endLbl = str(input("\nPlease enter the end location: "))

                        shortestPath = locationGraph.breadthFirstSearch(startLbl, endLbl)

                        print("\nDijkstra")
                        path, distance = locationGraph.doDijSearch(startLbl, endLbl)
                        if path != "No path found" and path != "End location not found" and path != "Starting location does not exist":
                            riskheap = getData(uavData, riskheap, path)

                    else:
                        print("Incorrect search method please enter either 'entire' or 'between'")
                # endregion
                # region TASK6 - UAV itinerary
                elif userCommand == "it":
                    if riskheap._count == 1:
                        ...
                    elif riskheap._count == 0:
                        print("\nNo locations explored! Please use the search function to add location data")
                    else:
                        riskGraph = graph.DSAGraph()
                        for i in range(riskheap._count):
                            for j in range(i, riskheap._count):
                                fromRiskLabel = riskheap[i].getValue()
                                toRiskLabel = riskheap[j].getValue()
                                riskGraph.addVertex(fromRiskLabel)
                                riskGraph.addVertex(toRiskLabel)
                                path, distance = locationGraph.doDijSearch(fromRiskLabel, toRiskLabel)
                                riskGraph.addEdge(fromRiskLabel, toRiskLabel, distance)
                # endregion
                elif userCommand == "cm":
                    print("Closing Menu")
                else:
                    print("Invalid command please see list below")
                    printCommands()
            # endregion
        except IOError as e:
            print("Error loading file: ", e)
        
if __name__ == "__main__":
    __main__()
# endregion
