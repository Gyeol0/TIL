def flag(N, M, arr):
    # 브루트 포스?
    min_count = 2500
    # 흰줄 열번호 i번까지 흰줄
    for i in range(0, N-2):
        # 파란줄 열번호, i +1부터 j까지 파란줄, 나머지 빨간줄
        for j in range(i+1, N-1):
            count = 0
            # 흰줄에서 흰색 아닌 것 카운트 0번부터 i번까지 흰줄
            for p in range(i+1):
                for q in range(M):
                    if arr[p][q] != 'W':
                        count += 1
            # i+1번줄부터 j까지 파란줄
            for p in range(i+1, j+1):
                for q in range(M):
                    if arr[p][q] != 'B':
                        count += 1
            # 나머지 빨간줄
            for p in range(j+1, N):
                for q in range(M):
                    if arr[p][q] != 'R':
                        count += 1
            if min_count > count:
                min_count = count
    return min_count

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(f'#{test}', flag(N, M, arr))