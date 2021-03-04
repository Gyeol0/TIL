from _collections import deque
def bfs(N, arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 창고를 저장할 리스트
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                # 왼쪽 위 꼭짓점
                start = (i, j)
                queue = deque()
                queue.append(start)
                arr[start[0]][start[1]] = 0
                # 탐색
                while queue:
                    x, y = queue.popleft()
                    # 네 방향 탐색
                    for k in range(4):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        # 범위 내
                        if 0 <= ax < N and 0 <= ay < N:
                            # 갈 수 있는지
                            if arr[ax][ay] != 0:
                                # 방문
                                arr[ax][ay] = 0
                                # 큐 삽입
                                queue.append((ax, ay))

                # 다 돌면 오른쪽 아래 꼭짓점 도착
                end = (x, y)
                result.append([end[0] - start[0] + 1, end[1] - start[1] + 1])
    result = sorted(result, key = lambda x: (x[0]*x[1], x[0]))
    return result
T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = bfs(N, arr)
    print(f'#{test}', len(result), end = ' ')
    for i in result:
        print(i[0], i[1], end = ' ')
    print()