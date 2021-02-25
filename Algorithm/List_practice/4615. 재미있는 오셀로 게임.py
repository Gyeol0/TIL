def Othello(N, M, arr):
    result = [[0]*N for _ in range(N)]
    dx = [0, 0, 1, -1, -1, 1, -1, 1]
    dy = [1, -1, 0, 0, -1, 1, 1, -1]
    count = {'B': 2, 'W': 2}
    # 첫 배치
    result[N // 2 - 1][N // 2 - 1] = 'W'
    result[N // 2 - 1][N // 2] = 'B'
    result[N // 2][N // 2 - 1] = 'B'
    result[N // 2][N // 2] = 'W'
    for i in range(M):
        # 흑돌
        if arr[i][2] == 1:
            result[arr[i][0] - 1][arr[i][1] - 1] = 'B'
            current = 'B'
            other = 'W'
            count['B'] += 1
        else:
            result[arr[i][0] - 1][arr[i][1] - 1] = 'W'
            current = 'W'
            other = 'B'
            count['W'] += 1

        # 가로 검사
        for k in range(8):
            x = arr[i][0] - 1
            y = arr[i][1] - 1
            turn = []
            while True:
                ax = x + dx[k]
                ay = y + dy[k]
                if 0 <= ax < N and 0 <= ay < N:
                    # 양 옆이 현재 놓은 돌이면 뒤집기
                    if result[ax][ay] == current:
                        for r in turn:
                            result[r[0]][r[1]] = current
                            count[current] += 1
                            count[other] -= 1
                        break
                    # 놓은 색과 다른 돌
                    # 뒤집을 돌
                    elif result[ax][ay] == other:
                        x = ax
                        y = ay
                        turn.append([ax, ay])
                    # 비어 있는 칸
                    else:
                        break
                else:
                    break
    return count

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    answer = Othello(N, M, arr)
    print(f'#{test}', answer['B'], answer['W'])