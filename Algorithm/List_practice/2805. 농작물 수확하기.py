def Crops(N, arr):
    mid = N // 2
    result = 0
    for i in range(N):
        for j in range(N):
            # 가운데 가로, 세로줄
            if i == mid or j == mid:
                result += int(arr[i][j])
            else:
                # 중앙 가로줄 아래
                if i > mid:
                    if i - mid <= j <= 3 * mid - i:
                        result += int(arr[i][j])
                # 중앙 가로줄 위
                else:
                    if mid - i <= j <= mid + i:
                        result += int(arr[i][j])
    return result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{test}', Crops(N, arr))
