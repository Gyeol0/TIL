# 최대 공약수 메서드
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 이진수로 변환하는 메서드
def binNum(s):
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

def password(N, M, arr):
    answer = [] # 코드 숫자합을 담을 리스트
    all_code = [] # 모든 암호 코드를 담을 리스트
    # 앞 뒤 0은 모두 자르기 때문에 가운데만 파악
    value = {
        '211': 0,
        '221': 1,
        '122': 2,
        '411': 3,
        '132': 4,
        '231': 5,
        '114': 6,
        '312': 7,
        '213': 8,
        '112': 9
    }
    # 배열 이진수로 변혼
    for i in range(N):
        for j in range(M):
            arr[i][j] = binNum(arr[i][j])
        arr[i] = ''.join(arr[i])

    # 암호코드 가져오기
    # 처음에 1로 시작하고 1로 끝나는 모든 코드를 가져온다
    password_list = []
    for i in range(N):
        for j in range(len(arr[i])-1, -1, -1):
            if arr[i][j] == '1':
                end = j
                break
        for j in range(len(arr[i])):
            if arr[i][j] == '1':
                start = j
                if arr[i][start: end + 1] not in password_list:
                    password_list.append(arr[i][start: end + 1])
                break


    # 1, 0의 개수를 세면서 코드로 변환
    for i in password_list:
        phase = 1
        all_ratio = []
        ratio = []
        current = '1'
        count = 0
        for j in range(len(i)):
            if i[j] == current:
                count += 1
            elif i[j] != current:
                if phase < 4:
                    ratio.append(count)
                    count = 1
                    current = i[j]
                    phase += 1
                else:
                    phase = 1
                    count = 1
                    current = i[j]
                    all_ratio.append(ratio)
                    ratio = []
        if len(ratio) == 2:
            ratio.append(count)
        all_ratio.append(ratio)

        # 한 줄에 암호코드 여러 개 있을 수도 있어서
        for p in range(len(all_ratio) // 8):
            code = []
            # 비율을 최대공약수로 나누어 서로소로 만든다
            for q in range(8):
                g1 = gcd(all_ratio[q+p*8][0], all_ratio[q+p*8][1])
                g = gcd(g1, all_ratio[q+p*8][2])

                ratio_value = ''
                for k in range(3):
                    ratio_value += str(all_ratio[q+p*8][k] // g)

                code.append(value[ratio_value])

            # 암호 코드 겹치지 않도록
            if code not in all_code:
                all_code.append(code)

    # 결과 검증
    for code in all_code:
        result = 0
        for j in range(8):
            if j % 2:
                result += code[j]
            else:
                result += code[j] * 3
        if result % 10:
            answer.append(0)
        else:
            answer.append(sum(code))
    return sum(answer)

T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(f'#{test}', password(N, M, arr))