from collections import deque
def square(N, arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_count = 0
    result = -1
    # 모든 점에서 출발
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                continue
            queue = deque()
            queue.append((i, j, arr[i][j], arr[i][j], 1))
            visit[i][j] = 1
            while queue:
                # 위치, 현재 값, 출발한 방 번호, count
                x, y, value, number, count = queue.popleft()
                if max_count < count:
                    result = number
                    max_count = count

                elif max_count == count:
                    if result > number:
                        result = number
                # bfs 상하좌우 이동
                for k in range(4):
                    ax = x + dx[k]
                    ay = y + dy[k]
                    if 0 <= ax < N and 0 <= ay < N:
                        if arr[ax][ay] - 1 == value:
                            queue.append((ax, ay, value + 1, number, count + 1))

    return max_count, result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count, result = square(N, arr)
    print(f'#{test}', result, max_count)

def square2(N, arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [0] * (N**2+1)
    # arr[i][j]에서 이동할 수 있는 방이 있는지 V 배열 만들기
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ax = i + dx[k]
                ay = j + dy[k]
                if 0 <= ax < N and 0 <= ay < N:
                    if arr[ax][ay] - 1 == arr[i][j]:
                        visit[arr[i][j]] = 1
                        break
    # 연속한 1의 개수 최댓값찾기
    max_count = 0
    count = 1
    result = -1
    for i in range(N**2+1):
        if visit[i] == 1:
            count += 1
        elif visit[i] == 0:
            if max_count < count:
                max_count = count
                result = i - count + 1
            count = 1
    return max_count, result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count, result = square2(N, arr)
    print(f'#{test}', result, max_count)


