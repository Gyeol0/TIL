def catch_fly(N, M, arr):
    # 초기화
    max_fly = 0
    # 시작점
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_sum = 0
            # 한 변이 M인 정사각형 안에 들어가는 파리 합
            for p in range(i, i+M):
                for q in range(j, j+M):
                    fly_sum += arr[p][q]
            if max_fly < fly_sum:
                max_fly = fly_sum
    return max_fly

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(f'#{test}', catch_fly(N, M, arr))
