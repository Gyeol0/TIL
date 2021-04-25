from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if 0 <= ax < N and 0 <= ay < N:
                if visit[ax][ay] > visit[x][y] + arr[ax][ay]:
                    queue.append((ax, ay))
                    visit[ax][ay] = visit[x][y] + arr[ax][ay]

    return visit[N-1][N-1]

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [[9999999] * N for _ in range(N)]
    print(f'#{test}', bfs(0, 0))