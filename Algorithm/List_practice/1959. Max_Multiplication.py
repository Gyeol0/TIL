def Max_Multiplication(A, B, N, M):
    answer = -9999999999
    # B가 더 길 때
    if N > M:
        # 시작점
        for i in range(N-M+1):
            mul = 0
            # M개 곱
            for j in range(M):
                mul += A[j + i] * B[j]
            if mul > answer:
                answer = mul
    # A가 더 길 때
    elif N < M:
        # 시작점
        for i in range(M-N+1):
            mul = 0
            # N개 곱
            for j in range(N):
                mul += A[j] * B[j + i]
            if mul > answer:
                answer = mul
    # 길이가 같을 때
    else:
        answer = 0
        for i in range(N):
            answer += A[i] * B[i]
    return answer

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f'#{test}', Max_Multiplication(A, B, N, M))