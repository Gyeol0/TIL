# Algoritm

> **무엇이 좋은 알고리즘인가?**

1. 정확성 : 얼마나 정확하게 동작하는가
2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
3. 메모리 사용량 : 얼마나 적은 메모리를 사용하ㅡㄴ가
4. 단순성 : 얼마나 단순한가
5. 최적성 : 더 이상 개선할 여지없이 최적화되었는가



### 시간복잡도

* 알고리즘의 작업량을 표현

* 실제 걸리는 시간을 측정
* 실행되는 명령문의 개수를 계산

* 빅-오(O) 표기법
  * 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
  * 계수는 생략
  * O(4n + 3) = O(4n) = O(n)
  
  

# List



## 정렬

* 버블 정렬
  * O(n2)
* 카운팅 정렬
  * O(n + k)
* 선택 정렬
  * O(n2)
* 퀵 정렬
  * O(n long n) ~ O(n2)
* 삽입 정렬
  * O(n2)
* 병합 정렬
  * O(n log n)

### 버블 정렬(Bubble Sort)

* 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
* 과정
  * 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
  * 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
* 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양 같다고 하여 버블 정렬
* O(n2)

```python
def BubbleSort(arr):
    for i in range(len(arr)-1, 0 ,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```



### 카운팅 정렬(Counting Sort)

* 항목들의 순서를 결저아기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
* 각 항목 앞에 위치할 항목의 개수를 반영하기 위해 누적 합으로 count 원소 조정
* counts[i]를 1 감소시키고 temp[count[i]-1]에 i 삽입
* **제한사항**
  * 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
  * 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
* 시간 복잡도
  * O(n + k) 

```python
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
```



## 완전 탐색(Exhaustive Search)

* 완전 탐색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법이다.
* Brute-force 혹은 Generate-and-Test 기법이라고도 불리운다.
* 모든 경우의 수를 테스트한 후, 최종 해법을 도출
* 경우의 수가 상대적으로 작을 때 유용
* 우선 완전 탐색으로 접근하고, 다른 알고리즘을 사용하며 성능 개선

### 순열(Permutation)

* 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것

```python
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
```

* 가장 쉬운 방법
* 단점
  * 중복한 수가 있을 경우에는 사용이 불가능
  * 특정 원소의 개수만을 사용





### Baby-gin Game

* 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
* 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다.
* 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.
* 완전 탐색 순열 또는 greedy를 통해 구현

```python
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
```

* itertools 사용







## 탐욕 알고리즘(Greedy)

* 최적해를 구하는 데 사용되는 근시안적인 방법
* 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택
* 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 전체의 최적이라는 보장은 없다.
* 일반적으로, 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근

1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분 해집합에 추가
2. 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지를 확인, 문제를 위반하지 않는지
3. 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지 확인, 아니라면 1부터 다시

### 거스름돈 줄이기

1. 해 선택 : 단위가 큰 동전으로 만들면 개수가 줄어들므로, 가장 단위가 큰 동전을 하나 골라 거스름돈에 추가
2. 실행 가능성 검사 : 거스름돈이 액수를 초과하는지 확인, 초과하면 마지막 동전을 빼고 1로 돌아감
3. 해 검사 : 거스름돈이 액수와 일치해야 하므로 부족하면 1로 돌아감

* 그러나 400원 짜리 동전이 있다면 배수 관계가 아니기 때문에 불가능



### Baby_gin

```python
def Baby_gin2(number):
    count = [0] * 10
    run = 0
    triplet = 0
    # 자리수의 count 리스트를 만들어서 3 이상이면 triplet, 연속해서 1 이상이면 run
    for i in range(6):
        count[number % 10] += 1
        number = number // 10

    for i in range(8):
        # run 탐색
        if count[i] > 0 and count[i+1] >0 and count[i+2] >0:
            run += 1
            count[i] -= 1
            count[i + 1] -= 1
            count[i + 2] -= 1
            
        # triplet 탐색
        if count[i] >= 3:
            count[i] -= 3
            triplet += 1
    if run + triplet == 2:
        return True
    return False
num = int(input())
print(Baby_gin2(num))
```





