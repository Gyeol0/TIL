def min_max(arr):
    # 1 ≤ num ≤ 1000000
    # min, max 초기화
    min_num = 1000000
    max_num = 1
    for i in arr:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i
    return max_num - min_num

T = int(input())
for i in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{i}', min_max(numbers))