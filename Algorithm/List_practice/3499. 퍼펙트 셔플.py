def shuffle(N, card):
    result = []
    # 홀수개면 mid + 1
    if N % 2:
        mid = N // 2 + 1
    else:
        mid = N // 2
    for i in range(N // 2):
        result.append(card[i])
        result.append(card[i + mid])
    # 홀수개면 첫 번째 덱 마지막 추가
    if N % 2:
        result.append(card[mid-1])
    return result

T = int(input())
for test in range(1, T+1):
    N = int(input())
    card = input().split()
    print(f'#{test}', *shuffle(N, card))