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
    # 초기화
    for node in vertices:
        make_set(node)
    # 가중치 기준으로 정렬
    edge_sort = sorted(edge, key=lambda x: x[2])
    for e in edge_sort:
        node1, node2, weight = e
        # 대표 원소가 다른지 확인, 같으면 사이클
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(e)
    return mst
T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    vertices = [i for i in range(V+1)]
    p = dict()
    rank = dict()
    mst = kruskal()
    result = 0
    for node in mst:
        result += node[2]
    print(f'#{test}', result)