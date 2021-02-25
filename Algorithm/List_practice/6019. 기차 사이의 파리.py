def Train(D, A, B, F):
    result = 0
    # A + B가 이동하는 거리 이상으로 사이 거리가 남아 있을 때
    while D >= (A + B):
        result += F
        D -= A + B
    # 나머지 거리 비율 더하기
    result += D / (A + B) * F
    return result

T = int(input())
for test in range(1, T+1):
    D, A, B, F = map(int, input().split())
    print(f'#{test}', Train(D, A, B, F))