from ClassDefinitions import heap

def __main__():

    print("\nInitialising a heap")
    DSAHeap = heap.DSAHeap()

    print("\nAdding Entry with value A priority 1")
    DSAHeap.add(1,"A")
    print("Adding Entry with value B priority 1")
    DSAHeap.add(1,"B")
    print("Adding Entry with value C priority 1")
    DSAHeap.add(1,"C")

    DSAHeap.display()

    print("\nAdding Entry with value X priority 3")
    DSAHeap.add(3,"X")
    print("Adding Entry with value Y priority 3")
    DSAHeap.add(3,"Y")
    print("Adding Entry with value Z priority 3")
    DSAHeap.add(3,"Z")

    DSAHeap.display()

    print("\nIs X added to heap? ", DSAHeap.isAdded("X"))
    print("Is A added to heap? ", DSAHeap.isAdded("A"))

    print("\nRemoving item - Value: ", DSAHeap.remove())
    DSAHeap.display()
    print("\nRemoving item - Value: ", DSAHeap.remove())
    DSAHeap.display()
    print("\nRemoving item - Value: ", DSAHeap.remove(), "\n")
    DSAHeap.display()

if __name__ == "__main__":
    __main__()

