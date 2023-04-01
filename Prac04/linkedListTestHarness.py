import sys
import linkedList as LL


def usage():
    print(" Usage: py linkedListTestHarness x")
    print("        where")
    print("        x is one of")
    print("           s - Single-Ended, Singly Linked")
    print("           d - Double-Ended, Doubly Linked")


def __main__():
    try:
        if len(sys.argv) != 2:
            usage()
        else:
            if sys.argv[1] == "s":
                #Testing Single-Ended, Singly Linked linklist
                print("\nTesting Single-Ended, Singly Linked linklist")

                print("Initialising list")
                singly = LL.DSASinglyLinkedList()

                print("Checking if list is empty: ", singly.isEmpty())

                print("Inserting first")
                singly.insertFirst(1)
                singly.printList()

                print("Inserting first")
                singly.insertFirst(2)
                singly.printList()

                print("Inserting last")
                singly.insertLast(3)
                singly.printList()

                print("Peek first")
                print(singly.peekFirst())

                print("Peek last")
                print(singly.peekLast())

                print("Removing first")
                singly.removeFirst()
                singly.printList()

                print("Removing first")
                singly.removeFirst()
                singly.printList()

                print("Removing last")
                singly.removeLast()

                print("Checking if list is empty")
                print(singly.isEmpty())

            elif sys.argv[1] == "d":
                #Testing Double-Ended, Doubly Linked linklist
                print("\nTesting Double-Ended, Doubly Linked linklist")

                print("Initialising list")
                doubly = LL.DSADoublyLinkedList()

                print("Checking if list is empty: ", doubly.isEmpty())

                print("Inserting first")
                doubly.insertFirst("a")
                doubly.printList()

                print("Inserting first")
                doubly.insertFirst("b")
                doubly.printList()

                print("Inserting last")
                doubly.insertLast("c")
                doubly.printList()

                print("Peek first")
                print(doubly.peekFirst())

                print("Peek last")
                print(doubly.peekLast())

                print("Removing first")
                doubly.removeFirst()
                doubly.printList()

                print("Removing first")
                doubly.removeFirst()
                doubly.printList()

                print("Removing last")
                doubly.removeLast()

                print("Checking if list is empty")
                print(doubly.isEmpty())
            else:
                print("Incorrect x term!")
                usage()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    __main__()