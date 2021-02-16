def Word_Position(N, K, arr):
    count = 0
    # 단어는 오른쪽 또는 밑으로 이어진다.
    dx = [1, 0]
    dy = [0, 1]
    for i in range(N):
        for j in range(N):
            # 출발지점 찾기
            if arr[i][j] == 1:
                for p in range(2):
                    # 벽이 아니거나 앞에 빈 칸이 있으면 안됨
                    if i-dx[p] < 0 or j-dy[p] < 0 or arr[i-dx[p]][j-dy[p]] != 1:
                        length = 1
                        x = i
                        y = j
                        # 오른쪽 또는 아래 방향으로 직진
                        while 1:
                            ax = x + dx[p]
                            ay = y + dy[p]
                            if 0 <= ax < N and 0 <= ay < N:
                                if arr[ax][ay] == 1:
                                    length += 1
                                    x = ax
                                    y = ay
                                    # 길이가 K 넘어가면 stop
                                    if length > K:
                                        break
                                else:
                                    break
                            else:
                                break
                        # 길이 확인
                        if length == K:
                            count += 1
    return count

T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
       arr.append(list(map(int,input().split())))
    print(f'#{test}', Word_Position(N, K, arr))