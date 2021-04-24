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
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    INF = int(1e9)
    distance = [INF] * (N ** 2)
    for _ in range(E):
        node1, node2, cost = map(int, input().split())
        graph[node1].append((node2, cost))
    dijkstra(0)
    print(f'#{test}', distance[N])