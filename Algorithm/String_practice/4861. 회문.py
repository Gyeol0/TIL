def Circular(N, M, str1):
    for i in range(N):
        for j in range(N-M+1):
            # 가로 회문 찾기
            row1 = ''
            row2 = ''
            for k in range(j, j+M):
                # 가로 정방향
                row1 += str1[i][k]
                # 가로 역방향
                row2 = str1[i][k] + row2
            if row1 == row2:
                return row1
            # 세로 회문 찾기
            col1 = ''
            col2 = ''
            for k in range(j, j+M):
                # 세로 정방향
                col1 += str1[k][i]
                # 세로 역방향
                col2 = str1[k][i] + col2
            if col1 == col2:
                return col1

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    str1 = []
    for _ in range(N):
        str1.append(input())
    print(f'#{test}', Circular(N,M,str1))
