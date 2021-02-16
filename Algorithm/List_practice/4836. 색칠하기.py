def Painting(N, squares, k):
    count = 0
    # 면적 초기화
    arr = [[0]*k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            for p in squares:
                # 정사각형 내부에 있는지 확인
                if p[0] <= i <= p[2] and p[1] <= j <= p[3]:
                    # 아무 색도 칠하지 않았으면 색칠
                    if arr[i][j] == 0:
                        arr[i][j] = p[4]
                    # 덧칠했을 때 보라색인지 확인
                    elif arr[i][j] + p[4] == 3:
                        count += 1
    return count

T = int(input())
for test in range(1, T+1):
    N = int(input())
    squares = []
    for _ in range(N):
       squares.append(list(map(int,input().split())))
    print(f'#{test}', Painting(N, squares, 10))
