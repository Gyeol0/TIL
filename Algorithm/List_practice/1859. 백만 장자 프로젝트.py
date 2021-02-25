def Project(N, arr):
    for i in range(N-1, -1, -1):
        # 마지막 가격으로 초기화
        if i == N-1:
            current = arr[i]
            result = 0
        # 현재 가격(팔 가격)보다 싸면 사고 판다(뒤에서부터).
        else:
            if current > arr[i]:
                result += current - arr[i]
            # 현재 가격이(팔 가격)이 더 비싸면 안사고 팔 가격 변경
            else:
                current = arr[i]
    return result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test}', Project(N, arr))