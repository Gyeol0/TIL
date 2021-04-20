def dfs(idx, cost):
    global min_cost

    if cost >= min_cost:
        return
    if idx == N:
        min_cost = min(cost, min_cost)
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            dfs(idx + 1, cost + arr[idx][i])
            visit[i] = 0

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    min_cost = 9999999999
    dfs(0, 0)
    print(f'#{test}', min_cost)