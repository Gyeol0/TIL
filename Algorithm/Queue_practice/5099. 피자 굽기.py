def Pizza(N, M, arr):
    # 화덕에서 꺼내서 확인할 자리
    idx = 0
    # 다음 화덕에 넣을 치즈 번호
    next = N
    # 다 녹은 치즈 개수
    count = 0
    num = [i+1 for i in range(N)]
    # 치즈별 넘버링
    pizza = list(map(list, zip(arr[:N], num)))
    while True:
        # 다 녹지 않은 치즈
        if pizza[idx][0] != 0:
            # 반으로 녹이고
            pizza[idx][0] //= 2
            # 다 녹으면
            if pizza[idx][0] == 0:
                # 다음 순번 치즈 넣음
                if next < M:
                    pizza[idx] = [arr[next], next + 1]
                    next += 1
                # 다 녹은 치즈 개수 + 1
                count += 1
        # 1개 빼고 다 녹으면 stop
        if count == M - 1:
            break
        # 회전
        idx = (idx + 1) % N
    # 0이 아닌 치즈 번호 반환
    for i in pizza:
        if i[0] != 0:
            return i[1]
T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{test}', Pizza(N, M, arr))