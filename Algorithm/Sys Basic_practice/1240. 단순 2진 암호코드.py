def password(N, M, arr):
    flag = False
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                start = (i, j)
                flag = True
                break
        if flag:
            break
    s = arr[start[0]][start[1]-55:start[1] + 1]
    code = []
    result = 0
    for i in range(1, 9):
        word = s[(i-1)*7:i*7]
        if word == '0001101':
            code.append(0)
        elif word == '0011001':
            code.append(1)
        elif word == '0010011':
            code.append(2)
        elif word == '0111101':
            code.append(3)
        elif word == '0100011':
            code.append(4)
        elif word == '0110001':
            code.append(5)
        elif word == '0101111':
            code.append(6)
        elif word == '0111011':
            code.append(7)
        elif word == '0110111':
            code.append(8)
        elif word == '0001011':
            code.append(9)
    for i in range(8):
        if i % 2:
            result += code[i]
        else:
            result += code[i] * 3
    if result % 10:
        return 0
    else:
        return sum(code)

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f'#{test}', password(N, M, arr))