def Sum_Subset2(N, k, c):
    result = 0
    arr = [i for i in range(1, c+1)]
    for i in range(1<<c):
        sum_subset = 0
        subset = []
        count = 0
        for j in range(c):
            if i & (1 << j):
                subset.append(arr[j])
                count += 1
                if count > N:
                    break
        if count == N:
            for p in subset:
                sum_subset += p
            if sum_subset == k:
                result += 1
    if result:
        return result
    else:
        return 0

T = int(input())
for test in range(1, T+1):
    N, k = map(int, input().split())
    print(f'#{test}', Sum_Subset2(N,k,12))