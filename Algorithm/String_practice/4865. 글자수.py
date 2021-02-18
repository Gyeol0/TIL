def Count_Str(str1, str2):
    count = {}
    max_count = 0
    # count 딕셔너리 생성
    for i in str1:
        count[i] = 0
    # 글자별 count하여 딕셔너리에 추가
    for i in count.keys():
        for j in str2:
            if i == j:
                count[i] += 1
    # 최대 count 계산
    for i in count.values():
        if max_count < i:
            max_count = i
    return max_count

T = int(input())
for test in range(1, T+1):
    str1 = input()
    str2 = input()
    print(f'#{test}', Count_Str(str1, str2))