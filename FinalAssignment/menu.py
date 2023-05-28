import utils
from ClassDefinitions import graph

def getItinerary(locationGraph, uavArray, riskheap):
    # case 1 - no locations have been explored
    if riskheap._count == 0:
        print("\nNo locations explored! Please use the search function to add location data")
    # case 2 - 1 location is at risk
    elif riskheap._count == 1:
        # iterate through the UAVs
        for i in range(len(uavArray)):
            # path from current location to at risk location
            path = str(uavArray[i].getLocation()) + "->" + str(riskheap._heap[0].getValue())
            print(f"Uav {i+1} Itinerary:", path)
    # case 3 - more than 1 location is at risk
    else:
        riskGraph = graph.DSAGraph()
        # iterate through all locations in heap
        for i in range(riskheap._count):
             # iterate through all locations in heap excluding previous locations
            for j in range(i, riskheap._count):
                # get the location labels
                fromRiskLabel = riskheap._heap[i].getValue()
                toRiskLabel = riskheap._heap[j].getValue()
                # add locations to new fully connected graph
                riskGraph.addVertex(fromRiskLabel, fromRiskLabel)
                riskGraph.addVertex(toRiskLabel, toRiskLabel)
                # get distance between vertices
                path, distance = locationGraph.doDijSearch(fromRiskLabel, toRiskLabel)
                # add connection to new fully connected graph
                riskGraph.addEdge(fromRiskLabel, toRiskLabel, distance)
        # iterate through UAVs
        for i in range(len(uavArray)):
            uavLabel = uavArray[i].getLocation()
            # add UAV location to fully connected graph
            riskGraph.addVertex(uavLabel, uavLabel)
            for item in riskGraph.vertices:
                vertex = item.getValue()
                # add connection to all vertices in graph
                if vertex.getLabel() != uavLabel:
                    path, distance = locationGraph.doDijSearch(uavLabel, vertex.getLabel())
                    riskGraph.addEdge(uavLabel, vertex.getLabel(), distance)
            # print UAV itinerary
            print(f"Uav {i+1} Itinerary:", riskGraph.nearestNeighbour(uavLabel))
            # remove the UAV location if it is not high risk
            if not riskheap.isAdded(uavLabel):
                riskGraph.deleteVertex(uavLabel)
    return locationGraph, uavArray, riskheap

def searchLocation(locationGraph, uavData, uavArray, riskheap):
    dfsOrbfs = str(input("\nWould you like to search the entire map or between 2 locations? (entire/between): "))
    # 2 DFS explore entire graph
    if dfsOrbfs == "entire":
        # prompt user to enter valid number of UAV
        uavNumber = -1
        while uavNumber < 1 or uavNumber > len(uavArray):
            try:
                print("\nValid UAV number must be between 1 and ", len(uavArray), " inclusive")
                uavNumber = int(input("Please enter the number of the searching UAV: "))
            except ValueError:
                print("Please enter an integer value!" )
                uavNumber = -1
        uavNumber = uavNumber - 1
        startLbl = uavArray[uavNumber].getLocation()
        # get path to search entire graph
        entirePath = locationGraph.depthFirstSearch(startLbl)
        print("Searching graph using DFS starting from: ", startLbl, " Path: ", entirePath)
        
        # look for unexplored nodes
        for item in locationGraph.vertices:
            if not item.getValue().getVisited():
                print("\nLocation: ", item.getValue().getLabel(), " was not visited! Please add connections to collect its data")
        # Update risk heap
        riskheap = utils.getData(uavData, riskheap, entirePath)
        # Update UAV location
        splitPath = entirePath.split("->")
        uavArray[uavNumber].setLocation(splitPath[-1])

    # 2 BFS explore shortest path
    elif dfsOrbfs == "between":
        # prompt user to enter valid number of UAV
        uavNumber = -1
        while uavNumber < 1 or uavNumber > len(uavArray):
            try:
                print("\nValid UAV number must be between 1 and ", len(uavArray), " inclusive")
                uavNumber = int(input("Please enter the number of the searching UAV: "))
            except ValueError:
                print("Please enter an integer value!" )
                uavNumber = -1
        uavNumber = uavNumber - 1
        startLbl = uavArray[uavNumber].getLocation()

        endLbl = str(input("\nPlease enter the end location: "))
        while not locationGraph.hasVertex(endLbl):
            print("Location does not exists!")
            endLbl = str(input("Please enter the end location: "))

        shortestPath = locationGraph.breadthFirstSearch(startLbl, endLbl)
        print("\nShortest Unweighted Path BFS")
        print("Shortest Path between: ", startLbl, " and ", endLbl, ": ", shortestPath)

        print("\nShortest Weighted Path BFS")
        path, distance = locationGraph.doDijSearch(startLbl, endLbl)
        print("Shortest Path: ", path, " Distance: ", distance)
        if path != "No path found, UAV did not move.":
            riskheap = utils.getData(uavData, riskheap, path)
            uavArray[uavNumber].setLocation(endLbl)

    else:
        print("Incorrect search method please enter either 'entire' or 'between'")
    return locationGraph, uavData, uavArray, riskheap

