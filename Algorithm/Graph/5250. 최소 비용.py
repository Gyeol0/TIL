import heapq
def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 힙 푸시
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기(힙)
        dist, now = heapq.heappop(q)
        # 바로 가는게 더 빠르면 continue
        if distance[now] < dist:
            continue
        # 현재 노드(now)와 연결된 노드
        for node, cost in graph[now]:
            # 지금 i를 거쳐서 가는게 더 짧으면 distance 갱신하고 큐에 삽입
            if dist + cost < distance[node]:
                distance[node] = dist + cost
                heapq.heappush(q, (dist+cost, node))


T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    graph = [[] for _ in range(N**2)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N**2):
        x = i // N
        y = i % N
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if 0 <= ax < N and 0 <= ay < N:
                if arr[ax][ay] > arr[x][y]:
                    cost = arr[ax][ay] - arr[x][y] + 1
                else:
                    cost = 1
                node2 = ax * N + ay
                graph[i].append((node2, cost))
    INF = int(1e9)
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (N**2)
    dijkstra(0)
    print(f'#{test}', distance[N**2-1])

# dfs는 시간 초과
def dfs(x, y, cost):
    global min_cost
    if cost >= min_cost:
        return

    if x == N-1 and y == N-1:
        min_cost = min(cost, min_cost)
        return

    for k in range(4):
        ax = x + dx[k]
        ay = y + dy[k]
        if 0 <= ax < N and 0 <= ay < N:
            if visit[ax][ay] == 0:
                if arr[ax][ay] > arr[x][y]:
                    new_cost = cost + arr[ax][ay] - arr[x][y] + 1
                else:
                    new_cost = cost + 1
                visit[ax][ay] = 1
                dfs(ax, ay, new_cost)
                visit[ax][ay] = 0

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    min_cost = 9999999
    visit[0][0] = 1
    dfs(0, 0, 0)
    print(f'#{test}', min_cost)

# bfs 가능
from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if 0 <= ax < N and 0 <= ay < N:
                if arr[ax][ay] > arr[x][y]:
                    new_cost = visit[x][y] + arr[ax][ay] - arr[x][y] + 1
                else:
                    new_cost = visit[x][y] + 1
                if new_cost < visit[ax][ay]:
                    visit[ax][ay] = new_cost
                    queue.append((ax, ay))
    return visit[N-1][N-1]

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[999999] * N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit[0][0] = 0
    print(f'#{test}', bfs(0, 0))