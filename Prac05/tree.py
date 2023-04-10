import linkedList as LL

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
        self._insertRecursive(key, value, self._root)
        return

    
    def _insertRecursive(self, key, value, curr: DSATreeNode): 
        if key < curr.getKey():
            next = curr.getLeft()
            if next == None:
                newNode = DSATreeNode(key, value)
                curr.setLeft(newNode)
            else:
                self._insertRecursive(key, value, next)
        elif key > curr.getKey():
            next = curr.getRight()
            if next == None:
                newNode = DSATreeNode(key, value)
                curr.setRight(newNode)
            else:
                self._insertRecursive(key, value, next)
        else:
            raise ValueError("Key " + key + " already exists")
        
    
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
        ...


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
        balance = 0
        leftHeight = self._heightRec(self._root.getLeft())
        rightHeight = self._heightRec(self._root.getRight())

        if (leftHeight == -1) or (rightHeight == -1):
            balance = 0
        elif leftHeight > rightHeight:
            balance = (rightHeight / leftHeight) * 100
        else:
            balance = (leftHeight / rightHeight) * 100
        
        return balance


    def inorder(self):
        llist = LL.DSADoublyLinkedList()
        llist = self._inorderRecursive(self._root, llist)
        print("In Order Traversal: ", end=" ")
        for item in llist:
            print(item, end=" ")
        print("\n")

    
    def _inorderRecursive(self, curr: DSATreeNode, llist: LL.DSADoublyLinkedList):
        if curr != None:
            llist = self._inorderRecursive(curr.getLeft(), llist)
            llist.insertLast(curr.getValue())
            llist = self._inorderRecursive(curr.getRight(), llist)
            return llist
    

    def preorder(self):
        llist = LL.DSADoublyLinkedList()
        llist = self._preorderRecursive(self._root, llist)
        print("Pre Order Traversal: ", end=" ")
        for item in llist:
            print(item, end=" ")
        print("\n")

    def _preorderRecursive(self, curr: DSATreeNode, llist: LL.DSADoublyLinkedList):
        if curr != None:
            llist.insertLast(curr.getValue())
            llist = self._preorderRecursive(curr.getLeft(), llist)
            llist = self._preorderRecursive(curr.getRight(), llist)
            return llist

    
    def postorder(self):
        llist = LL.DSADoublyLinkedList()
        llist = self._postorderRecursive(self._root, llist)
        print("Post Order Traversal: ", end=" ")
        for item in llist:
            print(item, end=" ")
        print("\n")

    def _postorderRecursive(self, curr: DSATreeNode, llist: LL.DSADoublyLinkedList):
        if curr != None:
            llist = self._postorderRecursive(curr.getLeft(), llist)
            llist = self._postorderRecursive(curr.getRight(), llist)
            llist.insertLast(curr.getValue())
            return llist

    ## alternative delete function

    # def delete(self, key):
    #     current = self._root
    #     parent = self._root
    #     isLeftChild = True

    #     while (current.getKey() != key):
    #         parent = current
    #         if (key < current.getKey()):
    #             isLeftChild = True
    #             current = current.getLeft()
    #         else:
    #             isLeftChild = False
    #             current = current.getRight()

    #         if current == None:
    #             raise ValueError("Key " + key + " was not found")
            
    #     if (current.getLeft() == None) and (current.getRight() == None):
    #         if (current == self._root):
    #             self._root = None
    #         elif (isLeftChild):
    #             parent.setLeft(None)
    #         else:
    #             parent.setRight(None)
    #     elif (current.getRight() == None):
    #         if (current == self._root):
    #             self._root = current.getLeft()
    #         elif (isLeftChild):
    #             parent.setLeft(current.getLeft())
    #         else:
    #             parent.setRight(current.getRight())
    #     elif (current.getLeft() == None):
    #         if (current == self._root):
    #             self._root = current.getRight()
    #         elif (isLeftChild):
    #             parent.setLeft(current.getLeft())
    #         else:
    #             parent.setRight(current.getRight())
    #     else:
    #         successor = self._getSuccessor(current)

    #         if (current == self._root):
    #             self._root = successor
    #         elif (isLeftChild):
    #             parent.setLeft(successor)
    #         else:
    #             parent.setRight(successor)
    #         successor.setLeft(current.getLeft())
    #     return


    # def _getSuccessor(delNode: DSATreeNode):
    #     parent = delNode
    #     successor = delNode
    #     current = delNode.getRight()
    #     while (current != None):
    #         parent = successor
    #         successor = current
    #         current.getLeft()
        
    #     if (successor != delNode.getRight()):
    #         parent.setLeft(successor.getRight())
    #         successor.setRight(delNode.getRight())
        
    #     return successor