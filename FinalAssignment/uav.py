
class UAV():

    def __init__(self):
        self._location = None
        return

    def setLocation(self, loc):
        self._location = loc
        return
    
    def getLocation(self):
        return self._location
