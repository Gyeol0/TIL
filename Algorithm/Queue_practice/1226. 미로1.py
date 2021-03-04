from _collections import deque
def bfs(arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                # 출발점 찾기
                start = (i, j, 0)
                queue = deque()
                queue.append(start)
                arr[start[0]][start[1]] = '1'
                # 탐색
                while queue:
                    x, y, count = queue.popleft()
                    # 네 방향 탐색
                    for k in range(4):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        # 범위 내
                        if 0 <= ax < 16 and 0 <= ay < 16:
                            # 갈 수 있는지
                            if arr[ax][ay] == '0':
                                # 방문
                                arr[ax][ay] = '1'
                                # 큐 삽입
                                queue.append((ax, ay, count + 1))
                            # 도착
                            elif arr[ax][ay] == '3':
                                return 1
                # 경로 못찾음
                return 0


for test in range(10):
    test = int(input())
    arr = [list(input()) for _ in range(16)]
    print(f'#{test}', bfs(arr))