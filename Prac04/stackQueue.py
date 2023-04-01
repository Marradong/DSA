import numpy as np
import linkedList as LL

class DSAStack():

    def __init__(self):
        self._list = LL.DSADoublyLinkedList()
    

    def isEmpty(self):
        return self._list.isEmpty()
    

    def push(self, value):
        self._list.insertFirst(value)
    

    def top(self):
        return self._list.peekFirst()
        

    def pop(self):
        return self._list.removeFirst()
    

    def printStack(self):
        self._list.printList()

    def __iter__(self):
        return iter(self._list)


class DSAQueue():

    def __init__(self):
        self._list = LL.DSADoublyLinkedList()

    
    def isEmpty(self):
        return self._list.isEmpty()
    

    def enqueue(self, value):
        self._list.insertLast(value)

    
    def dequeue(self):
            return self._list.removeFirst()
    

    def peek(self):
            return self._list.peekFirst()
    

    def printQueue(self):
         self._list.printList()


    def __iter__(self):
        return iter(self._list)