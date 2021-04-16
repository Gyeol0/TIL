def shelf(N, B, arr):
    min_value = 99999999999
    # 부분집합 구해서 계산
    for i in range(1<<N):
        subset = 0
        for j in range(N):
            if i & (1<<j):
                subset += arr[j]

        if subset >= B:
            min_value = min(min_value, subset - B)

    return min_value

for test in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{test}', shelf(N, B, arr))

def shelf2(N, k, B, value):
    global min_value
    # 재귀 모든 상황 계산
    if k == N:
        if B <= value:
            min_value = min(min_value, value-B)
        return

    # 현재 사람 넣는다
    shelf2(N, k+1, B, value+arr[k])
    # 안 넣는다
    shelf2(N, k+1, B, value)

T = int(input())
for test in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_value = 99999999999
    shelf2(N, 0, B, 0)
    print(f'#{test}', min_value)
