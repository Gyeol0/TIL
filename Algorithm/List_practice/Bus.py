def Bus(n, m, k, arr):
    count = 0 # 충전 횟수
    current = 0 # 이전에 충전한 정류소
    arr += [n]
    # 충전기가 있는 정류장을 돌면서 최대치 확인
    for i in range(m):
        # 정류장 간의 거리가 k이상이면 0 반환(불가능)
        if arr[i+1] - arr[i] > k:
            return 0
        # 이전에 충전한 정류소에서 최대한 갈 수 있는 정류소
        if current + k < arr[i+1]:
            current = arr[i]
            count += 1
    return count

T = int(input())
for test in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    print(f'#{test}', Bus(N, M, K, station))
