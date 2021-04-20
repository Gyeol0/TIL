# 부모 목록 찾기
def parent(node, pa):
    result = []
    while pa[node]:
        result.append(pa[node])
        node = pa[node]
    return result

def min_parent(result, node):
    while pa[node]:
        if pa[node] in result:
            return pa[node]
        node = pa[node]

def subTree(node):
    count = 1
    stack = []
    stack.append(node)
    while stack:
        node = stack.pop(0)
        if tree[node][0]:
            stack.append(tree[node][0])
            count += 1
        if tree[node][1]:
            stack.append(tree[node][1])
            count += 1

    return count

T = int(input())
for test in range(1, T+1):
    V, E, A, B = map(int, input().split())
    tree = [[0]*2 for _ in range(V+1)]
    pa = [0]*(V+1)
    arr = list(map(int, input().split()))
    for i in range(E):
        p, q = arr[i*2], arr[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = q
        else:
            tree[p][1] = q
        pa[q] = p
    result = parent(A, pa)
    min_node = min_parent(result, B)
    count = subTree(min_node)
    print(f'#{test}', min_node, count)