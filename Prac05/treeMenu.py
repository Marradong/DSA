import sys
import tree
import pickle


def traversalMethods():
    print("\nHere is a list of valid traversal methods (command - description): ")
    print("           in - Show inorder traversal")
    print("           pre - Show preorder traversal")
    print("           post - Show postorder traversal")


def printCommands():
    print("\nHere is a list of valid commands (command - description): ")
    print("           i - Insert Node")
    print("           f - Find Node")
    print("           r - Remove Node")
    print("           d - Display Tree")
    print("           mi - Min of Tree")
    print("           ma - Max of Tree")
    print("           h - Height of Tree")
    print("           b - Balance of Tree")
    print("           ws - Write Serialised file")
    print("           wc - Write CSV file")
    print("           cm - Close Menu without writing to a file")


def usage():
    print(" Usage: py treeMenu x")
    print("        where")
    print("        x is one of")
    print("           rs - Read Serialised file")
    print("           rc - Read CSV file")
    print("           nt - Create New Tree")


def checkArgs():
    argsOK = True
    if len(sys.argv) != 3:
        argsOK = False
    else:
        try:
            sys.argv[1][0]    
            sys.argv[1][1]
        except IndexError:
            print("Incorrect x term")
            argsOK = False
            

def __main__():
    if len(sys.argv) != 2:
        usage()
    else:
        try:
            if sys.argv[1] == "rs":
                fileName = str(input("\nPlease provide a file name to read from: "))
                try: 
                    with open(fileName, "rb") as dataFile: 
                        DSAtree = pickle.load(dataFile) 
                    dataFile.close()
                except Exception as e:
                    print(e)
            elif sys.argv[1] == "rc":
                fileName = str(input("\nPlease provide a file name to read from: "))
                try:
                    with open(fileName,"r") as csvFile:
                        treeOrder = csvFile.readline()
                        treeItems = treeOrder.split(",")
                        DSAtree = tree.DSABinarySearchTree()
                        for node in treeItems:
                            valueKey = node.split(":")
                            DSAtree.insert(valueKey[1], valueKey[0])
                    csvFile.close()
                except Exception as e:
                    print(e)

                
            elif sys.argv[1] == "nt":
                print("\nInitialising Tree")
                DSAtree = tree.DSABinarySearchTree()
            else:
                raise ValueError("Incorrect x term")

            printCommands()
            userCommand = ""

            while (userCommand != "cm") and (userCommand != "ws") and (userCommand != "wc"):
                userCommand = str(input("\nPlease enter a valid command: "))

                if userCommand == "i":
                    userVal = input("Please enter a new value: ")
                    userKey = input("Please enter a new key: ")
                    try:
                        DSAtree.insert(int(userKey), userVal)
                    except TypeError:
                        print("key must be an integer! Node was not added to tree.")
                elif userCommand == "f":
                    userKey = input("Please enter a key to find: ")
                    print("Result: ", DSAtree.find(userKey))
                elif userCommand == "r":
                    userKey = int(input("Please enter a key to remove: "))
                    DSAtree.delete(userKey)
                elif userCommand == "d":
                    traversalMethods()
                    userMethod = str(input("\nPlease enter a valid method: "))
                    if userMethod == "in":
                        print("Traversal Method is Inorder: ", DSAtree.inorder())
                    elif userMethod == "pre":
                        print("Traversal Method is Preorder: ", DSAtree.preorder())
                    elif userMethod == "post":
                        print("Traversal Method is Postorder: ", DSAtree.postorder())
                    else:
                        print("Invalid Traversal Method")
                    print()
                    print("Complete tree")
                    DSAtree.display()
                    print()
                elif userCommand == "mi":
                    print("Tree Min: ", DSAtree.min())
                elif userCommand == "ma":
                    print("Tree Max: ", DSAtree.max())
                elif userCommand == "h":
                    print("Tree Height: ", DSAtree.height())
                elif userCommand == "b":
                    print("Tree Balance: ", DSAtree.balance())
                elif userCommand == "in":
                    print(DSAtree.inorder()) 
                elif userCommand == "pre":
                    print(DSAtree.preorder())
                elif userCommand == "post":
                    print(DSAtree.postorder())
                elif userCommand == "wc":
                    traversalMethods()
                    userMethod = str(input("\nPlease enter a valid method: "))
                    if userMethod == "in":
                        inorderStr = DSAtree.inorder()
                        inorderItems = inorderStr.split(" ")
                        newLine = ",".join(inorderItems)
                        newLine = newLine.lstrip(",")
                        try: 
                            with open("tree.csv", "w") as csvFile: 
                                csvFile.write(newLine) 
                            csvFile.close()
                            print("Inorder written to file")
                        except Exception as e:
                            print(e)
                    elif userMethod == "pre":
                        preorderStr = DSAtree.inorder()
                        preorderItems = preorderStr.split(" ")
                        newLine = ",".join(preorderItems)
                        newLine = newLine.lstrip(",")
                        try: 
                            with open("tree.csv", "w") as csvFile: 
                                csvFile.write(newLine) 
                            csvFile.close()
                            print("Preorder written to file")
                        except Exception as e:
                            print(e)
                    elif userMethod == "post":
                        postorderStr = DSAtree.inorder()
                        postorderItems = postorderStr.split(" ")
                        newLine = ",".join(postorderItems)
                        newLine = newLine.lstrip(",")
                        try: 
                            with open("tree.csv", "w") as csvFile: 
                                csvFile.write(newLine) 
                            csvFile.close()
                            print("Postorder written to file")
                        except Exception as e:
                            print(e)
                    else:
                        print("Invalid Traversal Method")
                        userCommand = ""
                elif userCommand == "ws":
                    try: 
                        with open("tree", "wb") as dataFile: 
                            pickle.dump(DSAtree, dataFile) 
                        print("File has been written. Exiting Menu")
                    except: 
                        print("Error: problem pickling object!")

                else:
                    print("Invalid command please see list below")
                    printCommands()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    __main__()