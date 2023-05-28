import sys
import utils
import menu
from ClassDefinitions import heap

# region Global constants
LocFileIDX = 1
DataFileIDX = 2
UavNumberIDX = 3

# endregion

# region Main Method

def __main__():
    if len(sys.argv) != 4:
        utils.usage()
    else:
        
        lfileName = sys.argv[LocFileIDX]
        dfileName = sys.argv[DataFileIDX]
        numUavs = sys.argv[UavNumberIDX]
        try:
            numUavs = int(numUavs)
            # region TASK1 - Location From File
            locationGraph = utils.loadLocations(lfileName)
            # endregion
            # region TASK4 - Data From File
            uavData, locationGraph = utils.loadData(dfileName, locationGraph)
            # endregion
            uavArray = utils.createUAVs(numUavs, locationGraph)
            riskheap = heap.DSAHeap()
            # region Menu
            utils.printCommands()
            userCommand = ""
            while (userCommand != "cm"):
                userCommand = str(input("\nPlease enter a valid command: "))

                # region TASK1 - display adjacency list
                if userCommand == "ds":
                    locationGraph.displayAsList()
                # endregion
                # region TASK3 - insert location operation
                elif userCommand == "il":
                    locationGraph, uavData = menu.insertLocation(locationGraph, uavData)
                # endregion
                # region TASK3 - insert connection operation
                elif userCommand == "ic":
                    locationGraph = menu.insertConnection(locationGraph)
                # endregion
                # region TASK3 - delete location
                elif userCommand == "dl":
                    locationGraph, uavData, uavArray = menu.deleteLocation(locationGraph, uavData, uavArray)
                # endregion
                # region TASK3 - delete connection
                elif userCommand == "dc":
                    locationGraph = menu.deleteConnection(locationGraph)
                # endregion
                # region TASK3 - search operation
                elif userCommand == "sl":
                    locationGraph, uavData, uavArray, riskheap = menu.searchLocation(locationGraph, uavData, uavArray, riskheap)
                # endregion
                # region TASK6 - UAV itinerary
                elif userCommand == "it":
                    locationGraph, uavArray, riskheap = menu.getItinerary(locationGraph, uavArray, riskheap)
                # endregion
                elif userCommand == "cm":
                    print("\nClosing Menu\n")
                else:
                    print("Invalid command please see list below")
                    utils.printCommands()
            # endregion
        except IOError as e:
            print("\nError loading file: ", e)
        # except ValueError as e:
        #     print("\nNumber of UAVs Must be an integer above 0!\n")
        
if __name__ == "__main__":
    __main__()
# endregion
