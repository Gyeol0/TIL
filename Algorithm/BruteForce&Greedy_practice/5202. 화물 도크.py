def dock(schedule):
    result = 0
    # 끝나는 시간으로 정렬
    schedule = sorted(schedule, key=lambda x: x[1])
    start = 0
    # 스케줄 할 수 있으면 함
    for i in schedule:
        if i[0] >= start:
            result += 1
            start = i[1]
    return result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    schedule = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test}', dock(schedule))