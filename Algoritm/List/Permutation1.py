def Permutation_1(arr):
    answer = []
    for i in arr:
        for j in arr:
            if i !=j:
                for k in arr:
                    if i != k and j != k:
                        answer.append((i, j, k))
    return answer
print(Permutation_1([1, 2, 3]))