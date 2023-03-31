import sys
import linkedList as LL


def usage():
    print(" Usage: py linkListTestHarness x")
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
                #Testing Single-Ended, Singly Linked linklist iterator
                print("\nTesting Single-Ended, Singly Linked linklist")

                print("\nInitialising list")
                singly = LL.DSASinglyLinkedList()

                print("Adding Values 1 - 8 (insertFirst)")
                singly.insertFirst(1)
                singly.insertFirst(2)
                singly.insertFirst(3)
                singly.insertFirst(4)
                singly.insertFirst(5)
                singly.insertFirst(6)
                singly.insertFirst(7)
                singly.insertFirst(8)
                singly.printList()

                print("\nIterating with for loop")
                for value in singly: 
                    print(value)

                print("\nInitialising iterator")
                singlyIter = iter(singly)

                print("Getting next value")
                print(next(singlyIter))
                print("Getting next value")
                print(next(singlyIter))
                print("Getting next value")
                print(next(singlyIter))
                print("Getting next value")
                print(next(singlyIter))
                print("Getting next value")
                print(next(singlyIter))
                print("Getting next value")
                print(next(singlyIter))
                print("Getting next value")
                print(next(singlyIter))
                print("Getting next value")
                print(next(singlyIter))
                print("Getting next value")
                print(next(singlyIter))


            elif sys.argv[1] == "d":
                #Testing Double-Ended, Doubly Linked linklist
                print("\nTesting Double-Ended, Doubly Linked linklist")

                print("\nInitialising list")
                doubly = LL.DSADoublyLinkedList()

                print("Adding Values a - h (insertLast)")
                doubly.insertLast("a")
                doubly.insertLast("b")
                doubly.insertLast("c")
                doubly.insertLast("d")
                doubly.insertLast("e")
                doubly.insertLast("f")
                doubly.insertLast("g")
                doubly.insertLast("h")
                doubly.printList()
                
                print("\nIterating with for loop")
                for value in doubly: 
                    print(value)

                print("\nInitialising iterator")
                doublyIter = iter(doubly)

                print("Getting next value")
                print(next(doublyIter))
                print("Getting next value")
                print(next(doublyIter))
                print("Getting next value")
                print(next(doublyIter))
                print("Getting next value")
                print(next(doublyIter))
                print("Getting next value")
                print(next(doublyIter))
                print("Getting next value")
                print(next(doublyIter))
                print("Getting next value")
                print(next(doublyIter))
                print("Getting next value")
                print(next(doublyIter))
                print("Getting next value")
                print(next(doublyIter))

            else:
                print("Incorrect x term!")
                usage()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    __main__()