def dfs(N, x, y, result):
    # dfs 완전탐색
    global min_result
    # 최소값보다 커지면 가지치기
    if result >= min_result:
        return
    if x == N or y == N:
        return
    # 오른쪽 밑 끝에 도착
    if y == N-1 and x == N-1:
        result += arr[x][y]
        min_result = min(min_result, result)
        return
    # 현재 위치 더해주고
    result += arr[x][y]
    # 오른쪽, 아래 이동
    dfs(N, x+1,y,result)
    dfs(N,x,y+1,result)

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_result = 999999999999
    dfs(N, 0,0,0)
    print(f'#{test}', min_result)