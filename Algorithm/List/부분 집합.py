# 집합을 입력 받아서 합이 0인 부분 집합 반환
def Sum_Subset(N, arr):
    for i in range(1<<N):
        subset = []
        sum_sub = 0
        for j in range(N):
            if i & (1<<j):
                subset.append(arr[j])
        for k in subset:
            sum_sub += k
        if sum_sub == 0 and len(subset) != 0:
            return 1
    return 0
T = int(input())
for test in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#{test}', Sum_Subset(10, arr))