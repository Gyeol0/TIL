def Bread(M, K, time):
    count = 0
    # 먼저 온 사람 순으로
    time.sort()
    final = 0
    for i in time:
        # 현재까지 만든 붕어빵 개수
        count += (i - final) // M * K
        # 마지막으로 붕어빵 만든 시간
        final += (i - final) // M * M
        if count > 0:
            count -= 1
        else:
            return 'Impossible'
    return 'Possible'

T = int(input())
for test in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    print(f'#{test}', Bread(M, K, time))