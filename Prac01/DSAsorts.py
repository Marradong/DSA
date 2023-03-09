#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    for passNum in range(0, len(A)-1):
        swapped = False
        for i in range(0, len(A)-1-passNum):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                swapped = True
        if swapped is False:
            break

    print(A)


def insertionSort(A):
    for n in range(1, len(A)):
        i = n
        temp = A[i]
        while (i > 0) and (A[i-1] > temp):
            A[i] = A[i-1]
            i = i-1
        A[i] = temp
    print(A)


def selectionSort(A):
    for n in range(0, len(A)):
        minI = n
        for i in range(n+1, len(A)):
            if (A[i] < A[minI]):
                minI = i
        temp = A[minI]
        A[minI] = A[n]
        A[n] = temp
    print(A)


def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...


def mergeSortRecurse(A, leftIdx, rightIdx):
    ...


def merge(A, leftIdx, midIdx, rightIdx):
    ...


def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...


def quickSortRecurse(A, leftIdx, rightIdx):
    ...


def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...
