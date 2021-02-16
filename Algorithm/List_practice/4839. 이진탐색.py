def Binary_Book(P, A, B):
    # A, B 모두 찾을 것이라는 가정
    # 초기값
    start_A = 1
    start_B = 1
    end_A = P
    end_B = P
    while 1:
        # 중간값 계산
        mid_A = (start_A + end_A) // 2
        mid_B = (start_B + end_B) // 2
        if mid_A < A:
            start_A = mid_A
        elif mid_A > A:
            end_A = mid_A
        # A와 B 동시에 찾았을 때
        elif mid_B == B:
            return 0
        # A만 찾았을 때
        else:
            return 'A'
        if mid_B < B:
            start_B = mid_B
        elif mid_B > B:
            end_B = mid_B
        # B만 찾았을 때
        else:
            return 'B'

T = int(input())
for test in range(1, T+1):
    P, A, B = map(int, input().split())
    print(f'#{test}', Binary_Book(P, A, B))
