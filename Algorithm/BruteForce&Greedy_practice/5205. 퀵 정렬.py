def partition(arr, start, end):
    pivot = start
    L = start
    R = end
    while L <= R:
        while L <= R and arr[L] <= arr[pivot]:
            L += 1
        while L <= R and arr[R] >= arr[pivot]:
            R -= 1
        if L < R:
            arr[L], arr[R] = arr[R], arr[L]
    arr[start], arr[R] = arr[R], arr[start]
    return R

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = quick_sort(arr, 0, N-1)
    print(f'#{test}', arr[N//2])