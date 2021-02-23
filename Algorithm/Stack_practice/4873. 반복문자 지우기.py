def Del_Repeat(arr):
    stack = []
    for i in arr:
        # 스택에 원소가 있고, top과 반복 문자인지 비교
        if stack:
            if stack[-1] != i:
                # 반복문자가 아니면 스택에 추가
                stack.append(i)
            else:
                stack.pop()
        else:
            stack.append(i)
    return len(stack)

T = int(input())
for test in range(1, T+1):
    arr = input()
    print(f'#{test}', Del_Repeat(arr))