def monster(D, L, N):
    sum_d = 0
    for i in range(N):
        sum_d += D*(1+i*L/100)
    return int(sum_d)
T = int(input())
for test in range(1, T+1):
    D, L, N = map(int, input().split())
    print(f'#{test}', monster(D, L, N))