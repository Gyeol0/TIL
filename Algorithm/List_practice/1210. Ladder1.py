def Ladder1(N, arr):
    # 맨 아래에서 X 위치 찾기
    for i in range(N):
        if arr[N-1][i] == 2:
            x = N-1
            y = i
    # 양 옆, 위로 거꾸로 올라가기
    # 양 옆 우선
    dx = [0, 0, -1]
    dy = [1, -1, 0]
    k = 0
    # 맨 맨위에 도달할 때까지
    while x > 0:
        ax = x + dx[k]
        ay = y + dy[k]
        if 0 <= ax < N and 0 <= ay <N:
            # 사다리가 연결되어 있을 때
            if arr[ax][ay] == 1:
                x = ax
                y = ay
                arr[ax][ay] = 2
        k = (k + 1) % 3
    return y

for t in range(10):
    test= int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    print(f'#{test}', Ladder1(100, arr))