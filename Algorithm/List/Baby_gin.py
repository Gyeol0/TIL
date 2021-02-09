from itertools import permutations
# itertools 사용
def Baby_gin(number):
    number = list(map(int, number))
    case = list(permutations(number))
    for i in case:
        run = 0
        triplet = 0
        # 앞의 3개 run, triplet 탐색
        if i[0] == i[1] and i[1] == i[2]:
            triplet += 1
        elif i[0] - i[1] == i[1] - i[2]:
            run += 1
        # 두의 3개 run, triplet 탐색
        if i[3] == i[4] and i[1] == i[5]:
            triplet += 1
        elif i[3] - i[4] == i[4] - i[5]:
            run += 1
        if run + triplet == 2:
            return True
    return False
num = input()
print(Baby_gin(num))