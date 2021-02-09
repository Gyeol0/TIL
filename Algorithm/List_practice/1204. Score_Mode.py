def Score_Mode(arr):
    score_list = [0 for _ in range(101)]
    max_idx = -1
    max_count = -1
    # 점수별 count 리스트 생성
    for i in arr:
        score_list[i] += 1
        # 최빈값
        if max_count < score_list[i]:
            max_count = score_list[i]
            max_idx = i
        # 같은 빈도 수 일 때 큰 점수로 변환
        elif max_count == score_list[i]:
            if max_idx < i:
                max_idx = i
    return max_idx
T = int(input())
for _ in range(T):
    test = int(input())
    score = list(map(int, input().split()))
    print(f'#{test}', Score_Mode(score))
