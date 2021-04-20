def bus(idx, arr, count):
    global min_count
    if count >= min_count:
        return
    if idx >= N-1:
        min_count = min(min_count, count)
        return
    remain = arr[idx]
    if remain >= N - idx - 1:
        min_count = min(min_count, count)
        return
    for i in range(remain, -1, -1):
        bus(idx + i, arr, count + 1)

T = int(input())
for test in range(1, T+1):
    arr1 = list(map(int, input().split()))
    N = arr1[0]
    arr = arr1[1:]
    min_count = 99999999
    bus(0, arr, 0)
    print(f'#{test}', min_count)