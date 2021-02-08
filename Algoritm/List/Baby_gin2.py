def Baby_gin2(number):
    count = [0] * 10
    run = 0
    triplet = 0
    for i in range(6):
        count[number % 10] += 1
        number = number // 10
    # run 탑색
    for i in range(8):
        if count[i] > 0 and count[i+1] >0 and count[i+2] >0:
            run += 1
            count[i] -= 1
            count[i + 1] -= 1
            count[i + 2] -= 1
        if count[i] >= 3:
            count[i] -= 3
            triplet += 1
    if run + triplet == 2:
        return True
    return False
num = int(input())
print(Baby_gin2(num))