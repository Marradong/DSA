from ClassDefinitions import linkedList as LL

# taken from Prac04
def __main__():

    print("\nInitialising list")
    doubly = LL.DSADoublyLinkedList()

    print("Checking if list is empty: ", doubly.isEmpty())

    print("Inserting first")
    doubly.insertFirst("a")
    doubly.printList()

    print("Inserting first")
    doubly.insertFirst("b")
    doubly.printList()

    print("Inserting last")
    newNode = LL.DSADoublyListNode("c")
    doubly.insertLast(newNode)
    doubly.printList()

    print("Inserting last")
    doubly.insertLast("d")
    doubly.printList()

    print("Peek first")
    print(doubly.peekFirst().getValue())

    print("Peek last")
    print(doubly.peekLast())

    print("Removing C")
    doubly.remove("c")
    doubly.printList()

    print("Removing first")
    doubly.removeFirst()
    doubly.printList()

    print("Removing first")
    doubly.removeFirst()
    doubly.printList()

    print("Removing last")
    doubly.removeLast()

    print("Checking if list is empty: ", doubly.isEmpty())

if __name__ == "__main__":
    __main__()