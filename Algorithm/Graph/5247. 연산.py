from collections import deque
def bfs(N, M):
    queue = deque()
    queue.append((N, 0))
    visit = [0] * 1000001
    visit[N] = 1
    while queue:
        x, count = queue.popleft()
        if x == M:
            return count
        if 0 < x+1 <= 1000000 and visit[x+1] == 0:
            queue.append((x + 1, count+1))
            visit[x+1] = 1
        if 0 < x-1 <= 1000000 and visit[x-1] == 0:
            queue.append((x - 1, count + 1))
            visit[x-1] = 1
        if 0 < x*2 <= 1000000 and visit[x*2] == 0:
            queue.append((x * 2, count + 1))
            visit[x*2] = 1
        if 0 < x-10 <= 1000000 and visit[x-10] == 0:
            queue.append((x - 10, count + 1))
            visit[x-10] = 1

T = int(input())

for test in range(1, T+1):
    N, M = map(int ,input().split())
    print(f'#{test}', bfs(N, M))