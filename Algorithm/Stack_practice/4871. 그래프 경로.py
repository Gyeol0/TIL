def Graph_Route(graph, start, end):
    visit = []
    stack = [start]
    while stack:
        s = stack.pop()
        # 경로중 end를 만나면 종료
        if s == end:
            return 1
        # 방문하지 않았고 갈 수 있으면 stack에 추가
        if s not in visit and s in graph:
            visit.append(s)
            stack += graph[s]
    return 0

T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for i in range(E):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
    start, end = map(int, input().split())
    print(f'#{test}',Graph_Route(graph, start, end))