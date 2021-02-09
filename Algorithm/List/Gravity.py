def gravity(N, lst):
    max_height = 0
    for i in range(N-1):
        count = 0
        # 밑에 있는 상자들 중에서 자신보다 높은 상자 count
        for j in range(i+1, N):
            if lst[i] <= lst[j]:
                count += 1
        # 오른쪽으로 회전하였을 때 현재 높이 - 자신보다 높거나 같은 상자 count
        if max_height < N - (i+1) - count:
            max_height = N - (i+1) - count
    return max_height
N = int(input())
height = list(map(int, input().split()))
print(gravity(N, height))
