import numpy as np


class DSAHashEntry():

    
    def __init__(self, inKey="", inValue=None):
        self._key = inKey
        self._value = inValue
        if inKey == "" and inValue == None:
            self._state = 0
        else:
            self._state = 1


class DSADoubleHashTable():
    def __init__(self, tableSize):
            self._lfUpper = 0.6
            self._lfLower = 0.2
            self._count = 0
            actualSize = self.findNextPrime(tableSize)
            self._maxStep = 5
            self._hashArray = np.empty(actualSize, dtype=object)
            for i in range(actualSize):
                self._hashArray[i] = DSAHashEntry()


    def put(self, inKey, inValue):
        if self.getLoadFactor() > self._lfUpper:
            self.resize()

        hashIdx = self.hash(inKey)

        while self._hashArray[hashIdx]._key != "":
            hashIdx = hashIdx + self.stepHash(int(inKey))
            if hashIdx >= (len(self._hashArray) - 1):
                hashIdx = 0

        self._hashArray[hashIdx]._key = inKey
        self._hashArray[hashIdx]._value = inValue
        self._hashArray[hashIdx]._state = 1
        if(inValue != None):
            self._count = self._count + 1
        return


    def get(self, inKey):
        hashIdx = self.hash(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False

        while (not found) and (not giveUp):
            if (self._hashArray[hashIdx]._state == 0):
                giveUp = True
            elif (self._hashArray[hashIdx]._key == inKey):
                found = True
            else:
                hashIdx = (hashIdx + 1) % len(self._hashArray)
                if (hashIdx == origIdx):
                    giveUp = True
        if not found:
            raise ValueError("Key not found")
        else:
            return self._hashArray[hashIdx]._value
        
    
    def remove(self, inKey):
        hashIdx = self.hash(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False

        while (not found) and (not giveUp):
            if (self._hashArray[hashIdx]._state == 0):
                giveUp = True
            elif (self._hashArray[hashIdx]._key == inKey):
                found = True
            else:
                hashIdx = (hashIdx + 1) % len(self._hashArray)
                if (hashIdx == origIdx):
                    giveUp = True

        if not found:
            raise Exception("Key not found")
        else:
            self._hashArray[hashIdx]._key = ""
            self._hashArray[hashIdx]._value = None
            self._count = self._count - 1
            if self.getLoadFactor() < self._lfLower:
                self.resize()
            return
    

    def getLoadFactor(self):
        return self._count / len(self._hashArray)

    
    def export(self):
        print("\n---Values in Hash Table with State = 1---")
        for i in range(len(self._hashArray)):
            if (self._hashArray[i]._state == 1):
                print("key: ", self._hashArray[i]._key, "value: ", self._hashArray[i]._value)
        print("---End of Table---\n")
        return

    
    def resize(self):
        if self.getLoadFactor() < self._lfLower:
            # print("\nLoad factor <", self._lfLower, ": ", self.getLoadFactor(), " Resizing\n")
            actualSize = self.findNextPrime(len(self._hashArray)//2)
        else:
            # print("\nLoad factor >", self._lfUpper, ": ", self.getLoadFactor(), " Resizing\n")
            actualSize = self.findNextPrime(len(self._hashArray)*2)

        oldArray = self._hashArray
        self._hashArray = np.empty(actualSize, dtype=object)
        for i in range(len(self._hashArray)):
            self._hashArray[i] = DSAHashEntry()
        self._count = 0
        for j in range(len(oldArray)):
            if (oldArray[j]._state == 1):
                self.put(oldArray[j]._key, oldArray[j]._value)
        return 
    

    def hash(self, inKey):
        hashIdx = 0
        for i in range(len(inKey)):
            hashIdx = (33 * hashIdx) + ord(inKey[i])
        return hashIdx % len(self._hashArray)


    def stepHash(self, index):      
        return self._maxStep - (index % self._maxStep)


    def saveCSV(self):
        try:
            fileObj = open("hashTable.csv", "w")
            for i in range(len(self._hashArray)):
                if (self._hashArray[i]._value != None):
                    fileObj.write(str(self._hashArray[i]._key) + ", " + str(self._hashArray[i]._value))
            fileObj.close()
        except IOError as e:
            print("File Processing Error: " + str(e))
        return


    def findNextPrime(self, startValue):
        if (startValue % 2 == 0):
            nextPrime = startValue + 1
        else:
            nextPrime = startValue
        nextPrime = nextPrime - 2
        isPrime = False
        while (not isPrime):
            nextPrime = nextPrime + 2
            i = 3
            isPrime = True
            while (i*i <= nextPrime) and (isPrime):
                if (nextPrime % i) == 0:
                    isPrime = False
                else:
                    i = i + 2
        return nextPrime


    def __init__(self, tableSize):
        self._lfUpper = 0.6
        self._lfLower = 0.2
        self._count = 0
        actualSize = self.findNextPrime(tableSize)
        self._hashArray = np.empty(actualSize, dtype=object)
        for i in range(actualSize):
            self._hashArray[i] = DSAHashEntry()


    def put(self, inKey, inValue):
        if self.getLoadFactor() > self._lfUpper:
            self.resize()

        hashIdx = self.hash(inKey)

        while self._hashArray[hashIdx]._key != "":
            hashIdx = self.stepHash(hashIdx)

        self._hashArray[hashIdx]._key = inKey
        self._hashArray[hashIdx]._value = inValue
        self._hashArray[hashIdx]._state = 1
        if(inValue != None):
            self._count = self._count + 1
        return


    def get(self, inKey):
        hashIdx = self.hash(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False

        while (not found) and (not giveUp):
            if (self._hashArray[hashIdx]._state == 0):
                giveUp = True
            elif (self._hashArray[hashIdx]._key == inKey):
                found = True
            else:
                hashIdx = (hashIdx + 1) % len(self._hashArray)
                if (hashIdx == origIdx):
                    giveUp = True
        if not found:
            raise Exception("Key not found")
        else:
            return self._hashArray[hashIdx]._value
        
    
    def remove(self, inKey):
        hashIdx = self.hash(inKey)
        origIdx = hashIdx
        found = False
        giveUp = False

        while (not found) and (not giveUp):
            if (self._hashArray[hashIdx]._state == 0):
                giveUp = True
            elif (self._hashArray[hashIdx]._key == inKey):
                found = True
            else:
                hashIdx = (hashIdx + 1) % len(self._hashArray)
                if (hashIdx == origIdx):
                    giveUp = True

        if not found:
            raise Exception("Key not found")
        else:
            self._hashArray[hashIdx]._key = ""
            self._hashArray[hashIdx]._value = None
            self._count = self._count - 1
            if self.getLoadFactor() < self._lfLower:
                self.resize()
            return
    

    def getLoadFactor(self):
        return self._count / len(self._hashArray)

    
    def export(self):
        print("\n---Values in Hash Table with State = 1---")
        for i in range(len(self._hashArray)):
            if (self._hashArray[i]._state == 1):
                print("key: ", self._hashArray[i]._key, "value: ", self._hashArray[i]._value)
        print("---End of Table---\n")
        return

    
    def resize(self):
        if self.getLoadFactor() < self._lfLower:
            print("\nLoad factor <", self._lfLower, ": ", self.getLoadFactor(), " Resizing\n")
            actualSize = self.findNextPrime(len(self._hashArray)//2)
        else:
            print("\nLoad factor >", self._lfUpper, ": ", self.getLoadFactor(), " Resizing\n")
            actualSize = self.findNextPrime(len(self._hashArray)*2)

        oldArray = self._hashArray
        self._hashArray = np.empty(actualSize, dtype=object)
        for i in range(len(self._hashArray)):
            self._hashArray[i] = DSAHashEntry()
        self._count = 0
        for j in range(len(oldArray)):
            if (oldArray[j]._state == 1):
                self.put(oldArray[j]._key, oldArray[j]._value)
        return 
    

    def hash(self, inKey):
        hashIdx = 0
        for i in range(len(inKey)):
            hashIdx = (33 * hashIdx) + ord(inKey[i])
        return hashIdx % len(self._hashArray)


    def stepHash(self, index):
        newIdx = index + 1
        if newIdx >= (len(self._hashArray) - 1):
            newIdx = 0
        return newIdx


    def saveCSV(self):
        try:
            fileObj = open("hashTable.csv", "w")
            for i in range(len(self._hashArray)):
                if (self._hashArray[i]._value != None):
                    fileObj.write(str(self._hashArray[i]._key) + ", " + str(self._hashArray[i]._value))
            fileObj.close()
        except IOError as e:
            print("File Processing Error: " + str(e))
        return


    def findNextPrime(self, startValue):
        if (startValue % 2 == 0):
            nextPrime = startValue + 1
        else:
            nextPrime = startValue
        nextPrime = nextPrime - 2
        isPrime = False
        while (not isPrime):
            nextPrime = nextPrime + 2
            i = 3
            isPrime = True
            while (i*i <= nextPrime) and (isPrime):
                if (nextPrime % i) == 0:
                    isPrime = False
                else:
                    i = i + 2
        return nextPrime
    