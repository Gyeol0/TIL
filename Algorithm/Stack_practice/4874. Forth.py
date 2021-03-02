def Forth(cal):
    stack = []
    for i in cal:
        # 앞에 숫자가 2개 이상인지 확인
        # 없으면 error 반환
        if i == '+':
            try:
                a = stack.pop()
                stack[-1] = stack[-1] + a
            except:
                return 'error'
        elif i == '-':
            try:
                a = stack.pop()
                stack[-1] = stack[-1] - a
            except:
                return 'error'
        elif i == '*':
            try:
                a = stack.pop()
                stack[-1] = stack[-1] * a
            except:
                return 'error'
        elif i == '/':
            try:
                a = stack.pop()
                stack[-1] = stack[-1] // a
            except:
                return 'error'
        # 연산이 끝났을 때 하나 남는지 확인
        elif i == '.':
            if len(stack) == 1:
                return stack[-1]
            else:
                return 'error'
        # 숫자는 stack에 넣는다.
        else:
            stack.append(int(i))

T = int(input())
for test in range(1, T+1):
    cal = input().split()
    print(f'#{test}', Forth(cal))