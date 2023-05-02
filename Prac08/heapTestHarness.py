import heap
import numpy as np


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

    print("\nAdding Entry with value O priority 2")
    DSAHeap.add(2,"O")

    DSAHeap.display()

    print("\nRemoving item - Value: ", DSAHeap.remove())
    DSAHeap.display()
    print("\nRemoving item - Value: ", DSAHeap.remove())
    DSAHeap.display()
    print("\nRemoving item - Value: ", DSAHeap.remove())
    DSAHeap.display()
    print("\nRemoving item - Value: ", DSAHeap.remove())
    DSAHeap.display()

    sortTest = heap.DSAHeap()
    randomArray = np.random.randint(0, 10, 10)
    for i in range(len(randomArray)):
        sortTest.add(randomArray[i], randomArray[i])
    print("\nBefore Sort")
    sortTest.display()
    print("\nAfter Sort")
    sortTest.heapSort()
    sortTest.display()



if __name__ == "__main__":
    __main__()