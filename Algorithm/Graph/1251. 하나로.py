def find(node):
    if p[node] != node:
        p[node] = find(p[node])
    return p[node]

def make_set(node):
    p[node] = node
    rank[node] = 0


def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if rank[root1] > rank[root2]:
        p[root2] = root1
    else:
        p[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal():
    mst = []
    for node in vertices:
        make_set(node)
    edge_sort = sorted(edge, key=lambda x: x[2])
    for e in edge_sort:
        node1, node2, weight = e
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(e)
    return mst
T = int(input())
for test in range(1, T+1):
    p = dict()
    rank = dict()
    N = int(input())
    vertices = [i for i in range(N)]
    edge = []
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    for i in range(N):
        for j in range(i+1, N):
            dis = ((x[i] - x[j])**2 + (y[i] - y[j])**2) * E
            edge.append((i, j, dis))
    mst = kruskal()
    result = 0
    for route in mst:
        result += route[2]
    print(f'#{test}', round(result))

# 프림
def prim(graph, start):
    INF = 9999999999999
    key = [INF] * N
    visited = [0] * N
    key[start] = 0
    count = 0
    result = 0

    while count < N:
        minimum = INF
        now = 0
        for i in range(N):  # 방문 안한 곳 최소 가중치
            if not visited[i] and key[i] < minimum:
                minimum = key[i]
                now = i     # 선택 정점
        # 방문 처리
        visited[now] = 1
        result += minimum      # 결과값
        count += 1  # 탐색 정점 개수

        for w in range(N):  # 인접한 정점
            if not visited[w] and key[w] > graph[now][w]:
                key[w] = graph[now][w]  # 방문 안한 곳들 중에서 가중치가 더 작으면 갱신

    return result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    graph = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            dis = ((x[i] - x[j])**2 + (y[i] - y[j])**2) * E
            graph[i][j] = dis
            graph[j][i] = dis
    result = prim(graph, 0)
    print(f'#{test}', round(result))