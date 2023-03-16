#**
#** Testharness to test recursive and iterative functions
#**

import recursiveIterativeFunctions as rif

#########################################################
print("test factorial functions")

print("\nChecking integer input: factRecursive(\"a\")")
rif.factRecursive("a")

print("\nChecking integer input: factIterative(\"a\")")
rif.factIterative("a")

print("\nChecking negative input: factRecursive(-1)")
rif.factRecursive(-1)

print("\nChecking negative input: factIterative(-1)")
rif.factIterative(-1)

print("\nChecking result: factRecursive(10)")
print(rif.factRecursive(10))

print("\nChecking result: factIterative(10)")
print(rif.factIterative(10))

#########################################################
print("test fibonacci functions")

print("\nChecking integer input: fibRecursive(\"a\")")
rif.fibRecursive("a")

print("\nChecking integer input: fibIterative(\"a\")")
rif.fibIterative("a")

print("\nChecking negative input: fibRecursive(-1)")
rif.fibRecursive(-1)

print("\nChecking negative input: fibIterative(-1)")
rif.factIterative(-1)

print("\nChecking result: fibRecursive(10)")
print(rif.fibRecursive(10))

print("\nChecking result: fibIterative(10)")
print(rif.factIterative(10))

#########################################################
print("test GCD function")

print("\nChecking integer input: gcdRecursive(\"a\", \"b\")")
rif.gcdRecursive("a", "b")

print("\nChecking negative input: gcdRecursive(-1, -10)")
rif.gcdRecursive(-1, -10)

print("\nChecking result: gcdRecursive(12,8)")
print(rif.gcdRecursive(12,8))

#########################################################
print("test base function")

print("\nChecking integer input: base10ToAny(\"a\", \"b\")")
rif.base10ToAny("a", "b")

print("\nChecking negative input: base10ToAny(-11, -8)")
rif.base10ToAny(-11, -8)

print("\nChecking result: base10ToAny(10,2)")
print(rif.base10ToAny(10,2))

#########################################################
print("test towers function")

print("\nChecking integer input: towersOfHanoi(\"a\", \"b\", \"c\")")
rif.towersOfHanoi("a", "b", "c")

print("\nChecking negative input: towersOfHanoi(-3, -1, -3)")
rif.towersOfHanoi(-3, -1, -3)

print("\nChecking result: towersOfHanoi(3, 1, 3)")
print(rif.towersOfHanoi(3, 1, 3))