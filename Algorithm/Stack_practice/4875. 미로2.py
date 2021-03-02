def DFS(x, y, arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = [[x, y]]
    while stack:
        x, y = stack.pop()
        # 도착하면 1
        if arr[x][y] == '3':
            return 1
        # 아니면 방문
        else:
            arr[x][y] = '1'
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            # 벽이나 방문 한 곳이 아닐 때
            if 0 <= ax < N and 0 <= ay < N and arr[ax][ay] != '1':
                stack.append([ax, ay])
    return 0

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 출발지에서 dfs 시작
            if arr[i][j] == '2':
                print(f'#{test}', DFS(i, j, arr))