def String(string, key):
    idx = 0
    count = 0
    k = 0
    while k >= 0:
        # k+1 인덱스부터 검색
        k = string.find(key, idx)
        idx = k + 1
        count += 1
    count -= 1
    return count

for i in range(10):
    test = int(input())
    key = input()
    string = input()
    print(f'#{test}', String(string, key))