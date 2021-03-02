def Postfix_Notation(expression): # 후위 표기법
    stack = []
    result = []
    priority_in = {
        '(': 0,
        '+': 1,
        '*': 2,
        ')': '-'
    }
    priority_out = {
        '(': 3,
        '+': 1,
        '*': 2,
        ')': '-'
    }

    for i in expression:
        # 피연산자는 push
        if i not in priority_in:
            result.append(int(i))
        else:   # 연산자
            # 스택이 있을 때
            if stack:
                # 닫는 괄호면 여는 괄호가 나올 때까지 pop
                if i == ')':
                    while stack[-1] != '(':
                        result.append(stack.pop())
                    stack.pop()
                else:
                    # top보다 우선순위가 클 때까지 pop
                    while stack:
                        if priority_in[stack[-1]] < priority_out[i]:
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
            if i == '+':
                stack[-1] = stack[-1] + a
            elif i == '*':
                stack[-1] = stack[-1] * a
    result = stack.pop()
    return result

for test in range(1, 11):
    N = int(input())
    ex = input()
    postfix = Postfix_Notation(ex)
    result = calculator(postfix)
    print(f'#{test}', result)