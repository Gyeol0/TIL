def Special_Sort(N, arr):
    # 최댓값을 위치할지 최솟값을 위치할지 판단
    max_min = True
    # 선택 정렬
    for i in range(N-1):
        maxIndex = i
        minIndex = i
        for j in range(i+1, N):
            # 최댓값 위치할 때
            if max_min:
                if arr[maxIndex] < arr[j]:
                    maxIndex = j
            
            # 최솟값 위치할 때
            else:
                if arr[minIndex] > arr[j]:
                    minIndex = j
        if max_min:
            arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
            # 다음 차례 최솟값
            max_min = False
        else:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
            # 다음 차례 최댓값
            max_min = True
    return arr

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test}', *Special_Sort(N, arr)[:10])