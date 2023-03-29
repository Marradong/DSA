import classes as cl


def display(stack: cl.DSAStack):
    print("-----Call Stack-----")
    for i in range(stack._count):
        print(stack._stack[0])
    print("-----End  Stack-----")


def callStack(stack: cl.DSAStack, function, args):
    if function != "":
        stack.push(str(function)+"("+str(args)+")")
    else: 
        stack.pop()
    return stack


###################################
# Recursive and Iterative Methods #
###################################


# Wrapper
def fibRecursive(n, stack: cl.DSAStack):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            stack = callStack(stack, "fibRecursive", n)
            display(stack)

            fibVal = _fibRecursive(n, stack)

            stack = callStack(stack, "", n)
            display(stack)

            return fibVal
    except TypeError:
        print("input must be a number")


# Method
def _fibRecursive(n, stack: cl.DSAStack):
    fibVal = 0
    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = fibRecursive(n-1, stack) + fibRecursive(n-2, stack)
    return fibVal

# Wrapper
def factRecursive(n, stack: cl.DSAStack):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            stack = callStack(stack, "factRecursive", n)
            display(stack)

            factVal = _factRecursive(n, stack)

            stack = callStack(stack, "", n)
            display(stack)

            return factVal
    except TypeError:
        print("input must be a number")


# Method
# max 499
def _factRecursive(n, stack: cl.DSAStack):
    if (n == 0):
        return 1
    else:
        return n * factRecursive((n-1), stack)
    

# Wrapper
def factIterative(n):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            stack = callStack(stack, "factIterative", n)
            display(stack)

            factVal = _factIterative(n)

            stack = callStack(stack, "", n)
            display(stack)

            return factVal
    except TypeError:
        print("input must be a number")


# Method
def _factIterative(n):
    nFactorial = 1
    for i in range(n, 1, -1):
        nFactorial = nFactorial * i
    return nFactorial
    

# Wrapper
def fibIterative(n, stack: cl.DSAStack):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            stack = callStack(stack, "fibIterative", n)
            display(stack)

            fibVal = _fibIterative(n)

            stack = callStack(stack, "", n)
            display(stack)

            return fibVal
    except TypeError:
        print("input must be a number")


# Method
def _fibIterative(n):
    fibVal = 0
    currVal = 1
    lastVal = 0

    if n == 0:
        fibVal = 0
    elif n == 1:
        fibVal = 1
    else:
        for i in range(2, n):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal

    return fibVal

def __main__():
    try:
        stack = cl.DSAStack()
        stack.printStack()
        nUser = int(input("\nEnter a numer for the fibonacci functions: "))
        print("The recursive fibonacci function gives a value of: ",fibRecursive(nUser, stack))
        print("The iterative fibonacci function gives a value of: ",fibIterative(nUser, stack))
        nUser = int(input("\nEnter a numer for the factorial functions: "))
        print("The recursive factorial function gives a value of: ",factRecursive(nUser, stack))
        print("The iterative factorial function gives a value of: ",factIterative(nUser, stack))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    __main__()

