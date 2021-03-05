def Ham(N, L, ingredient):
    # i 칼로리 안에 최대 점수 dp
    dp = [0] * (L + 1)
    for i in ingredient:
        # 제한 칼로리부터 i번 재료의 칼로리까지
        for j in range(L, i[1] - 1, -1):
            # 현재보다 이전의 최대 점수에 점수를 더한 것이 더 크면 바꿔라
            if dp[j] < i[0] + dp[j - i[1]]:
                dp[j] = i[0] + dp[j - i[1]]
    return dp[L]

T = int(input())
for test in range(1, T + 1):
    N, L = map(int, input().split())
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test}', Ham(N, L, ingredient))