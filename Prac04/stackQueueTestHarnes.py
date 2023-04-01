#**
#** Testharness to generate various different types of arrays of integers
#** and then sort them using various sorts.
#**


import numpy as np
import sys
import stackQueue
import random


NEARLY_PERCENT = 0.10 #% of items to move in nearly sorted array
RANDOM_TIMES = 100    #No times to randomly swap elements in array

def usage():
    print(" Usage: py classesTestHarness x n")
    print("        where")
    print("        n is the amount of items to add to the stack/queue")
    print("        x is one of")
    print("           s - stack")
    print("           q - queue")

def doTest(capacity, classType):
        A = np.arange(1, capacity+1, 1)   #create array with values from 1 to n

        if classType == "s":
            print("\nInitialising Stack")
            DSAStack = stackQueue.DSAStack()
            print("Is stack empty: ", DSAStack.isEmpty())

            print("\nAdding items to Stack")
            for item in A:
                DSAStack.push(item)
                print("Adding item: ", item)

            print("\nIterating through stack")
            print("---Top---")
            for items in DSAStack:
                print(items)
            print("---Bottom---")

            print("\nPeeking top of stack: ", DSAStack.top())

            print("\nRemoving items from Stack")
            while not DSAStack.isEmpty():
                print("Removing item: ", DSAStack.pop())
            print("Is stack empty: ", DSAStack.isEmpty(), "\n")

        elif classType == "q":
            print("\nInitialising Queue")
            DSAQueue = stackQueue.DSAQueue()
            print("Is Queue empty: ", DSAQueue.isEmpty())

            print("\nAdding items to Queue")
            for item in A:
                DSAQueue.enqueue(item)
                print("Adding item: ", item)

            print("\nIterating through Queue")
            print("---Front---")
            for items in DSAQueue:
                print(items)
            print("---Back---")

            print("\nPeeking first item in queue: ", DSAQueue.peek())

            print("\nRemoving items from Queue")
            while not DSAQueue.isEmpty():
                print("Removing item: ", DSAQueue.dequeue())
            print("Is Queue empty: ", DSAQueue.isEmpty(), "\n")

        else:
            print("Incorrect x term")
            usage()
            return


def checkArgs():
    argsOK = False
    if len(sys.argv) < 3:
        argsOK = True
    else:
        try:
            int(sys.argv[2])
        except ValueError:
            print("Input n must be an integer")
            argsOK = True

    return argsOK

#main program
def __main__():
    try:
        if checkArgs():
            usage()
        else:        
                classType = sys.argv[1]
                capacity = int(sys.argv[2])

                doTest(capacity, classType)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    __main__()
