import numpy as np
from ClassDefinitions import uav
from ClassDefinitions import graph
from ClassDefinitions import hash


def usage():
    print(" Usage: py runUAV.py x y z")
    print("        where")
    print("        x is the name of the file containing the locations")
    print("        y is the name of the file containing the UAV data")
    print("        Z is the number of the UAVs")

def printCommands():
    print("\nHere is a list of valid commands (command - description): ")
    print("           ds - Display Area")
    print("           il - Insert Location")
    print("           ic - Insert Connection")
    print("           dl - Delete Location")
    print("           dc - Delete Connection")
    print("           sl - Search Location/s")
    print("           it - Provide Itinerary")
    print("           cm - Close Menu")

def createKey(lbl):
    lbl = str(lbl)
    keyVal = 0
    for i in range(len(lbl)):
        keyVal = keyVal + ord(lbl[i])
    return str(keyVal)

def getRisk(temperature, humidity, windSpeed):
    if (humidity < 0):
        print("Incorrect Humidity! Must be 0 or above")
    elif (windSpeed < 0):
        print("Incorrect Wind Speed! Must be 0 or above")
    elif temperature < 25:
        print("Incorrect Temperature! Must be 25 or above")
    else:
        return _getRiskBasic(temperature, humidity, windSpeed)

def _getRiskBasic(temperature, humidity, windSpeed):
    risk = 0
    if (temperature >= 41) or (humidity <= 30) or (windSpeed >= 56):
        risk = 3
    elif (33 <= temperature <= 40) or (31 <= humidity <= 50) or (41 <= windSpeed <= 55):
        risk = 2
    elif (25 <= temperature <= 32) or (humidity >= 51) or (windSpeed <= 40):
        risk = 1
    return risk


def loadLocations(fileName):
    with open(fileName, "r") as locationFile:
        graphDimensions = locationFile.readline().split()
        numEdges = int(graphDimensions[1])
        locationGraph = graph.DSAGraph() 
        for i in range(numEdges):
            newEdge = locationFile.readline().strip("\n").split()
            locationGraph.addVertex(newEdge[0], newEdge[0])
            locationGraph.addVertex(newEdge[1], newEdge[1])
            locationGraph.addEdge(newEdge[0],newEdge[1], newEdge[2])
    return locationGraph

def loadData(fileName, locationGraph):
    with open(fileName, "r") as dataFile:
        uavData = hash.DSADoubleHashTable(10)
        locationData = dataFile.readline()
        while locationData:
            vertex = locationData.split()[0]
            if not locationGraph.hasVertex(vertex):
                locationGraph.addVertex(vertex, vertex)
            temperature = locationData.split()[1]
            humidity = locationData.split()[2]
            windSpeed = locationData.split()[3]
            value = str(float(temperature)) + "," + str(float(humidity)) + "," + str(float(windSpeed))
            uavData.put(createKey(vertex), value)
            locationData = dataFile.readline()
    return uavData, locationGraph


def getData(uavData, riskHeap, path):
    locations = path.split("->")
    print("\nSearch results")
    print("Location : Temperature, Humidity, Wind Speed")
    for i in range(len(locations)):
        data = uavData.get(createKey(locations[i]))
        splitData = data.split(",")
        risk = getRisk(float(splitData[0]), float(splitData[1]), float(splitData[2]))
        value = str(locations[i]) + ":" + str(splitData[0]) + "," + str(splitData[1]) + "," + str(splitData[2])
        riskHeap.add(risk, locations[i])
        print(value, " risk: ", risk)
    return riskHeap

def createUAVs(numUavs, locationGraph):
    if numUavs <= 0:
        raise ValueError()
    
    uavArray = np.empty(numUavs, dtype=uav.UAV)
    for i in range(numUavs):
        newUav = uav.UAV()
        startLbl = str(input(f"\nPlease enter the UAV Number {i+1} starting location: "))
        while not locationGraph.hasVertex(startLbl):
            print("Location does not exists!")
            startLbl = str(input(f"Please enter the UAV Number {i+1} starting location: "))
        newUav.setLocation(startLbl)
        uavArray[i] = newUav
    return uavArray


# region redundant

risk_matrix = np.array([[[0, 1, 2], 
                         [1, 3, 4], 
                         [2, 4, 5]], 
                        
                        [[1, 3, 4], 
                         [3, 6, 7], 
                         [4, 7, 8]], 
                        
                         [[2, 4, 5], 
                          [4, 7, 8], 
                          [5, 8, 9]]])

def _getRiskComplex(temperature, humidity, windSpeed):
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