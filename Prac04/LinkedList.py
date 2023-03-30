class DSADoublyListNode:
    
    def __init__(self, inValue):
        self._value = self.setValue(inValue)
        self._next = self.setNext(None)

class DSADoublyLinkedList:
    def __init__(self):
        self.head = None


class DSAListNode():

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
    

class DSALinkedList():

    def __init__(self):
        self.head = None

    
    def isEmpty(self):
        empty = False
        if self.head == None:
            empty = True
        return empty
    

    def insertFirst(self, newValue):
        newNode = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode


    def insertLast(self, newValue):
        newNode = DSAListNode(newValue)
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
