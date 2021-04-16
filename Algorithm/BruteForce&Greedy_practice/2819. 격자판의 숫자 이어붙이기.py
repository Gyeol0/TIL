from collections import deque
def bfs(arr):
    result = set()
    dx = [1, -1, 0 , 0]
    dy = [0 , 0, -1, 1]
    queue = deque()
    # 모든 점에서 시작
    for i in range(4):
        for j in range(4):
            # 위치, 현재 값, count
            queue.append((i, j, arr[i][j], 1))
            while queue:
                x, y, num, count = queue.popleft()
                # 7개 이어 붙이면 그만
                if count == 7:
                    result.add(num)
                    continue
                # bfs 상하좌우 이동
                for k in range(4):
                    ax = x + dx[k]
                    ay = y + dy[k]
                    if 0 <= ax < 4 and 0 <= ay < 4:
                        queue.append((ax, ay, num + arr[ax][ay], count + 1))

    return len(result)

T = int(input())
for test in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    print(f'#{test}', bfs(arr))