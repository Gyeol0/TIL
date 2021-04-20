def binarySearch(N, M, A, B):
    count = 0
    A.sort()
    for i in range(M):
        left = 0
        right = N-1
        current = -1
        while left <= right:
            mid = (left+right) // 2
            if A[mid] > B[i]:
                if current != 0:
                    current = 0
                    right = mid - 1
                else:
                    break
            elif A[mid] < B[i]:
                if current != 1:
                    current = 1
                    left = mid+1
                else:
                    break
            else:
                count += 1
                break
    return count

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f'#{test}', binarySearch(N,M, A, B))