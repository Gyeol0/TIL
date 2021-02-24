def Postfix_Notation(expression): # 후위 표기법
    stack = []
    result = []
    priority = {
        '+': 1,
        '*': 2
    }
    for i in expression:
        # 피연산자는 push
        if i not in priority:
            result.append(int(i))
        else:   # 연산자
            # 스택이 있을 때
            if stack:
                while stack:
                    if priority[stack[-1]] < priority[i]:
                        stack.append(i)
                        break
                    else:
                        result.append(stack.pop())
                # 스택 비어지면 push
                if not stack:
                    stack.append(i)
            else:   # 스택이 비었을 때
                stack.append(i)
    # 스택에 남아있을 때 모두 pop
    while stack:
        result.append(stack.pop())
    return result

def calculator(expression):
    stack = []
    symbol = ['+', '*']
    for i in expression:
        # 피연산자는 스택에 push
        if i not in symbol:
            stack.append(i)
        else:
            # 연산자는 뒤에서부터 2개 계산해서 push
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(b + a)
            elif i == '*':
                stack.append(b * a)
    result = stack.pop()
    return result

for test in range(1, 11):
    N = int(input())
    exp = input()
    print(f'#{test}', calculator(Postfix_Notation(exp)))