def Room(N, arr):
    check = [0]*401
    for i in arr:
        start = i[0]
        go = i[1]
        # 반대로 갈 떄
        if start > go:
            start, go = go, start
        # 출발점이 # 짝수면 이전 방도 겹칩
        if start % 2 == 0:
            start - 1
        # 도착점이 홀수면 다음 방도 겹침
        if go % 2:
            go += 1

        # 겹치는 경로
        for j in range(start, go+1):
            check[j] += 1
    # 하나도 안겹치면 리스트 원소 모두 1, 최대값이 최대 겹치는 수, 겹치는 수만큼 걸린다.
    result = 0
    for i in check:
        if result < i:
            result = i
    return result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test}', Room(N, arr))