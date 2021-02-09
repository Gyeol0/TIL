def prefix_sum(n, m, arr):
    # 구간 합 최소, 최대 초기화
    PrefixMin = 1000000
    PrefixMax = -1000000
    # 출발지점
    for i in range(n-m+1):
        PrefixSum = 0
        # 구간합
        for j in range(m):
            PrefixSum += arr[i+j]
        if PrefixMax < PrefixSum:
            PrefixMax = PrefixSum
        if PrefixMin > PrefixSum:
            PrefixMin = PrefixSum
    return PrefixMax - PrefixMin

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(f'#{test}', prefix_sum(N, M, numbers))
