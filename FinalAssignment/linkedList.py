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
        self._head = None
        self._tail = None
        self._count = 0


    def isEmpty(self):
        empty = False
        if (self._head == None) and (self._tail == None):
            empty = True
        return empty
    
    
    def isFull(self):
        pass
    

    def insertFirst(self, newValue):
        newNode = DSADoublyListNode(newValue)
        self._count = self._count + 1
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            newNode.setNext(self._head)
            self._head.setPrev(newNode)
            self._head = newNode


    def insertLast(self, newValue):
        newNode = DSADoublyListNode(newValue)
        self._count = self._count + 1
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.setNext(newNode)
            newNode.setPrev(self._tail)
            self._tail = newNode
    
    def peekFirst(self):
        if not self.isEmpty():
            nodeValue = self._head
            return nodeValue


    def peekLast(self):
        if not self.isEmpty():
            nodeValue = self._tail.getValue()
            return nodeValue

    
    def removeFirst(self):
        if not self.isEmpty():
            self._count = self._count - 1
            if self._head.getNext() == None:
                nodeValue = self._head.getValue()
                self._head = None
                self._tail = None
            else:
                nodeValue = self._head.getValue()
                self._head = self._head.getNext()
                self._head.setPrev(None)
            return nodeValue


    def removeLast(self):
        if not self.isEmpty():
            self._count = self._count - 1
            if self._tail.getPrev() == None:
                nodeValue = self._tail.getValue()
                self._tail = None
                self._head = None
            else:
                nodeValue = self._tail.getValue()
                self._tail = self._tail.getPrev()
                self._tail.setNext(None)
            return nodeValue
        
    def remove(self, value):
        curr = self._head
        while curr and (curr.getValue().getValue() != value):
            curr = curr.getNext()
        
        if not curr:
            # do nothing
            ...
        elif curr == self._head:
            self.removeFirst()
        elif curr == self._tail:
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
                print(item)
            print("---Tail---")
    
    def __iter__(self):
        currentNode = self._head
        while currentNode:
            yield currentNode
            currentNode = currentNode.getNext()
