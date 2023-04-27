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
        self._heap = np.empty(100, dtype=DSAHeapEntry)
        self._count = 0

    
    def add(self, priority, value):
        newEntry = DSAHeapEntry(priority, value)
        self._heap[self._count] = newEntry
        self.trickleUp(self._count)
        self._count = self._count + 1
        return


    def remove(self):
        root = self._heap[0]
        self._heap[0] = self._heap[self._count - 1]
        self._heap[self._count - 1] = None
        self.trickleDown(0)
        return
    

    def display(self):
        ...


    def trickleUp(self, index):
        parentIdx = (index-1)/2
        if index > 0:
            if self._heap[index] > self._heap[parentIdx]:
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
                if self._heap[lChildIdx] < self._heap[rChildIdx]:
                    largeIdx = rChildIdx
            if  self._heap[largeIdx] > self._heap[index]:
                temp = self._heap[index]
                self._heap[index] = self._heap[largeIdx]
                self._heap[largeIdx] = temp
                self.trickleDown(largeIdx)
