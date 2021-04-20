def dfs(idx, percent):
    global max_percent
    if idx == N:
        max_percent = max(max_percent, percent)
        return
    if percent <= max_percent:
        return
    for i in range(N):
        if not check[i]:
            check[i] = 1
            dfs(idx+1, percent*arr[idx][i]/100)
            check[i] = 0

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    max_percent = 0
    dfs(0, 1)
    print(f'#{test}', '%.6f' % (max_percent*100))