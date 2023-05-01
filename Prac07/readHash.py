import hash

def __main__():
    
    try:
        fileObj = open("RandomNames7000.csv", "r")
        DSAHashTable = hash.DSADoubleHashTable(7000)
        line = fileObj.readline()
        lineNum = 0
        while line:
            splitLine = line.split(",")
            DSAHashTable.put(str(splitLine[0]), str(splitLine[1]))
            line = fileObj.readline()
            lineNum = lineNum + 1
        DSAHashTable.export()
        DSAHashTable.saveCSV()
        print("Number of lines in file: ", lineNum)
        print("Number of entries in table: ", DSAHashTable._count)
        fileObj.close()
    except IOError as e:
        print("File Processing Error: " + str(e))

if __name__ == "__main__":
    __main__()