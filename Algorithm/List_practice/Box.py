def Box(i, arr):
    L, R = map(int, input().split())
    for k in range(L-1, R):
        arr[k] = i
    return arr

T = int(input())
for test in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0 for _ in range(N)]
    for i in range(1, Q+1):
        box = Box(i, box)
    print(f'#{test}', end = ' ')
    for i in box:
        print(i, end = ' ')
    print()