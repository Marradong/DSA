import sys
import linkedList as LL
import pickle


def printCommands():
    print("\nHere is a list of valid commands (command - description): ")
    print("           if - Insert First")
    print("           il - Insert Last")
    print("           rf - Remove First")
    print("           rl - Remove Last")
    print("           dl - Display List")
    print("           wf - Write serialised file")
    print("           cm - Close Menu without writing to a file")


def __main__():
    try:
        userInput = str(input("\nWould you like to read a serialised file (yes/no)? "))
        while (userInput != "yes") and (userInput != "no"):
            print("\nInvalid Input! Please enter 'yes' or 'no'")
            userInput = str(input("Would you like to read a serialised file (yes/no)? "))

        if (userInput == "yes"):
            fileName = str(input("\nPlease provide a file name to read from: "))
            try: 
                with open(fileName, "rb") as dataFile: 
                    llist = pickle.load(dataFile) 
            except: 
                raise Exception("Error: Object file does not exist!")
            
        elif (userInput == "no"):
            print("\nInitialising linked list")
            llist = LL.DSADoublyLinkedList()

        printCommands()
        userCommand = ""

        while (userCommand != "cm") and (userCommand != "wf"):
            userCommand = str(input("\nPlease enter a valid command: "))

            if userCommand == "if":
                userVal = input("Please enter the value you would like to insert: ")
                llist.insertFirst(userVal)

            elif userCommand == "il":
                userVal = input("Please enter the value you would like to insert: ")
                llist.insertLast(userVal)

            elif userCommand == "rf":
                if llist.isEmpty():
                    print("List is Empty")
                else:
                    print("Removing first")
                    llist.removeFirst()

            elif userCommand == "rl":
                if llist.isEmpty():
                    print("List is Empty")
                else:
                    print("Removing last")
                    llist.removeLast()

            elif userCommand == "dl":
                print("----head----")
                for item in llist:
                    print(item)
                print("----tail----")

            elif userCommand == "wf":
                try: 
                    with open("linkedlist", "wb") as dataFile: 
                        pickle.dump(llist, dataFile) 
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