def Parentheses(arr):
    stack = []
    P = {'(': ')', '{': '}', '[': ']'}
    for i in arr:
        # 여는 괄호인지 확인, 괄호면 스택에 추가
        if i in P:
            stack.append(i)
        # 닫는 괄호인지 확인, top과 비교
        elif i in P.values():
            if stack:
                s = stack.pop()
                if P[s] != i:
                    return 0
            else:
                return 0
    if stack:
        return 0
    else:
        return 1

T = int(input())
for test in range(1, T+1):
    arr = input()
    print(f'#{test}', Parentheses(arr))
