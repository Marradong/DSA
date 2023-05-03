#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
import numpy as np
import random

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
    leftIdx = 0
    rightIdx = len(A) - 1
    mergeSortRecurse(A, leftIdx, rightIdx)
    print(A)


def mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = int((leftIdx + rightIdx) / 2)
        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)
    return


def merge(A, leftIdx, midIdx, rightIdx):
    tempArr = np.empty((rightIdx - leftIdx + 1))
    i = leftIdx
    j = midIdx + 1
    k = 0
    while (i <= midIdx) and (j <= rightIdx):
        if (A[i] <= A[j]):
            tempArr[k] = A[i]
            i = i + 1
        else:
            tempArr[k] = A[j]
            j = j + 1
        k = k + 1
    
    for ii in range(i, midIdx+1):
        tempArr[k] = A[ii]
        k = k + 1
    for jj in range(j, rightIdx):
        tempArr[k] = A[jj]
        k = k + 1
    for kk in range(leftIdx, rightIdx-1):
        A[kk] = tempArr[kk - leftIdx]
    return


def quickSort(A):
    leftIdx = 0
    rightIdx = len(A) - 1
    quickSortRecurse(A, leftIdx, rightIdx)
    print(A)


def quickSortRecurse(A, leftIdx, rightIdx):
    if (rightIdx > leftIdx):
        pivotIdx = int((leftIdx + rightIdx)/2)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRecurse(A, leftIdx, newPivotIdx-1)
        quickSortRecurse(A, newPivotIdx+1, rightIdx)
    return


def quickSortMedian3(A):
    leftIdx = 0
    rightIdx = len(A) - 1
    quickSortMedian3Recurse(A, leftIdx, rightIdx)
    print(A)


def quickSortMedian3Recurse(A, leftIdx, rightIdx):
    if (rightIdx > leftIdx):
        lIdx = leftIdx
        rIdx = rightIdx
        mIdx = int((leftIdx + rightIdx)/2)
        if A[lIdx] > A[mIdx]:
            temp = lIdx
            lIdx = mIdx
            mIdx = temp
        if A[mIdx] > A[rIdx]:
            temp = rIdx
            rIdx = mIdx
            mIdx = temp
            if A[lIdx] > A[mIdx]:
                temp = lIdx
                lIdx = mIdx
                mIdx = temp
        pivotIdx = mIdx
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortMedian3Recurse(A, leftIdx, newPivotIdx-1)
        quickSortMedian3Recurse(A, newPivotIdx+1, rightIdx)
    return


def quickSortRandom(A):
    leftIdx = 0
    rightIdx = len(A) - 1
    quickSortRandomRecurse(A, leftIdx, rightIdx)
    print(A)


def quickSortRandomRecurse(A, leftIdx, rightIdx):
    if (rightIdx > leftIdx):
        pivotIdx = random.randint(leftIdx, rightIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)
        quickSortRandomRecurse(A, leftIdx, newPivotIdx-1)
        quickSortRandomRecurse(A, newPivotIdx+1, rightIdx)


def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    pivotVal = A[pivotIdx]
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivotVal

    currIdx = leftIdx
    for i in range(leftIdx, rightIdx):
        if A[i] < pivotVal:
            temp = A[i]
            A[i] = A[currIdx]
            A[currIdx] = temp
            currIdx = currIdx + 1
    newPivotIdx = currIdx
    A[rightIdx] = A[newPivotIdx]
    A[newPivotIdx] = pivotVal
    return newPivotIdx
