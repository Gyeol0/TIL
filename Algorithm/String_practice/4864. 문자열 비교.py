def String_Compare(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    # 문자열 비교
    for i in range(l2-l1+1):
        # i부터 str1의 길이만큼 슬라이싱
        if str2[i:i+l1] == str1:
            return 1
    return 0

T = int(input())
for test in range(1, T+1):
    str1 = input()
    str2 = input()
    print(f'#{test}', String_Compare(str1, str2))