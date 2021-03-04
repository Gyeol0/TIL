from collections import deque
def Node_Dis(graph, start, end):
    queue = deque()
    # 큐에 출발점 삽입
    queue.append((start, 0))
    visit = []
    while queue:
        # pop
        node, count = queue.popleft()
        # 도착하면 간선 개수 반환
        if node == end:
            return count
        # 방문한 곳이 아니면
        if node not in visit:
            # 방문
            visit.append(node)
            # 이어진 노드 모두 큐에 삽입
            for i in graph[node]:
                queue.append((i, count + 1))
    # 도착하지 못하면 0 반환
    return 0

T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        # 그래프 생성
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    start, end = map(int, input().split())
    print(f'#{test}', Node_Dis(graph, start, end))