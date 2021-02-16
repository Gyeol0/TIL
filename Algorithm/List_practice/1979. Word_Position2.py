def Word_Position(N, K, arr):
    count = 0
    # 단어는 오른쪽 또는 밑으로 이어진다.
    for i in range(N):
        length_x = 0
        length_y = 0
        for j in range(N):
            # 출발지점 찾기
            if arr[i][j] == 1:
                # 길이 증가
                length_x += 1
            else:
                # 길이 막혔을 때, 길이가 K 인지
                if length_x == K:
                    count += 1
                # 길이 초기화
                length_x = 0
            # y도 같은 방식
            if arr[j][i] == 1:
                length_y += 1
            else:
                if length_y == K:
                    count += 1
                length_y = 0
        # 행이나 열이 바뀌었을 때 길이가 K인지
        if length_x == K:
            count += 1
        if length_y == K:
            count += 1
    return count

T = int(input())
for test in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
       arr.append(list(map(int,input().split())))
    print(f'#{test}', Word_Position(N, K, arr))