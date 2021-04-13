def binNum(N, s):
    result = ''
    for i in s:
        binary = ''
        number = int(i, 16)
        while number:
            binary = str(number % 2) + binary
            number //= 2
        binary = binary.zfill(4)
        result += binary
    return result

T = int(input())
for test in range(1, T+1):
    N, s = input().split()
    print(f'#{test}', binNum(N, s))