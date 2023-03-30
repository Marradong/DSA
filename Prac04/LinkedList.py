class DSADoublyListNode:
    

    def __init__(self, inValue):
        self._value = self.setValue(inValue)
        self._next = self.setNext(None)
        self._prev = self.setPrev(None)


    def getValue(self):
        return self._value
    

    def setValue(self, inValue):
        self._value = inValue


    def getNext(self):
        return self._next
    

    def setNext(self, nextNode):
        self._next = nextNode


    def getPrev(self):
        return self._prev
    

    def setPrev(self, prevNode):
        self._prev = prevNode

class DSADoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def isEmpty(self):
        empty = False
        if (self.head == None) and (self.tail == None):
            empty = True
        return empty
    
    
    def isFull(self):
        pass
    

    def insertFirst(self, newValue):
        newNode = DSADoublyListNode(newValue)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode


    def insertLast(self, newValue):
        newNode = DSADoublyListNode(newValue)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
    
    def peekFirst(self):
        if not self.isEmpty():
            nodeValue = self.head.getValue()
            return nodeValue


    def peekLast(self):
        if not self.isEmpty():
            nodeValue = self.tail.getValue()
            return nodeValue

    
    def removeFirst(self):
        if not self.isEmpty():
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
            self.head.setPrev(None)
            return nodeValue


    def removeLast(self):
        if not self.isEmpty():
            nodeValue = self.tail.getValue()
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
            return nodeValue



class DSASinglyListNode():

    def __init__(self, inValue):
        self._value = self.setValue(inValue)
        self._next = self.setNext(None)

    def getValue(self):
        return self._value
    

    def setValue(self, inValue):
        self._value = inValue


    def getNext(self):
        return self._next
    

    def setNext(self, nextNode):
        self._next = nextNode
    

class DSASinglyLinkedList():

    def __init__(self):
        self.head = None

    
    def isEmpty(self):
        empty = False
        if self.head == None:
            empty = True
        return empty
    
    def isFull(self):
        pass
    

    def insertFirst(self, newValue):
        newNode = DSASinglyListNode(newValue)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode


    def insertLast(self, newValue):
        newNode = DSASinglyListNode(newValue)
        if self.isEmpty():
            self.head = newNode
        else:
            currNode = self.head
            while currNode.getNext() != None:
                currNode = currNode.getNext()
            currNode.setNext(newNode)
    
    def peekFirst(self):
        if not self.isEmpty():
            nodeValue = self.head.getValue()
            return nodeValue


    def peekLast(self):
        if not self.isEmpty():
            currNode = self.head
            while currNode.getNext() != None:
                currNode = currNode.getNext()
            nodeValue = currNode.getValue()
            return nodeValue

    
    def removeFirst(self,):
        if not self.isEmpty():
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
            return nodeValue

    def removeLast(self):
        if not self.isEmpty():
            if self.head.getNext() == None:
                nodeValue = self.head.getValue()
                self.head = None
            else:
                prevNode = None
                currNode = self.head
                while currNode.getNext() != None:
                    prevNode = currNode
                    currNode = currNode.getNext()
                prevNode.setNext(None)
                nodeValue = currNode.getValue()
            return nodeValue
