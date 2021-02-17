def Pattern1(p, t):
    M = len(p)
    N = len(t)
    # i는 텍스트 인덱스, j는 패턴 인덱스
    i = 0
    j = 0
    while j < M and i < N:
        # 틀렸을때
        if t[i] != p[j]:
            i = i - j # 텍스트 인덱스 다시 제자리로
            j = -1 # 패턴 인덱스는 다시 처음으로
        # 한 칸 앞으로
        i += 1
        j += 1
    if j == M:
        return i - M # 검색 성공
    else:
        return -1 # 실패

print(Pattern1('abc', 'aasabsabbcabcsa'))