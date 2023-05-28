from ClassDefinitions import stackQueue as sq
import numpy as np

def __main__():
    A = np.arange(1, 11, 1)
    print("Initialising Stack")
    DSAStack = sq.DSAStack()
    DSAStack.printStack()
    print("Is stack empty: ", DSAStack.isEmpty())
    print("Adding items to Stack")
    for item in A:
        DSAStack.push(item)
    DSAStack.printStack()
    print("Peeking top of in stack: ", DSAStack.top().getValue())   
    print("Is stack empty: ", DSAStack.isEmpty())
    print("removing items from Stack")
    for i in DSAStack:
        print("removing item: ", DSAStack.pop())
    DSAStack.printStack()   
    print("Is stack empty: ", DSAStack.isEmpty())

    print("\nInitialising Queue")
    DSAQueue = sq.DSAQueue()
    DSAQueue.printQueue()
    print("Is Queue empty: ", DSAQueue.isEmpty())
    print("Adding items to Queue")
    for item in A:
        DSAQueue.enqueue(item)
    DSAQueue.printQueue()   
    print("Is Queue empty: ", DSAQueue.isEmpty())
    print("Peeking first item in queue: ", DSAQueue.peek().getValue())
    print("removing items from Queue")
    for i in DSAQueue:
        print("removing item: ", DSAQueue.dequeue())
    DSAQueue.printQueue()   
    print("Is Queue empty: ", DSAQueue.isEmpty())

if __name__ == "__main__":
    __main__()