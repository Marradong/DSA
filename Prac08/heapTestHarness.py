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

    try:
        trySort = input("\nWould you like to test heapSort()? (Yes/No): ")
        if trySort == "Yes":
            sortTest = heap.DSAHeap()
            sortInput = input("Would you like to test from a csv? (Yes/No): ")
            if sortInput == "Yes":
                fileName = input("Please enter the file name: ")
                fileObj = open(fileName, "r")
                line = fileObj.readline()
                while line:
                    line = line.strip("\n")
                    splitLine = line.split(",")
                    sortTest.add(splitLine[0], splitLine[0])
                    line = fileObj.readline()
                fileObj.close()
            else:
                arrLength = int(input("Please enter a length of array for testing: "))
                randomArray = np.random.randint(0, 10, arrLength)
                print("\nTesting Heap sort with a random array of size", arrLength, "numbers 0-9")
                for i in range(len(randomArray)):
                    sortTest.add(randomArray[i], randomArray[i])
                print("\nArray Before Sort:")
                for i in range(len(randomArray)):
                    print(randomArray[i], end=", ")
            print("\nSort Result:")
            sortTest.heapSort()
            for i in range(sortTest._count):
                print(sortTest.remove(), end=", ")
            print("\n")
        else:
            print("Sorting will not be tested")
    except ValueError:
        print("Please ensure inputs are entered correctly!")
    except IOError as e:
        print("File processing Error: ", e)


if __name__ == "__main__":
    __main__()