def Number_Sorting(N, arr):
    # Bubble sort
    for i in range(N-1, 0, -1):
        # 앞에서부터 한 칸 뒤의 수와 비교
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
T = int(input())
for test in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = Number_Sorting(N, numbers)
    print(f'#{test}', end = ' ')
    for i in numbers:
        print(i, end = ' ')
    print()