def dart(arr):
    total = 0
    for i in arr:
        length = (i[0]**2 + i[1]**2) ** (1/2)
        if length <= 200:
            if length % 20:
                score = 10 -length // 20
            else:
                score = 11- length // 20
            total += score
    return int(total)
T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr_dart = []
    for i in range(N):
        x, y = map(int, input().split())
        arr_dart.append((x,y))
    print(f'#{test}', dart(arr_dart))