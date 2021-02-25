def Sudoku(arr):
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    dia = [1, 4, 7]
    for i in range(9):
        # 가로 세로줄 검사
        # 1 ~ 9까지 모두 있는지 확인
        check_x = [0] * 9
        check_y = [0] * 9
        for j in range(9):
            check_x[arr[i][j]-1] += 1
            check_y[arr[j][i]-1] += 1

        for j in range(9):
            if check_x[j] == 0 or check_y[j] == 0:
                return 0
    # 정사각형 검사
    for i in dia:
        for j in dia:
            check_dia = [0] * 9
            for k in range(9):
                check_dia[arr[i + dx[k]][j + dy[k]] - 1] += 1
            for p in range(9):
                if check_dia[p] == 0:
                    return 0
    return 1

T = int(input())
for test in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{test}', Sudoku(arr))