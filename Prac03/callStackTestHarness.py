import classes as cl
import callStack

def __main__():
    try:
        stack = cl.DSAStack()
        nUser = int(input("\nEnter a numer for the fibonacci functions: "))
        val = callStack.fibRecursive(nUser, stack)
        print("The recursive fibonacci function gives a value of: ", val)
        val = callStack.fibIterative(nUser, stack)
        print("The iterative fibonacci function gives a value of: ", val)
        nUser = int(input("\nEnter a numer for the factorial functions: "))
        val = callStack.factRecursive(nUser, stack)
        print("The recursive factorial function gives a value of: ", val)
        val = callStack.factIterative(nUser, stack)
        print("The iterative factorial function gives a value of: ", val)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    __main__()