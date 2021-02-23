def Pascal(N):
    arr = [[0]*(N+1) for _ in range(N)]
    arr[0][1] = 1
    for i in range(1, N):
        for j in range(1, i+2):
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    return arr

T = int(input())
for test in range(1, T+1):
    N = int(input())
    result = Pascal(N)
    print(f'#{test}')
    for i in range(N):
        print(*result[i][1:i+2])