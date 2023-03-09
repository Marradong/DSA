#
# File containing parsing methods for known csv file
# RandomNames7000.csv
#
# Author: Ethan Batt
# Date: 2 March 2023

import numpy as np
import DSAsorts


class Student(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


# processing function
def processLine(csvRow):
    tokens = csvRow.split(",")
    try:
        id = int(tokens[0])
        name = tokens[1]
        newStudent = Student(id, name)
        return newStudent
    except TypeError:
        raise TypeError("Invalid CSV Row Format")


# main program
unsortedArr = np.zeros(7000, dtype=int)

try:
    fileObj = open("RandomNames7000.csv", "r")
    lineNum = 0
    line = fileObj.readline()
    while line:
        nextStudent = processLine(line)
        unsortedArr[lineNum] = nextStudent.id
        lineNum = lineNum + 1
        line = fileObj.readline()
    fileObj.close()
except IOError as e:
    print("File Processing Error: " + str(e))

bubbleArr = unsortedArr.copy()
selectArr = unsortedArr.copy()
insertArr = unsortedArr.copy()

DSAsorts.bubbleSort(bubbleArr)
DSAsorts.selectionSort(selectArr)
DSAsorts.insertionSort(insertArr)

try:
    fileObj = open("RandomNames7000Results.csv", "w")

    fileObj.write("Sorted Bubble Array:")
    for i in range(len(bubbleArr)):
        fileObj.write(","+str(bubbleArr[i]))
    fileObj.write("\n")

    fileObj.write("Sorted Selection Array:")
    for i in range(len(selectArr)):
        fileObj.write(","+str(selectArr[i]))
    fileObj.write("\n")

    fileObj.write("Sorted Insertion Array:")
    for i in range(len(insertArr)):
        fileObj.write(","+str(insertArr[i]))

    fileObj.close()
except IOError as e:
    print("File Processing Error: " + str(e))
