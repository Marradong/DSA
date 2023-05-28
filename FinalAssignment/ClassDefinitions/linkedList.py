class DSADoublyListNode:
    

    def __init__(self, inValue):
        self._value = self.setValue(inValue)
        self._next = self.setNext(None)
        self._prev = self.setPrev(None)


    def getValue(self):
        return self._value
    

    def setValue(self, inValue):
        self._value = inValue
        return self._value


    def getNext(self):
        return self._next
    

    def setNext(self, nextNode):
        self._next = nextNode
        return self._next


    def getPrev(self):
        return self._prev
    

    def setPrev(self, prevNode):
        self._prev = prevNode
        return self._prev

class DSADoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0


    def isEmpty(self):
        empty = False
        if (self.head == None) and (self.tail == None):
            empty = True
        return empty
    

    def insertFirst(self, newValue):
        newNode = DSADoublyListNode(newValue)
        self._count = self._count + 1
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode


    def insertLast(self, newValue):
        newNode = DSADoublyListNode(newValue)
        self._count = self._count + 1
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
    
    def peekFirst(self):
        if not self.isEmpty():
            nodeValue = self.head
            return nodeValue


    def peekLast(self):
        if not self.isEmpty():
            nodeValue = self.tail.getValue()
            return nodeValue

    
    def removeFirst(self):
        if not self.isEmpty():
            self._count = self._count - 1
            if self.head.getNext() == None:
                nodeValue = self.head.getValue()
                self.head = None
                self.tail = None
            else:
                nodeValue = self.head.getValue()
                self.head = self.head.getNext()
                self.head.setPrev(None)
            return nodeValue


    def removeLast(self):
        if not self.isEmpty():
            self._count = self._count - 1
            if self.tail.getPrev() == None:
                nodeValue = self.tail.getValue()
                self.tail = None
                self.head = None
            else:
                nodeValue = self.tail.getValue()
                self.tail = self.tail.getPrev()
                self.tail.setNext(None)
            return nodeValue
        
    def remove(self, value):
        curr = self.head
        try:
            currVal = curr.getValue().getValue()
        except AttributeError:
            print(curr.getValue())
            currVal = None
        while curr and (currVal != value):
            curr = curr.getNext()
            try:
                currVal = curr.getValue().getValue()
            except AttributeError:
                currVal = None
        
        if not curr:
            ...
        elif curr == self.head:
            self.removeFirst()
        elif curr == self.tail:
            self.removeLast()
        else:
            self._count = self._count - 1
            prev = curr.getPrev()
            next = curr.getNext()
            prev.setNext(next)
            next.setPrev(prev)
        return
        
        
    def printList(self):
        if not self.isEmpty():
            print("---Head---")
            for item in self:
                print(item.getValue())
            print("---Tail---")
    
    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode
            currentNode = currentNode.getNext()
