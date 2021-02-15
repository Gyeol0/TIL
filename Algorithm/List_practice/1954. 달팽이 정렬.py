def Snail_Sort(N):
    # N x N 배열 초기화
    arr = [[0]*N for _ in range(N)]
    # 처음 위치 초기화
    x = 0
    y = -1
    # 방향 초기화
    po = 1
    value = 1
    while N > 0:
        # 행 채우기
        for i in range(N):
            y += 1 * po
            arr[x][y] = value
            value += 1
        # 한 칸 줄이기
        N -= 1
        # 열 채우기
        for i in range(N):
            x += 1* po
            arr[x][y] = value
            value += 1
        # 방향 반대로
        po *= -1
    return arr
T = int(input())
for test in range(1, T+1):
    N = int(input())
    result = Snail_Sort(N)
    print(f'#{test}')
    for i in range(N):
        for j in range(N):
            print(result[i][j], end = ' ')
        print()