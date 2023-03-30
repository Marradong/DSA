import classes as cl


def display(stack):
    print("\n-----Call Stack-----")
    for i in range(stack._count):
        print(stack._stack[i])
    print("-----End  Stack-----")


def callStack(stack, function, args):
    if function != "":
        stack.push(str(function)+"("+str(args)+")")
    else: 
        stack.pop()
    return stack


###################################
# Recursive and Iterative Methods #
###################################


# Wrapper
def fibRecursive(n, stack):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            fibVal = _fibRecursive(n, stack)
            return fibVal
    except TypeError:
        print("input must be a number")


# Method
def _fibRecursive(n, stack):
    stack = callStack(stack, "fibRecursive", n)
    display(stack)
    fibVal = 0
    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = fibRecursive(n-1, stack) + fibRecursive(n-2, stack)
    stack = callStack(stack, "", n)
    display(stack)
    return fibVal

# Wrapper
def factRecursive(n, stack):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            factVal = _factRecursive(n, stack)
            return factVal
    except TypeError:
        print("input must be a number")


# Method
# max 499
def _factRecursive(n, stack):
    stack = callStack(stack, "factRecursive", n)
    display(stack)
    if (n == 0):
        val = 1
    else:
        val = n * factRecursive((n-1), stack)
    stack = callStack(stack, "", n)
    display(stack)
    return val
    

# Wrapper
def factIterative(n, stack):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            factVal = _factIterative(n, stack)
            return factVal
    except TypeError:
        print("input must be a number")


# Method
def _factIterative(n, stack):
    stack = callStack(stack, "factIterative", n)
    display(stack)
    nFactorial = 1
    for i in range(n, 1, -1):
        nFactorial = nFactorial * i
    stack = callStack(stack, "", n)
    display(stack)
    return nFactorial
    

# Wrapper
def fibIterative(n, stack):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            fibVal = _fibIterative(n, stack)
            return fibVal
    except TypeError:
        print("input must be a number")


# Method
def _fibIterative(n, stack):
    stack = callStack(stack, "fibIterative", n)
    display(stack)
    fibVal = 0
    currVal = 1
    lastVal = 0

    if n == 0:
        fibVal = 0
    elif n == 1:
        fibVal = 1
    else:
        for i in range(2, n+1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    stack = callStack(stack, "", n)
    display(stack)
    return fibVal
