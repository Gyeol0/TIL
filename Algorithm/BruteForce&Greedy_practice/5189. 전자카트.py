def perm(idx):
    # 모든 순열을 만들어서 비교
    global min_result
    # 순열 완성
    if idx == N-1:
        result = 0
        # 0부터 시작해서 순회하고 돌아옴
        start = 0
        for j in arr:
            result += value[start][j]
            start = j
        # 마지막 돌아오는 과정
        result += value[start][0]
        # 비교
        min_result = min(min_result, result)
    else:
        for i in range(idx, N-1):
            # idx는 내가 결정할 칸
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx+1)
            arr[idx], arr[i] = arr[i], arr[idx]

T = int(input())
for test in range(1, T+1):
    N = int(input())
    value = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(1, N)]
    min_result = 99999999999
    perm(0)
    print(f'#{test}', min_result)