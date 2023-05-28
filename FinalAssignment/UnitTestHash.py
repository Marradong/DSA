from ClassDefinitions import hash

# taken from prac07
def __main__():

    print("\nInitialising a hash table with capacity 6")
    DSAHashTable = hash.DSADoubleHashTable(6)

    print("\nAdding Entry with value 1 key 123")
    print("Did the table resize: ", DSAHashTable.put("123", 1))
    print("Adding Entry with value 2 key 234")
    print("Did the table resize: ", DSAHashTable.put("234", 2))
    print("Adding Entry with value 3 key 345")
    print("Did the table resize: ", DSAHashTable.put("345", 3))
    print("Adding Entry with value 4 key 456")
    print("Did the table resize: ", DSAHashTable.put("456", 4))
    print("Adding Entry with value 5 key 567")
    print("Did the table resize: ", DSAHashTable.put("567", 5))
    print("Adding Entry with value 6 key 678")
    print("Did the table resize: ", DSAHashTable.put("678", 6))
    print("Adding Entry with value 7 key 789")
    print("Did the table resize: ", DSAHashTable.put("789", 7))

    print("\nHash Table Load Factor: ", DSAHashTable.getLoadFactor())

    DSAHashTable.export()

    print("\nGet Value of Entry with key 345 (3): ", DSAHashTable.get("345"))
    print("Get Value of Entry with key 123 (1): ", DSAHashTable.get("123"))
    print("Get Value of Entry with key 789 (7): ", DSAHashTable.get("789"))

    print("\nRemoving Entry with key 456")
    print("Did the table resize: ", DSAHashTable.remove("456"))
    print("Removing Entry with key 567")
    print("Did the table resize: ", DSAHashTable.remove("567"))
    print("Removing Entry with key 678")
    print("Did the table resize: ", DSAHashTable.remove("678"))
    print("Removing Entry with key 789")
    print("Did the table resize: ", DSAHashTable.remove("789"))

    print("\nHash Table Load Factor: ", DSAHashTable.getLoadFactor())
    
    DSAHashTable.export()


if __name__ == "__main__":
    __main__()