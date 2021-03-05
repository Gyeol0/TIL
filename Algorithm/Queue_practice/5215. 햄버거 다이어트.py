def Ham(N, L, score, cal, idx):
    global max_score
    # 칼로리가 넘어가면 그만
    if cal > L:
        return
    # 다음 재료를 모두 먹어도 현재 최고점을 못넘기면 가지치기
    if sum(ingredient[0][idx:]) + score <= max_score:
        return

    # 마지막 순번까지 가면 비교하고 stop
    if idx == N:
        if score > max_score:
            max_score = score
        return

    # 현재 idx 재료를 넣지 않고 진행
    Ham(N, L, score, cal, idx + 1)
    # 현재 idx 재료를 넣고 진행
    Ham(N, L, score + ingredient[0][idx], cal + ingredient[1][idx], idx + 1)

T = int(input())
for test in range(1, T+1):
    N, L = map(int, input().split())
    ingredient = [list(map(int, input().split())) for _ in range(N)]
    ingredient = list(zip(*ingredient))
    max_score = 0
    Ham(N, L, 0, 0, 0)
    print(f'#{test}', max_score)