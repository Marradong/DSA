import classes as cl


# Wrapper
def fibIterative(n, stack):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            return _fibIterative(n, stack)
    except TypeError:
        print("input must be a number")


# Method
def _fibIterative(n, stack):
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


# Wrapper
def fibRecursive(n, stack):
    try:
        if n < 0:
            print("Number must be positive!")
        else:
            return _fibRecursive(n, stack)
    except TypeError:
        print("input must be a number")


# Method
def _fibRecursive(n, stack):
    fibVal = 0
    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = fibRecursive(n-1) + fibRecursive(n-2)
    return fibVal
