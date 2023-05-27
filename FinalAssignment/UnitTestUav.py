import uav

def __main__():
    print("\ntest uav initialisation")
    newUav = uav.UAV()
    print(newUav)

    print("\ntest set location")
    location = str(input("Please enter a location for the UAV"))

    print("\ntest get location")
    print("The uav location is: ", newUav.getLocation())

if __name__ == "__main__":
    __main__()