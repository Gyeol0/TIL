def Box(N, Q, change):
    box = [0] * N
    for i in range(Q):
        L = change[i][0]
        R = change[i][1]
        # i로 변경
        for j in range(L-1, R):
            box[j] = i + 1
    return box

T = int(input())
for test in range(1, T+1):
    N, Q = map(int, input().split())
    change = [list(map(int, input().split())) for _ in range(Q)]
    print(f'#{test}', *Box(N, Q, change))