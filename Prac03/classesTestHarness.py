#**
#** Testharness to generate various different types of arrays of integers
#** and then sort them using various sorts.
#**


import numpy as np
import sys
import timeit
import classes
import random


NEARLY_PERCENT = 0.10 #% of items to move in nearly sorted array
RANDOM_TIMES = 100    #No times to randomly swap elements in array

def usage():
    print(" Usage: py classesTestHarness xy c")
    print("        where")
    print("        c is the capacity of stack/queue")
    print("        x is one of")
    print("           s - stack")
    print("           q - queue")
    print("           c - circular queue")
    print("           f - shuffling queue")
    print("        y is one of")
    print("           a - 1..n ascending")
    print("           d - 1..n descending")
    print("           r - 1..n in random order")

def doTest(capacity, classType, arrayType):
        A = np.arange(1, capacity+1, 1)   #create array with values from 1 to n
        
        if arrayType == 'a':
            ...
        elif arrayType =='d':  #convert to descending
            for i in range(0, int(capacity/2)):
                temp = A[i]
                A[i] = A[capacity-i-1]
                A[capacity-i-1] = temp
            print("Descending: ", A)
        elif arrayType == 'r':
            for i in range(RANDOM_TIMES*capacity):
                x = int(random.random()*capacity)
                y = int(random.random()*capacity)
                temp = A[x]
                A[x] = A[y]
                A[y] = temp
            print("Random: ", A)
        else:
            print("Unsupported array type")
            usage()
            return

        if classType == "s":
            print("Initialising Stack")
            DSAStack = classes.DSAStack(capacity)
            DSAStack.printStack()
            print("Is stack empty: ", DSAStack.isEmpty())
            print("Is stack full: ", DSAStack.isFull())
            print("Adding items to Stack")
            for item in A:
                DSAStack.push(item)
            DSAStack.printStack()
            print("\nPeeking top of in stack: ", DSAStack.top())   
            print("Is stack empty: ", DSAStack.isEmpty())
            print("Is stack full: ", DSAStack.isFull())
            print("removing items from Stack")
            for i in range(DSAStack.getCount()):
                print("removing item: ", DSAStack.pop())
            DSAStack.printStack()   
            print("Is stack empty: ", DSAStack.isEmpty())
            print("Is stack full: ", DSAStack.isFull())

        elif classType == "q":
            print("Initialising Queue")
            DSAQueue = classes.DSAQueue(capacity)
            DSAQueue.printQueue()
            print("Is Queue empty: ", DSAQueue.isEmpty())
            print("Is Queue full: ", DSAQueue.isFull())
            print("Adding items to Queue")
            for item in A:
                DSAQueue.enqueue(item)
            DSAQueue.printQueue()   
            print("Is Queue empty: ", DSAQueue.isEmpty())
            print("Is Queue full: ", DSAQueue.isFull())
            print("\nPeeking first item in queue: ", DSAQueue.peek())
            print("removing items from Queue")
            for i in range(DSAQueue.getCount()):
                print("removing item: ", DSAQueue.dequeue())
            DSAQueue.printQueue()   
            print("Is Queue empty: ", DSAQueue.isEmpty())
            print("Is Queue full: ", DSAQueue.isFull())

        elif classType == "c":
            print("\nInitialising Circular Queue")
            DSACircularQueue = classes.DSACircularQueue(capacity)
            DSACircularQueue.printQueue()
            print("Is Queue empty: ", DSACircularQueue.isEmpty())
            print("Is Queue full: ", DSACircularQueue.isFull())
            print("\nAdding items to Queue")
            for item in A:
                DSACircularQueue.enqueue(item)
            DSACircularQueue.printQueue()   
            print("Is Queue empty: ", DSACircularQueue.isEmpty())
            print("Is Queue full: ", DSACircularQueue.isFull())
            print("\nPeeking first item in queue: ", DSACircularQueue.peek())
            print("\nTesting circularity")
            print("removing item: ", DSACircularQueue.dequeue())
            for i in range(capacity + 2):
                print("removing item: ", DSACircularQueue.dequeue())
                DSACircularQueue.printQueue()
                print("adding item: ", 1)
                DSACircularQueue.enqueue(1)
                DSACircularQueue.printQueue()
            print("\nRemoving all items from Queue")
            for i in range(DSACircularQueue.getCount()):
                print("removing item: ", DSACircularQueue.dequeue())
            DSACircularQueue.printQueue()   
            print("Is Queue empty: ", DSACircularQueue.isEmpty())
            print("Is Queue full: ", DSACircularQueue.isFull())
        
        elif classType == "f":
            print("Initialising Shuffling Queue")
            DSAShufflingQueue = classes.DSAShufflingQueue(capacity)
            DSAShufflingQueue.printQueue()
            print("Is Shuffling Queue empty: ", DSAShufflingQueue.isEmpty())
            print("Is Shuffling Queue full: ", DSAShufflingQueue.isFull())
            print("Adding items to Queue")
            for item in A:
                DSAShufflingQueue.enqueue(item)
            DSAShufflingQueue.printQueue()  
            print("\nPeeking first item in queue: ", DSAShufflingQueue.peek()) 
            print("Is Shuffling Queue empty: ", DSAShufflingQueue.isEmpty())
            print("Is Shuffling Queue full: ", DSAShufflingQueue.isFull())
            print("removing items from Queue")
            for i in range(DSAShufflingQueue.getCount()):
                print("removing item: ", DSAShufflingQueue.dequeue())
            DSAShufflingQueue.printQueue()   
            print("Is Shuffling Queue empty: ", DSAShufflingQueue.isEmpty())
            print("Is Shuffling Queue full: ", DSAShufflingQueue.isFull())

        else:
            print("Unsupported sort algorithm")
            usage()
            return


def checkArgs():
    argsOK = False
    if len(sys.argv) < 3:
        argsOK = True
    try:
        sys.argv[1][0]    
        sys.argv[1][1]
        int(sys.argv[2])
    except IndexError:
        print("Incorrect xy terms")
        argsOK = True
    except ValueError:
        print("Input c must be an integer")
        argsOK = True

    return argsOK

#main program
def __main__():
    try:
        if checkArgs():
            usage()
        else:        
                classType = sys.argv[1][0]
                arrayType = sys.argv[1][1]
                capacity = int(sys.argv[2])

                doTest(capacity, classType, arrayType)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    __main__()