## 실습 1

* 상자들이 쌓여있는 방이 있다.
* 방이 오른쪽으로 90도 회전하여 상자들이 낙하한다고 할 때, 낙차가 큰 상자를 구하라.

* 중력은 회전한 후에 적용

```python
def gravity(N, lst):
    max_height = 0
    for i in range(N-1):
        count = 0
        # 밑에 있는 상자들 중에서 자신보다 높은 상자 count
        for j in range(i+1, N):
            if lst[i] <= lst[j]:
                count += 1
        # 오른쪽으로 회전하였을 때 현재 높이 - 자신보다 높거나 같은 상자 count
        if max_height < N - (i+1) - count:
            max_height = N - (i+1) - count
    return max_height
N = int(input())
height = list(map(int, input().split()))
print(gravity(N, height))
```

문제 출처 :  https://swexpertacademy.com/main/main.do

## 실습 2

* 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.

* 빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

```python
def view(N, building):
    answer = 0
    for j in range(2, N-2):
        # 전방과 후방 view 확인, 모두 현재 빌딩보다 낮아야 한다.
        if building[j] > building[j+1] and building[j] > building[j+2] and building[j] > building[j-1] and building[j] > building[j-2]:
            max_height = 0
            # 전방, 후방에서 가장 높은 빌딩 높이
            for i in range(j-2, j+3):
                if i != j:
                    if max_height < building[i]:
                        max_height = building[i]
            # 확보된 조망권
            answer += building[j] - max_height
    return answer

for i in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    print(f'#{i}',view(N, building))
```

문제 출처 : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh



## 탐색

### 지그재그 순회

```python
for i in range(N):
    for j in range(M):
        arr[i][j + (M-1-2*j) * (i % 2)]
       	# 연산 수행ㄴ
```

### 상하좌우 탐색

```python
dx = [1, -1, 0, 0]
dy = [0, ,0 1, -1]
for i in range(4):
    ax = x + dx
    ay = y + dy
```

```python
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(4):
    ax = x + dxy[i][0]
    ay = y + dxy[i][1]
```



#### 연습 문제

> 인접한 요소와의 차이의 절댓값의 총합을 구하시오.

```python
# 인접한 요소와의 차의 절댓값의 총합
def Sum_Abs(N, M ,arr):
    abs_sum = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            for k i n range(4):
                ax = arr[i][j] + dx[k]
                ay = arr[i][j] + dy[k]
                if ax >= 0 and ax < N and ay >=0 and ay <M:
                    abs_sum += abs(arr[i][j] - arr[ax][ay])
    return abs_sum
```



### 비트 연산자

* **&** : 비트 단위로 AND 연산
* **|** :  비트 단위로 OR 연산
* **<<** : 피연산자의 비트 열을 왼쪽으로 이동
  * 1<<n : 2의 n제곱, 원소가 n개일 경우으 모든 부분 집합의 수를 의미
  * i & (1<<j) : i의 j번째 비트가 1인지 아닌지를 리턴
* **>>** : 피연산자의 비트 열을 오른쪽으로 이동



> 부분 집합을 생성

```python
arr = [1,2,3,4]
n = len(arr)
for i in range(1<<n):
    for j in rnage(n):
        if i & (1<<j):
            print(arr[j], end=", ")
    print()
print()
```



#### 연습 문제

> 정수 집합을 입력 받아서 합이 0인 부분 집합 반환

```python
def Sum_Subset():
    arr = list(map(int, input().split()))
    N = len(arr)
    result = []
    for i in range(1<<N):
        subset = []
        sum_sub = 0
        for j in range(N):
            if i & (1<<j):
                subset.append(arr[j])
        for j in subset:
            sum_sub += j
        if sum_sub == 0:
            result.append(subset)
    return result
```



