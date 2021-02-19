def Col_String(N, arr):
    result = ''
    # 최대 문자열 15
    for i in range(15):
        for j in range(N):
            # 짧으면 패스
            if i < len(arr[j]):
                result += arr[j][i]
    return result

T = int(input())
for test in range(1, T+1):
    arr = []
    for _ in range(5):
        arr.append(input())
    print(f'#{test}', Col_String(5, arr))