def view(N, building):
    answer = 0
    for j in range(2, N-2):
        # 전방과 후방 view 확인, 모두 현재 빌딩보다 낮아야 한다.
        if building[j] > building[j+1] and building[j] > building[j+2] and building[j] > building[j-1] and building[j] > building[j-2]:
            max_height = 0
            # 전방, 후방에서 가장 높은 빌딩 높이
            for i in range(j-2, j+3):
                if i != j:
                    if max_height < building[i]:
                        max_height = building[i]
            # 확보된 조망권
            answer += building[j] - max_height
    return answer

for i in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    print(f'#{i}',view(N, building))