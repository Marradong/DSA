import numpy as np

class DSAStack():

    def __init__(self, capacity=100):
        self._capacity = capacity
        self._stack = np.zeros(capacity, dtype=object)
        self._count = 0
    

    def getCount(self):
        return self._count
    

    def isEmpty(self):
        if self._count == 0:
            empty = True
        else:
            empty = False
        return empty


    def isFull(self):
        if self._count == self._capacity:
            full = True
        else:
            full = False
        return full
    

    def push(self, value):
        if not self.isFull():
            self._stack[self._count] = value
            self._count = self._count + 1
    

    def top(self):
        if not self.isEmpty():
            topVal = self._stack[self._count - 1]
            return topVal
        

    def pop(self):
        topVal = self.top()
        self._stack[self._count - 1] = 0
        self._count = self._count - 1
        return topVal
    

    def printStack(self):
        print("Current Stack: ", self._stack)


class DSAQueue():

    def __init__(self, capacity=100):
        self._capacity = capacity
        self._queue = np.zeros(self._capacity, dtype=object)
        self._count = 0


    def getCount(self):
        return self._count
    

    def isEmpty(self):
        if self._count == 0:
            empty = True
        else:
            empty = False
        return empty


    def isFull(self):
        if self._count == self._capacity:
            full = True
        else:
            full = False
        return full

    def enqueue(self, value):
        if not self.isFull():
            self._queue[self._count] = value
            self._count = self._count + 1

    
    def dequeue(self):
        if not self.isEmpty():
            frontVal = self._queue[0]
            for i in range(self._count - 1):
                self._queue[i] = self._queue[i+1]
                self._queue[i+1] = 0
            if (self._count - 1) == 0:
                self._queue[0] = self._queue[1]
            self._count = self._count - 1
            return frontVal
    

    def peek(self):
            return self._queue[0]
    

    def printQueue(self):
        print("Current Queue: ", self._queue)


class DSAShufflingQueue(DSAQueue):
    def __init__(self, capacity=100):
        super().__init__(capacity)


class DSACircularQueue(DSAQueue):

    def __init__(self, capacity=100):
        super().__init__(capacity)
        self._frontIdx = 0

    def dequeue(self):
        if not self.isEmpty():
            frontVal = self._queue[self._frontIdx]
            self._queue[self._frontIdx] = 0
            if (self._frontIdx + 1) > (self._capacity - 1):
                self._frontIdx = 0
            else:
                self._frontIdx = self._frontIdx + 1
            self._count = self._count - 1
            
            return frontVal
        
    
    def enqueue(self, value):
        if not self.isFull():
            if (self._frontIdx + self._count) >= (self._capacity - 1):
                    self._queue[self._count + self._frontIdx - self._capacity] = value
                    self._count = self._count + 1
            else:
                self._queue[self._count] = value
                self._count = self._count + 1