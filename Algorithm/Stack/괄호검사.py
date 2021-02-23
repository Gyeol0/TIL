def Parentheses(arr):
    stack = []
    for i in arr:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            s = stack.pop()
            if i == ')':
                if s != '(':
                    return False
            elif i == '}':
                if s != '{':
                    return False
            elif i == ']':
                if s != ']':
                    return False
    if stack:
        return False
    else:
        return True
print(Parentheses('((({})))'))