import utils
from ClassDefinitions import graph

def getItinerary(locationGraph, uavArray, riskheap):
    if riskheap._count == 0:
        print("\nNo locations explored! Please use the search function to add location data")
    elif riskheap._count == 1:
        for i in range(len(uavArray)):
            path = str(uavArray[i].getLocation()) + "->" + str(riskheap._heap[0].getValue())
            print(f"Uav {i+1} Itinerary:", path)
    else:
        riskGraph = graph.DSAGraph()
        for i in range(riskheap._count):
            for j in range(i, riskheap._count):
                fromRiskLabel = riskheap._heap[i].getValue()
                toRiskLabel = riskheap._heap[j].getValue()
                riskGraph.addVertex(fromRiskLabel, fromRiskLabel)
                riskGraph.addVertex(toRiskLabel, toRiskLabel)
                path, distance = locationGraph.doDijSearch(fromRiskLabel, toRiskLabel)
                riskGraph.addEdge(fromRiskLabel, toRiskLabel, distance)

        for i in range(len(uavArray)):
            uavLabel = uavArray[i].getLocation()
            riskGraph.addVertex(uavLabel, uavLabel)
            for item in riskGraph.vertices:
                vertex = item.getValue()
                if vertex.getLabel() != uavLabel:
                    path, distance = locationGraph.doDijSearch(uavLabel, vertex.getLabel())
                    riskGraph.addEdge(uavLabel, vertex.getLabel(), distance)
            print(f"Uav {i+1} Itinerary:", riskGraph.nearestNeighbour(uavLabel))
            if not riskheap.isAdded(uavLabel):
                riskGraph.deleteVertex(uavLabel)
    return locationGraph, uavArray, riskheap

def searchLocation(locationGraph, uavData, uavArray, riskheap):
    dfsOrbfs = str(input("\nWould you like to search the entire map or between 2 locations? (entire/between): "))
    # 2 DFS explore entire graph
    if dfsOrbfs == "entire":
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
        
        entirePath = locationGraph.depthFirstSearch(startLbl)
        print("Searching graph using DFS starting from: ", startLbl, " Path: ", entirePath)
        

        for item in locationGraph.vertices:
            if not item.getValue().getVisited():
                print("\nLocation: ", item.getValue().getLabel(), " was not visited! Please add connections to collect its data")

        riskheap = utils.getData(uavData, riskheap, entirePath)

        splitPath = entirePath.split("->")
        uavArray[uavNumber].setLocation(splitPath[-1])

    # 2 BFS explore shortest path
    elif dfsOrbfs == "between":
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