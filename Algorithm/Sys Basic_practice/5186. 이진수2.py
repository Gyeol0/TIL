def binNum2(s):
    result = ''
    while s != 1:
        s -= int(s)
        s *= 2
        result += str(int(s))
        if len(result) >= 13:
            return 'overflow'
    return result

T = int(input())
for test in range(1, T+1):
    s = float(input())
    print(f'#{test}', binNum2(s))