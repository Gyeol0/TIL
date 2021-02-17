def GNS(N, arr):
    result = []
    # 행성의 숫자를 0~9로 만들 딕셔너리
    num_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    num_dict = {}
    for i in range(10):
        num_dict[num_str[i]] = i
    # 표현된 문자열 count
    count = [0 for _ in range(10)]
    for i in range(N):
        count[num_dict[arr[i]]] += 1
    # count 만큼 0~9 순대로 *
    for i in range(10):
        result += [num_str[i]] * count[i]
    return result

T = int(input())
for test in range(1, T+1):
    tc, N = input().split()
    arr = input().split()
    print(tc)
    print(*GNS(int(N), arr))