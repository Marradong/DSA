import classes as cl


def solve(equation):
    postfixQueue = _parseInfixToPostfix(equation)
    print("Postfix:")
    postfixQueue.printQueue()
    print("Result:")
    print(_evaluatePostfix(postfixQueue))


def _parseInfixToPostfix(equation):
    infix = equation.split()
    postfix = cl.DSAQueue(len(infix))
    opStack = cl.DSAStack(len(infix))

    while len(infix) != 0:
        term, infix = _parseNextTerm(infix)
        if term == "(":
            opStack.push('(')
        elif term == ")":
            while opStack.top() != "(":
                postfix.enqueue(opStack.pop())
            opStack.pop()
        elif term == "+" or term == "-" or term == "*" or term == "/":
            while (not opStack.isEmpty()) and (opStack.top() != '(') and (_precedenceOf(opStack.top()) >= _precedenceOf(term)):
                print(opStack.getCount())
                postfix.enqueue(opStack.pop())
            opStack.push(term)
        else:
            postfix.enqueue(term)
        print("\n",infix)
        opStack.printStack()
        postfix.printQueue()
    while not opStack.isEmpty():
        postfix.enqueue(opStack.pop())
    return postfix

def _evaluatePostfix(postfixQueue):
    operands = cl.DSAStack(postfixQueue.getCount())
    operators = ["+", "-", "*", "/",]
    while not postfixQueue.isEmpty():
        item = postfixQueue.dequeue()
        if item not in operators:
            operands.push(item)
            #print(item)
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            result = _executeOperation(item, float(op1), float(op2))
            print(op1, item, op2, "=", result)
            operands.push(result)
    return operands.pop()
    

def _precedenceOf(theOp):
    precedence = 0
    if theOp == "+" or theOp == "-":
        precedence = 1
    elif theOp == "*" or theOp == "/":
        precedence = 2
    return precedence


def _executeOperation(op, op1, op2):
    if op == "+":
        result = op1 + op2
    elif op == "-":
        result = op1 - op2
    elif op == "*":
        result = op1 * op2
    elif op == "/":
        result = op1 / op2
    return result


def _parseNextTerm(equation):
    nextTerm = equation[0]
    equation = equation[1:]
    return nextTerm, equation