def deleteConnection(locationGraph):
    fromLabel = str(input("\nPlease enter the first existing location of connection: "))
    while not locationGraph.hasVertex(fromLabel):
        print("Location does not exists!")
        fromLabel = str(input("Please enter the first existing location of connection: "))

    toLabel = str(input("\nPlease enter the second existing location of connection: "))
    while not locationGraph.hasVertex(toLabel):
        print("Location does not exists!")
        toLabel = str(input("Please enter the second existing location of connection: "))

    locationGraph.deleteEdge(toLabel, fromLabel)
    locationGraph.deleteEdge(fromLabel, toLabel)
    return locationGraph

def deleteLocation(locationGraph, uavData, uavArray):
    locationLbl = str(input("\nPlease enter a location to delete: "))
    print(locationLbl)
    while not locationGraph.hasVertex(locationLbl):
        print("Location does not exists!")
        locationLbl = str(input("Please enter a location to delete: "))

    locationGraph.deleteVertex(locationLbl)
    uavData.remove(utils.createKey(locationLbl))

    for i in range(len(uavArray)):
        if uavArray[i].getLocation() == locationLbl:
            print("\nOld Location Deleted")
            newLbl = str(input(f"\nPlease enter the UAV Number {i+1} new location: "))
            while not locationGraph.hasVertex(newLbl):
                print("Location does not exists!")
                newLbl = str(input(f"Please enter the UAV Number {i+1} new location: "))
            uavArray[i].setLocation(newLbl)

    print("\nLocation and Data Deleted!")
    return locationGraph, uavData, uavArray

def insertConnection(locationGraph):
    fromVertex = str(input("\nPlease enter the first existing location of the connection: "))
    while not locationGraph.hasVertex(fromVertex):
        print("Location does not exists!")
        fromVertex = str(input("Please enter the first existing location of the connection: "))

    toVertex = str(input("Please enter the second existing location of the connection: "))
    while not locationGraph.hasVertex(toVertex):
        print("Location does not exists!")
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
    return locationGraph


def insertLocation(locationGraph, uavData):
    newLocLbl = str(input("\nPlease enter a label for the new location: "))
    while locationGraph.hasVertex(newLocLbl):
        print("Location already exists!")
        newLocLbl = str(input("Please enter a label for the new location: "))

    locationGraph.addVertex(newLocLbl, newLocLbl)

    print("\nPlease provide location data below")
    temperature = 0.0
    while temperature < 25.0 or temperature > 48.0:
        try:
            temperature  = float(input("Please enter the temperature (25-48 inclusive): "))
        except ValueError:
            print("Please enter a floating point value!")
            temperature = 0.0

    humidity = -1.0
    while humidity < 15.0 or humidity > 60.0:
        try:
            humidity  = float(input("Please enter the humidity (15-60 inclusive): "))
        except ValueError:
            print("Please enter a floating point value!")
            humidity = -1.0

    windSpeed = -1.0
    while windSpeed < 30.0 or windSpeed > 100:
        try:
            windSpeed  = float(input("Please enter the wind (30-100 inclusive): "))
        except ValueError:
            print("Please enter a floating point value!")
            windSpeed = -1.0

    value = str(temperature) + "," + str(humidity) + "," + str(windSpeed)
    uavData.put(utils.createKey(newLocLbl), value)

    print("\nLocation Added!")

    addAnotherEdge = str(input("\nWould you like to add a connection? (Yes/No): "))
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
    return locationGraph, uavData