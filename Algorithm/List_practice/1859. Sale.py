T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 뒤에서 부터 현재 최고가보다 가격이 올라가면 현재 최고가 변경 및 판매
    for i in range(N-1, -1, -1):
        if i == N-1:
            current = arr[i]
            result = 0
        else:
            if current > arr[i]:
                result += current - arr[i]
            else:
                current = arr[i]
    print(f'#{test}', result)
