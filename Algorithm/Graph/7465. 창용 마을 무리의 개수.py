def dfs(node):
    visit[node] = 1
    if graph[node]:
        for k in graph[node]:
            if visit[k] == 0:
                dfs(k)

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    visit = [0] * (N+1)
    count = 0
    for i in range(1, N+1):
        if visit[i] == 0:
            count += 1
            dfs(i)
    print(f'#{test}', count)