import numpy as np

class DSAStack():

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.stack = np.zeros(capacity, dtype=object)
        self.count = 0
    

    def getCount(self):
        return self.count
    

    def isEmpty(self):
        if self.count == 0:
            empty = True
        else:
            empty = False
        return empty


    def isFull(self):
        if self.count == self.capacity:
            full = True
        else:
            full = False
        return full
    

    def push(self, value):
        if not self.isFull():
            self.stack[self.count] = value
            self.count = self.count + 1
    

    def top(self):
        if not self.isEmpty():
            topVal = self.stack[self.count - 1]
            return topVal
        

    def pop(self):
        topVal = self.top()
        self.stack[self.count - 1] = 0
        self.count = self.count - 1
        return topVal


class DSAQueue():

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.queue = np.zeros(self.capacity, dtype=object)
        self.count = 0


    def getCount(self):
        return self.count
    

    def isEmpty(self):
        if self.count == 0:
            empty = True
        else:
            empty = False
        return empty


    def isFull(self):
        if self.count == self.capacity:
            full = True
        else:
            full = False
        return full

    def enqueue(self, value):
        if not self.isFull():
            self.queue[self.count] = value
            self.count = self.count + 1

    
    def dequeue(self):
        if not self.isEmpty():
            frontVal = self.queue[0]
            for i in range(self.count - 1):
                self.queue[i] = self.queue[i+1]
                self.queue[i+1] = 0
            if (self.count - 1) == 0:
                self.queue[0] = self.queue[1]
            self.count = self.count - 1
            return frontVal
    

    def peek(self):
            return self.queue[0]
    
class DSACircularQueue(DSAQueue):

    def __init__(self, capacity=100):
        super().__init__(capacity)
        self.frontIdx = 0

    def dequeue(self):
        if not self.isEmpty():
            frontVal = self.queue[self.frontIdx]
            self.queue[self.frontIdx] = 0
            if (self.frontIdx + 1) > self.capacity:
                self.frontIdx = 0
            else:
                self.frontIdx = self.frontIdx + 1
            self.count = self.count - 1
            
            return frontVal
        
    
    def enqueue(self, value):
        if (self.frontIdx + self.count) > self.capacity:
            if not self.isFull():
                #TODO
                self.queue[self.count] = value
                self.count = self.count + 1
        else:
            return super().enqueue(value)