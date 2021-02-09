# 절댓값이 100000000 이하인 정수 리스트의 최댓값을 구하시오.
def search_max(numbers):
    max_num = -100000000
    for i in numbers:
        if max_num < i:
            max_num = i
    return max_num
num = list(map(int, input().split()))
print(search_max(num))