def Snail_Sort2(N):
    # N x N 배열 초기화
    arr = [[0]*N for _ in range(N)]
    # 처음 위치 초기화
    x = 0
    y = -1
    # 상하좌우
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    value = 1
    cnt = N
    while cnt > 0:
        for i in range(4):
            # 밖으로 나가거나 이미 들렸던 곳이 나올 때까지 직진
            while True:
                ax = x + dx[i]
                ay = y + dy[i]
                # 밖으로 나가는지
                if ax>=0 and ax<N and ay>=0 and ay<N:
                    # 들렸던 곳인지
                    if arr[ax][ay] == 0:
                        arr[ax][ay] = value
                        value += 1
                        # 현재 위치 변경
                        x, y = ax, ay
                    else:
                        break
                else:
                    break
        # 한 바퀴 돌고 2칸 감소
        cnt -= 2
    return arr

T = int(input())
for test in range(1, T+1):
    N = int(input())
    result = Snail_Sort2(N)
    print(f'#{test}')
    for i in range(N):
        for j in range(N):
            print(result[i][j], end = ' ')
        print()