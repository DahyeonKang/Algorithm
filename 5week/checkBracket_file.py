from stackclass import Stack


def checkBracketsV2(lines):
    stack = Stack()
    for line in lines:
        for ch in line:
            if ch in ('{', '{', '('):
                stack.push(ch)
            elif ch in ('}', '}', ')'):
                if stack.isEmpty():
                    return False
                else:
                    left = stack.pop()
                    if (ch == '}' and left != '{') or \
                       (ch == ']' and left != '[') or \
                       (ch == ')' and left != '('):
                        return False

    return stack.isEmpty()


filename = 'ArrayStack.h'
infile = open(filename, 'r')
lines = infile.readlines()
infile.close()

result = checkBracketsV2(lines)
print(filename, " ---> ", result)