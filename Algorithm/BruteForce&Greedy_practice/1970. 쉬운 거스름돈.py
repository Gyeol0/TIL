def change(N):
    result = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 높은 금액부터 처리해주면 된다.
    for i in range(8):
        if N >= money[i]:
            result[i] = N // money[i]
            N %= money[i]

    return result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    result = change(N)
    print(f'#{test}')
    print(*result)