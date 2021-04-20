def dfs(idx, start, distance):
    global min_dis
    if idx == N:
        distance += abs(start[0] - home[0]) + abs(start[1] - home[1])
        min_dis = min(distance, min_dis)
        return

    if distance >= min_dis:
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            new_dis = distance + abs(start[0] - customer[i][0]) + abs(start[1] - customer[i][1])
            dfs(idx+1, customer[i], new_dis)
            visit[i] = 0

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = (arr[0], arr[1])
    home = (arr[2], arr[3])
    customer = []
    visit = [0] * N
    for i in range(N):
        customer.append((arr[2*i+4], arr[2*i+1+4]))
    min_dis = 9999999999999
    dfs(0, company, 0)
    print(f'#{test}', min_dis)