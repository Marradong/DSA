import numpy as np

class DSAHeapEntry():

    def __init__(self, priority, value):
        self.setPriority(priority)
        self.setValue(value)

    
    def setPriority(self, priority):
        self._priority = priority
        return
    

    def setValue(self, value):
        self._value = value
        return


    def getPriority(self):
        return self._priority
    

    def getValue(self):
        return self._value
    

class DSAHeap():

    def __init__(self):
        self._heap = np.empty(10000, dtype=DSAHeapEntry)
        self._count = 0


    def updatePriority(self, priority, value):
        for i in range(self._count):
            if self._heap[i].getValue() == value:
                self._heap[i].setPriority(priority)
                self.trickleUp(i)
        return

    
    def add(self, priority, value):
        if not self.isAdded(value):
            newEntry = DSAHeapEntry(priority, value)
            self._heap[self._count] = newEntry
            self.trickleUp(self._count)
            self._count = self._count + 1
        return

    def add(self, priority, value):
        if self._heap[0] == None:
            newEntry = DSAHeapEntry(priority, value)
            self._heap[self._count] = newEntry
            self.trickleUp(self._count)
            self._count = self._count + 1
        elif self._heap[0].getPriority() < priority:
            for i in range(self._count):
                self.remove()
            newEntry = DSAHeapEntry(priority, value)
            self._heap[self._count] = newEntry
            self.trickleUp(self._count)
            self._count = self._count + 1
        elif self._heap[0].getPriority() == priority:
            newEntry = DSAHeapEntry(priority, value)
            self._heap[self._count] = newEntry
            self.trickleUp(self._count)
            self._count = self._count + 1
        return

    def remove(self):
        root = self._heap[0]
        rootValue = ""
        if root != None:
            self._heap[0] = self._heap[self._count - 1]
            self._heap[self._count - 1] = None
            self.trickleDown(0)
            self._count = self._count - 1
            rootValue = root.getValue()
        return rootValue


    def isAdded(self, value):
        isAdded = False
        for i in range(self._count):
            if self._heap[i].getValue() == value:
                isAdded = True
        return isAdded

    
    def find(self, value):
        found = False
        for i in range(self._count):
            if self._heap[i].getValue == value:
                found = True
        return found
            
    def peekPriority(self):
        root = self._heap[0]
        priority = -1
        if root != None:
            priority = root.getPriority()
        return priority
        

    def display(self):
        print("\n---Top of Heap---")
        for i in range(self._count):
            print(self._heap[i].getValue())
        print("---Bottom of Heap---")
        return


    def trickleUp(self, index):
        parentIdx = (index-1)//2
        if index > 0:
            if (self._heap[index] != None) and (self._heap[parentIdx] != None) and (self._heap[index].getPriority() > self._heap[parentIdx].getPriority()):
                temp = self._heap[parentIdx]
                self._heap[parentIdx] = self._heap[index]
                self._heap[index] = temp
                self.trickleUp(parentIdx)

    
    def trickleDown(self, index):
        lChildIdx = index * 2 + 1
        rChildIdx = lChildIdx + 1
        if lChildIdx < self._count:
            largeIdx = lChildIdx
            if rChildIdx < self._count:
                if (self._heap[lChildIdx] != None) and (self._heap[rChildIdx] != None) and (self._heap[lChildIdx].getPriority() < self._heap[rChildIdx].getPriority()):
                    largeIdx = rChildIdx
            if (self._heap[index] != None) and (self._heap[largeIdx] != None) and (self._heap[largeIdx].getPriority() > self._heap[index].getPriority()):
                temp = self._heap[index]
                self._heap[index] = self._heap[largeIdx]
                self._heap[largeIdx] = temp
                self.trickleDown(largeIdx)


    def _heapify(self):
        for i in range((int((self._count-1)/2)-1), -1, -1):
            self.trickleDown(i)
        return
    

    def heapSort(self):
        self._heapify()
        for i in range(((self._count-1)-1), -1, -1):
            temp = self._heap[0]
            self._heap[0] = self._heap[i]
            self._heap[i] = temp
            self.trickleDown(0)
            self.trickleDown(i)

