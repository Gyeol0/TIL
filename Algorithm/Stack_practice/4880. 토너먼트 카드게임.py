# 1 가위, 2 바위, 3 보

def Game(N, player):
    if N == 1:
        # [(가위, number)] 형태로 들어감
        return player
    if N % 2 == 0:
        g1 = Game(N // 2, player[:N // 2])
        g2 = Game(N // 2, player[N // 2:])
    else:
        g1 = Game(N // 2 + 1, player[:N // 2 + 1])
        g2 = Game(N // 2 , player[N // 2 + 1:])
    # g1이 가위를 내고 이길 때
    if g1[0][0] == 1 and (g2[0][0] == 1 or g2[0][0] == 3):
        return g1
    # g1이 바위를 내고 이길 때
    elif g1[0][0] == 2 and (g2[0][0] == 1 or g2[0][0] == 2):
        return g1
    # g1이 보를 내고 이길 때
    elif g1[0][0] == 3 and(g2[0][0] == 2 or g2[0][0] == 3):
        return g1
    # 나머지는 g2가 이김
    else:
        return g2

T = int(input())
for test in range(1, T+1):
    N = int(input())
    p = list(map(int, input().split()))
    idx = [i for i in range(1, N+1)]
    player = list(zip(p, idx))
    print(f'#{test}', Game(N, player)[0][1])