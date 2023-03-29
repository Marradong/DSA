
import sys
import timeit
import callStack
import classes as cl

def usage():
    print(" Usage: ClallStackTestHarness n xy")
    print("        where")
    print("        n is number input for functions")
    print("        x is one of")
    print("           b - fibonacci")
    print("           c - factorial")
    print("        y is one of")
    print("           r - recursive")
    print("           i - iterative")

def doCallStack(n, functionType, callType):
    callstk = cl.DSAStack(1000)
    if callStack != None:
        if functionType == "b":
            if callType == "r":
                callStack.fibRecursive(n, callstk)
            elif callType == "i":
                callStack.fibIterative(n, callstk)
        elif functionType == "c":
            if callType == "r":
                callStack.factRecursive(n, callstk)
            elif callType == "i":
                callStack.factIterative(n, callstk)
        else:
            print("Unsupported function")


def checkArgs():
    argsOK = False
    if len(sys.argv) < 3:
        argsOK = True
    try:
        sys.argv[2][0]    
        sys.argv[2][1]
        int(sys.argv[1])
    except IndexError:
        print("Incorrect xy terms")
        argsOK = True
    except ValueError:
        print("Input n must be an integer")
        argsOK = True

    return argsOK

#main program

if not checkArgs:
    usage()
else:
    for aa in range(2, len(sys.argv)):
        
        n = int(sys.argv[1])
        functionType = sys.argv[aa][0]
        callType = sys.argv[aa][1]
        runningTotal = 0

        startTime = timeit.default_timer()
        doCallStack(n, functionType, callType)
        endTime = timeit.default_timer()

        runningTotal += (endTime - startTime)
    
        print(functionType + callType + " " + str(n) + " " + str(runningTotal))
