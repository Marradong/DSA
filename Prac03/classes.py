import numpy as np

class DSAStack():

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.stack = np.zeros(capacity)
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
            self.stack[self.count] == value
            self.count = self.count + 1
    

    def top(self):
        if not self.isEmpty():
            topVal = self.stack[self.count]
            return topVal
        

    def pop(self):
        topVal = self.top()
        self.count = self.count - 1
        return topVal


class DSAQueue():

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.queue = np.zeros(self.capacity)
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
