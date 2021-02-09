def Factorization(N):
    F = [2, 3, 5, 7, 11]
    answer = []
    for i in F:
        count = 0
        while N % i == 0:
            count += 1
            N //= i
        answer.append(count)
    return answer

T = int(input())
for test in range(1, T+1):
    N = int(input())
    result = Factorization(N)
    print(f'#{test}', end = ' ')
    for i in result:
        print(i, end = ' ')
    print()