# k 진수를 10진수로 바꾸는 메서드
def numChange(s1, k):
    result = 0
    for i in range(len(s1)):
        result += int(s1[i]) * (k**(len(s1)-i-1))
    return result


def change(s1, s2):
    # 한 자리 바꾼 이진 수
    binary = []
    for i in range(len(s1)):
        if s1[i] == '1':
            s1[i] = '0'
            binary.append(numChange(s1, 2))
            s1[i] = '1'
        else:
            s1[i] = '1'
            binary.append(numChange(s1, 2))
            s1[i] = '0'

    # 한 자리 바꾼 3진수
    third = []
    for i in range(len(s2)):
        if s2[i] == '0':
            s2[i] = '1'
            third.append(numChange(s2, 3))
            s2[i] = '2'
            third.append(numChange(s2, 3))
            s2[i] = '0'
        elif s2[i] == '1':
            s2[i] = '0'
            third.append(numChange(s2, 3))
            s2[i] = '2'
            third.append(numChange(s2, 3))
            s2[i] = '1'
        else:
            s2[i] = '0'
            third.append(numChange(s2, 3))
            s2[i] = '1'
            third.append(numChange(s2, 3))
            s2[i] = '2'
    
    # 같은 수면 return
    for i in binary:
        if i in third:
            return i

T = int(input())
for test in range(1, T+1):
    s1 = list(input())
    s2 = list(input())
    print(f'#{test}', change(s1, s2))