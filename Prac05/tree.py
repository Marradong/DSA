import linkedList as LL
import numpy as np

class DSATreeNode():


    def __init__(self, inKey, inValue):
        self._key = inKey
        self._value = inValue
        self._leftChild = None
        self._rightChild = None


    def getKey(self):
        return self._key
    

    def getValue(self):
        return self._value
    
    def __str__(self):
        return ("Key: " + str(self.getKey()) + " Value: " + str(self.getValue()))
    
    
    def getLeft(self):
        return self._leftChild
    

    def setLeft(self, newLeft):
        self._leftChild = newLeft
        return
    

    def getRight(self):
        return self._rightChild
    

    def setRight(self, newRight):
        self._rightChild = newRight
        return
    

class DSABinarySearchTree():


    def __init__(self):
        self._root = None


    def find(self, key):
        return self._findRecursive(key, self._root)


    def _findRecursive(self, key, curr: DSATreeNode):
        value = None
        if curr == None:
            raise ValueError("Key " + key + " was not found")
        elif key == curr.getKey():
            value = curr.getValue()
        elif key < curr.getKey():
            value = self._findRecursive(key, curr.getLeft())
        else:
            value = self._findRecursive(key, curr.getRight())
        return value


    def insert(self, key, value):
        self._root = self._insertRecursive(key, value, self._root)
        return

    
    def _insertRecursive(self, key, value, curr: DSATreeNode): 
        updateNode = curr
        if curr == None:
            newNode = DSATreeNode(key, value)
            updateNode = newNode
        elif key == curr.getKey():
            raise ValueError("Key " + str(key) + " already exists")
        elif key < curr.getKey():
            curr.setLeft(self._insertRecursive(key, value, curr.getLeft()))
        else:
            curr.setRight(self._insertRecursive(key, value, curr.getRight()))
        return updateNode
    
    def delete(self, key):
        self._root = self._deleteRecursive(key, self._root)
        return
    

    def _deleteRecursive(self, key, curr: DSATreeNode):
        updateNode = curr
        if curr == None:
            raise ValueError("Key " + str(key) + " was not found")
        elif key == curr.getKey():
            updateNode = self._deleteNode(key, curr)
        elif key < curr.getKey():
            curr.setLeft(self._deleteRecursive(key, curr.getLeft()))
        else:
            curr.setRight(self._deleteRecursive(key, curr.getRight()))
        return updateNode

    
    def _deleteNode(self, key, delNode: DSATreeNode):
        updateNode = None
        if (delNode.getLeft() == None) and (delNode.getRight() == None):
            updateNode = None
        elif (delNode.getLeft() != None) and (delNode.getRight() == None):
            updateNode = delNode.getLeft()
        elif (delNode.getLeft() == None) and (delNode.getRight() != None):
            updateNode = delNode.getRight()
        else:
            updateNode = self._promoteSuccessor(delNode.getRight())
            if updateNode != delNode.getRight():
                updateNode.setRight(delNode.getRight())
            updateNode.setLeft(delNode.getLeft())
        return updateNode
    
    def _promoteSuccessor(self, curr: DSATreeNode):
        successor = curr
        if curr.getLeft() != None:
            successor = self._promoteSuccessor(curr.getLeft())
            if successor == curr.getLeft():
                curr.setLeft(successor.getRight())
        return successor
        
        
    def display(self):
        self._displyRecursive(0, self._root)
        return

    def _displyRecursive(self, level, curr: DSATreeNode):
        if curr != None:
            level = level + 1
            self._displyRecursive(level, curr.getRight())
            print('    '*level + "———"+ str(curr.getValue()))
            self._displyRecursive(level, curr.getLeft())


    def height(self):
        return self._heightRec(self._root)

    def _heightRec(self, curNode):
        
        if curNode == None:
            htSoFar = -1
        else:
            leftHt = self._heightRec(curNode.getLeft())
            rightHt = self._heightRec(curNode.getRight())
        
            if leftHt > rightHt:
                htSoFar = leftHt + 1
            else:
                htSoFar = rightHt + 1
    
        return htSoFar
    
    def min(self):
        curNode = self._root
        while (curNode.getLeft() != None):
            curNode = curNode.getLeft()
        minKey = curNode.getKey()
        return minKey

    
    def max(self):
        curNode = self._root
        while (curNode.getRight() != None):
            curNode = curNode.getRight()
        maxKey = curNode.getKey()
        return maxKey
    

    def balance(self):
        balance = 0.0
        leftHeight = self._heightRec(self._root.getLeft()) + 1
        rightHeight = self._heightRec(self._root.getRight()) + 1

        if leftHeight > rightHeight:
            balance = (float(rightHeight) / float(leftHeight)) * 100
        else:
            balance = (float(leftHeight) / float(rightHeight)) * 100
        
        return balance


    def inorder(self):
        llist = LL.DSADoublyLinkedList()
        llist = self._inorderRecursive(self._root, llist)
        inorderStr = ""
        for item in llist:
            inorderStr = inorderStr + " " + str(item)
        return inorderStr

    
    def _inorderRecursive(self, curr: DSATreeNode, llist: LL.DSADoublyLinkedList):
        if curr != None:
            llist = self._inorderRecursive(curr.getLeft(), llist)
            valueToInsert = str(curr.getValue()) + ":" + str(curr.getKey())
            llist.insertLast(valueToInsert)
            llist = self._inorderRecursive(curr.getRight(), llist)
        return llist
    

    def preorder(self):
        llist = LL.DSADoublyLinkedList()
        llist = self._preorderRecursive(self._root, llist)
        preorderStr = ""
        for item in llist:
            preorderStr = preorderStr + " " + str(item)
        return preorderStr

    def _preorderRecursive(self, curr: DSATreeNode, llist: LL.DSADoublyLinkedList):
        if curr != None:
            valueToInsert = str(curr.getValue()) + ":" + str(curr.getKey())
            llist.insertLast(valueToInsert)
            llist = self._preorderRecursive(curr.getLeft(), llist)
            llist = self._preorderRecursive(curr.getRight(), llist)
        return llist

    
    def postorder(self):
        llist = LL.DSADoublyLinkedList()
        llist = self._postorderRecursive(self._root, llist)
        postorderStr = ""
        for item in llist:
            postorderStr = postorderStr + " " + str(item)
        return postorderStr

    def _postorderRecursive(self, curr: DSATreeNode, llist: LL.DSADoublyLinkedList):
        if curr != None:
            llist = self._postorderRecursive(curr.getLeft(), llist)
            llist = self._postorderRecursive(curr.getRight(), llist)
            valueToInsert = str(curr.getValue()) + ":" + str(curr.getKey())
            llist.insertLast(valueToInsert)
        return llist