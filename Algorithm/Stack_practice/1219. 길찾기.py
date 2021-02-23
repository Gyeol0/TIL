def dfs(graph):
    visit = []
    stack = [0]
    while stack:
        s = stack.pop()
        # 경로중 end를 만나면 종료
        if s == 99:
            return 1
        # 방문하지 않았고 갈 수 있으면 stack에 추가
        if s not in visit and s in graph:
            visit.append(s)
            stack += graph[s]
    return 0

for _ in range(10):
    test, N = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = {}
    for i in range(0, N*2, 2):
        if arr[i] not in graph:
            graph[arr[i]] = [arr[i+1]]
        else:
            graph[arr[i]].append(arr[i+1])
    print(f'#{test}', dfs(graph))