def Bus_Route(N, A, B, C):
    route = []
    # 정류장을 지나가는지 확인
    for i in C:
        result = 0
        # 노선마다 확인
        for j in range(N):
            if i >= A[j] and i <= B[j]:
                result += 1
        route.append(result)
    return route

T = int(input())
for test in range(1, T+1):
    N = int(input())
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    P = int(input())
    C = [0 for _ in range(P)]
    for i in range(P):
        C[i] = int(input())
    route = Bus_Route(N, A, B, C)
    print(f'#{test}', end = ' ')
    for i in route:
        print(i, end = ' ')
    print()