def arr_sum(k, result):
    global min_result
    # 세로줄 끝까지 왔을 때, 결과 비교
    if k == N:
        if min_result > result:
            min_result = result
        return
    # 현재의 최솟값보다 커지면 가지치기
    if min_result < result:
        return
    # 세로줄 N개가 겹치면 안됨, check로 세로줄 사용 체크
    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            arr_sum(k + 1, arr[k][i] + result)
            check[i] = 0

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _  in range(N)]
    check = [0] * N
    # N 최대 10
    min_result = 99
    arr_sum(0, 0)
    print(f'#{test}', min_result)