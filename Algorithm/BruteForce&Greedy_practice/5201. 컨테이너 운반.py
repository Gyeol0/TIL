def container(N, M, weight, truck):
    # 가장 용량 큰 트럭이 담을 수 있는 화물 중 가장 무거운 것을 담으면 된다.
    result = 0
    weight = sorted(weight, reverse=True)
    truck = sorted(truck, reverse=True)
    idx = 0
    for i in range(N):
        if idx == M:
            break
        if weight[i] <= truck[idx]:
            result += weight[i]
            idx += 1
    return result

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    print(f'#{test}', container(N, M, weight, truck))
