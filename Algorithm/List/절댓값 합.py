# 차의 절댓값 함수
def min_abs(a,b):
    if a < b:
        return b-a
    else:
        return a-b
def Sum_Abs(N, M ,arr):
    abs_sum = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N): # 행
        for j in range(M): # 열
            for k in range(4): # 인접 요소
                ax = i + dx[k]
                ay = j + dy[k]
                if ax >= 0 and ax < N and ay >=0 and ay <M: # 범위를 벗어나는지
                    # abs_sum += abs(arr[i][j] - arr[ax][ay])
                    abs_sum += min_abs(arr[i][j], arr[ax][ay])
    return abs_sum

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(f'#{test}', Sum_Abs(N, N, arr))