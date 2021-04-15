def babyGin(N, arr):
    player1 = [0] * 10
    player2 = [0] * 10
    p1 = False
    p2 = False
    for i in range(N//2):
        num1 = arr[i*2]
        num2 = arr[i*2+1]
        player1[num1] += 1
        player2[num2] += 1

        # 플레이어 1 triplet 확인
        if player1[num1] >= 3:
            p1 = True
        # 플레이어 2 triplet 확인
        if player2[num2] >= 3:
            p2 = True

        # 플레이어 1, 2 run 확인
        for j in range(8):
            if player1[j] >= 1 and player1[j+1] >= 1 and player1[j+2] >= 1:
                p1 = True
            if player2[j] >= 1 and player2[j+1] >= 1 and player2[j+2] >= 1:
                p2 = True

        if p1 and p2:
            return 1
        if p1:
            return 1
        if p2:
            return 2

    return 0

T = int(input())
for test in range(1, T+1):
    N = 12
    arr = list(map(int, input().split()))
    print(f'#{test}', babyGin(N, arr))