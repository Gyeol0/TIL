def Paper(N):
    dp = []
    N = N // 10
    dp.append(1)
    dp.append(3)
    for i in range(2,N):
        # (i-1) 왼쪽 끝이 2 x 1 막대, (i-2) 왼쪽 끝이 2 x 2 막대(가로로 2x1 2개 또는 2x2 1개 이므로 * 2)
        dp.append(dp[i-1] + dp[i-2] * 2)
    return dp[-1]

T = int(input())
for test in range(1, T+1):
    N = int(input())
    print(f'#{test}', Paper(N))