def Card(num):
    count = [0 for _ in range(10)]
    max_count = 0
    while num:
        count[num%10] += 1
        num = num // 10
    for i in range(10):
        if max_count <= count[i]:
            max_count = count[i]
            max_idx = i
    return max_idx, max_count

T = int(input())
for test in range(1, T+1):
    N = int(input())
    number = int(input())
    result = Card(number)
    print(f'#{test}', result[0], result[1])
