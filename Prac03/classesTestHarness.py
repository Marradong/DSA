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
    print("        y is one of")
    print("           a - 1..n ascending")
    print("           d - 1..n descending")
    print("           r - 1..n in random order")
    print("           n - 1..n nearly sorted (10% moved)")

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
        elif arrayType == 'n':
            for i in range(int(capacity*NEARLY_PERCENT/2+1)):
                x = int(random.random()*capacity)
                y = int(random.random()*capacity)
                temp = A[x]
                A[x] = A[y]
                A[y] = temp
            print("Nearly sorted: ", A)
        else:
            print("Unsupported array type")
            usage()

        if classType == "s":
            print("Initialising Stack")
            DSAStack = classes.DSAStack(capacity)
            print("Current Stack", DSAStack.stack)
            print("Is stack empty: ", DSAStack.isEmpty())
            print("Is stack full: ", DSAStack.isFull())
            print("Adding items to Stack")
            for item in A:
                DSAStack.push(item)
            print("Current Stack", DSAStack.stack)   
            print("Is stack empty: ", DSAStack.isEmpty())
            print("Is stack full: ", DSAStack.isFull())
            print("removing items from Stack")
            for i in range(DSAStack.count):
                print("removing item: ", DSAStack.pop())
            print("Current Stack", DSAStack.stack)   
            print("Is stack empty: ", DSAStack.isEmpty())
            print("Is stack full: ", DSAStack.isFull())
            


        elif classType == "q":
            print("Initialising Queue")
            DSAQueue = classes.DSAQueue(capacity)
            print("Current Queue", DSAQueue.queue)
            print("Is Queue empty: ", DSAQueue.isEmpty())
            print("Is Queue full: ", DSAQueue.isFull())
            print("Adding items to Queue")
            for item in A:
                DSAQueue.enqueue(item)
            print("Current Queue", DSAQueue.queue)   
            print("Is Queue empty: ", DSAQueue.isEmpty())
            print("Is Queue full: ", DSAQueue.isFull())
            print("removing items from Queue")
            for i in range(DSAQueue.count):
                print("removing item: ", DSAQueue.dequeue())
            print("Current Queue", DSAQueue.queue)   
            print("Is Queue empty: ", DSAQueue.isEmpty())
            print("Is Queue full: ", DSAQueue.isFull())
        else:
            print("Unsupported sort algorithm")
            usage()

        for i in range(capacity-2):
            if (A[i] > A[i+1]):
                raise ValueError("Array not in order")


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

if checkArgs():
    usage()
else:        
        classType = sys.argv[1][0]
        arrayType = sys.argv[1][1]
        capacity = int(sys.argv[2])

        runningTotal = 0

        startTime = timeit.default_timer()
        doTest(capacity, classType, arrayType)
        endTime = timeit.default_timer()

        runningTotal += (endTime - startTime)
    
        print(classType + arrayType + " " + str(capacity) + " " + str(runningTotal))
