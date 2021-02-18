def Sum_Subset2(N, k, c):
    result = 0
    arr = [i for i in range(1, c+1)]
    subset = [[]]
    for i in arr:
        l = len(subset)
        # 원래 있는 모든 집합에 요소로 추가로 더한 것을 append, 원래 있던 집합은 건들지 않는다.
        for j in range(l):
            subset.append(subset[j]+[i])
            if len(subset[-1]) == N and sum(subset[-1]) == k:
                result += 1
    return result

T = int(input())
for test in range(1, T+1):
    N, k = map(int, input().split())
    print(f'#{test}', Sum_Subset2(N,k,12))