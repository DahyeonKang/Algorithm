from stackclass import Stack

def precedence(op):
    if op == '(' or  op == ')': return 0
    elif op == '+' or op == '-': return 1
    elif op == '*' or op == '/': return 2
    else: return -1


def infix2postfix(expr):
    s = Stack()
    output = []

    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(': break
                else: output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output


def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if token == '+': s.push(val1 + val2)
            elif token == '-': s.push(val1 - val2)
            elif token == '*': s.push(val1 * val2)
            elif token == '/': s.push(val1 / val2)
        else:
            s.push(float(token))
    return s.pop()


infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']

postfix1 = infix2postfix(infix1)
postfix2 = infix2postfix(infix2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)

print('중위표기: ', infix1)
print('후위표기: ', postfix1)
print('중위표기: ', result1, end='\n\n')
print('중위표기: ', infix2)
print('중위표기: ', postfix2)
print('중위표기: ', result2)