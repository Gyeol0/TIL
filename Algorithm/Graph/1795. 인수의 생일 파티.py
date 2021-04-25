import heapq
def dijkstra(start, graph):
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, cost in graph[now]:
            if dist + cost < distance[node]:
                distance[node] = dist + cost
                heapq.heappush(q, (dist+cost, node))
    return distance

T = int(input())
for test in range(1, T+1):
    N, M, X = map(int, input().split())
    graph1 = [[] for _ in range(N+1)]
    graph2 = [[] for _ in range(N+1)]
    INF = int(1e9)

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph1[x].append((y, c))
        graph2[y].append((x, c))
    max_result = 0
    distance1 = dijkstra(X, graph1)     # X에서 나가는
    distance2 = dijkstra(X, graph2)     # X로 들어오는
    for i in range(1, N+1):
        if i != X:
            max_result = max(max_result, distance1[i] + distance2[i])
    print(f'#{test}', max_result)