def make_table1(pat):
    # 최대 길이를 저장할 lps, 실패하였을 때 돌아갈 위치
    table = [0] * len(pat)
    # 접두사와 접미사가 같은 최대 길이
    length = 0
    for i in range(1, len(pat)):
        # length가 0보다 크다는 것은 바로 전까지는 일치했기 때문에
        # 다음부터 일치하지 않으므로
        # l을 줄여나가면서 짧게 만들면서 확인
        # 끝가지 접두사와 접미사가 맞는 것이 없으면 0으로 가게됨
        while length > 0 and pat[i] != pat[length]:
            length = table[length-1]

        # 일치할 때에는 최대 길이 1 증가
        if pat[i] == pat[length]:
            length += 1
            table[i] = length
        # 일치하지 않으면 그대로 둠, 모두 0으로 초기화 되어 있어서
    return table

def make_table2(pat):
    max_length = 0  # 접두사와 접미사가 같은 최대 길이
    # 최대 길이를 저장할 lps, 실패하였을 때 돌아갈 위치
    table = [0] * len(pat)
    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    # i가 0일 떄에는 -1, 길이가 1이어서 접두사와 접미사가 같다.
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pat[i] == pat[max_length]:
            max_length += 1
            table[i] = max_length
            i += 1
        else:
            # 일치하지 않는 경우
            if max_length != 0:
                # 이전 인덱스에서는 같았으므로 length를 줄여서 다시 검사
                max_length = table[max_length-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 table[i]는 0 이고 i는 1 증가
                table[i] = 0
                i += 1

    return table




def KMP(txt, pat):
    table = make_table1(pat)
    # 패턴 인덱스
    j = 0
    count = 0
    idx = []
    # i는 패턴이 시작할 위치를 찾음
    for i in range(len(txt)):
        while j > 0 and txt[i] != pat[j]:
            # 앞으로 이동
            j = table[j-1]
        # 일치 했을 때
        if txt[i] == pat[j]:
            # 패턴 인덱스 끝까지 같을 때
            if j == len(pat)-1:
                count += 1
                # 패턴 시작 위치
                idx.append(i - len(pat) + 1)
                j = table[j]
            else:
                j += 1
    return idx

print(KMP('asasvsaasdasadasdaa', 'aa'))