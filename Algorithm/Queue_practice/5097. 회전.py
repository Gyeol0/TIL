def Turn(N, M, arr):
    front = 0
    for _ in range(M):
        front = (front + 1) % N

    return arr[front]
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{test}', end = ' ')
    print(Turn(N, M, arr))