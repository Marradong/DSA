############################################################################
#
# recursive functions


# Wrapper
def factRecursive(n):
    if n < 0:
        raise Exception("Number must be positive!")
    else:
        return _factRecursive(n)


# Method
# max 499
def _factRecursive(n):
    if (n == 0):
        return 1
    else:
        return n * factRecursive(n-1)


# Wrapper
def fibRecursive(n):
    if n < 0:
        raise Exception("Number must be positive!")
    else:
        return _fibRecursive(n)


# Method
def _fibRecursive(n):
    fibVal = 0
    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = fibRecursive(n-1) + fibRecursive(n-2)
    return fibVal


# greatest common denominator function
# taken from https://www.geeksforgeeks.org/gcd-in-python/

# Wrapper
def gcdRecursive(n, m):
    if (n < 0) or (m < 0):
        raise Exception("Numbers must be positive!")
    else:
        return _gcdRecursive(n)


# Method
def _gcdRecursive(n, m):
    if m == 0:
        gcd = n
    else:
        gcd = gcdRecursive(m, n % m)
    return gcd


# Wrapper
def base10ToAny(decimalNum, base):
    if (decimalNum < 0):
        raise Exception("Number must be positive!")
    elif (base < 2) or (base > 16):
        raise Exception("Base must be between 2 and 16!")
    else:
        return _base10ToAny(decimalNum)


# Method
def _base10ToAny(decimalNum, base):
    if(decimalNum < base):
        newNum = str(decimalNum)
    else:
        newNum = str(base10ToAny(decimalNum // base, base)) + str(decimalNum % base)
    return int(newNum)


def moveDisk(n, src, dest, recLevel):
    print(recLevel*"\t", "Recursion Level = ", recLevel)
    print(recLevel*"\t", "Moving Disk ", str(n), " from peg ", str(src), " to peg ", str(dest))
    print(recLevel*"\t", "n =", str(n), " src =", str(src), " dest =", str(dest))
    print()


def towersOfHanoi(n, src, dest, recLevel=1):
    if (n == 1):
        moveDisk(n, src, dest, recLevel)
    else:
        temp = 6 - src - dest
        towersOfHanoi(n-1, src, temp, (recLevel+1))
        moveDisk(n, src, dest, recLevel)
        towersOfHanoi(n-1, temp, dest, (recLevel+1))


############################################################################
#
# iterative facctorial & fibonacci functions


# Wrapper
def factIterative(n):
    if n < 0:
        raise Exception("Number must be positive!")
    else:
        return _factIterative(n)


# Method
def _factIterative(n):
    nFactorial = 1
    for i in range(n, 1, -1):
        nFactorial = nFactorial * i
    return nFactorial


# Wrapper
def fibIterative(n):
    if n < 0:
        raise Exception("Number must be positive!")
    else:
        return _fibIterative(n)


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
