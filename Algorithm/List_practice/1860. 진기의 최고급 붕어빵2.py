def Bread(M, K, time):
    # 정렬 없이 풀어보기
    # 시간별로 만드는 붕어빵 최대 리스트
    bread = [K] * (11111 // M + 1)
    # 0 타임에는 없음
    bread[0] = 0
    for i in time:
        # 가장 나중에(최근)에 만든 붕어빵을 준다.
        for j in range(i//M, -1, -1):
            if bread[j] > 0:
                bread[j] -= 1
                break
            # 마지막까지 붕어빵이 없으면 불가능
            if j == 0:
                return 'Impossible'
    return 'Possible'

T = int(input())
for test in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    print(f'#{test}', Bread(M, K, time))