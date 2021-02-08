# arr1 : 입력
# arr2 : 정렬할 배열
# k : 최댓값
def Counting_Sort(arr1, arr2, k):
    count = [0] * (k+1)
    # 원소별 counting
    for i in range(len(arr2)):
        count[arr1[i]] += 1
    # 누적합으로 변환
    for i in range(1, len(count)):
        count[i] += count[i-1]
    # 자리에 맞는 값을 1씩 감소하면서 대입
    for i in range(len(arr2)-1, -1, -1):
        arr2[count[arr1[i]]-1] = arr1[i]
        count[arr1[i]] -= 1

    return arr2
print(Counting_Sort([5,2,1,3,2], [5,2,1,3,2], 5))
