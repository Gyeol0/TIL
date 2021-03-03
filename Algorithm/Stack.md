# Stack

## 특성

* 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
* 스택에 저자왼 자료는 선형 구조를 갖는다
  * 선형구조 : 자료 간의 관계가 1대 1의 관계를 갖는다.
  * 비선형구조 : 자료 간의 관계가 1대 N의 관계를 갖는다.(ex 트리)
* 자료 삽입, 꺼내기 가능
* 마지막 삽입 자료를 먼저 꺼낸다. 후입 선출(LIFO, Last-In-First-Out)



## 구현

* 구현하기 위해 필요한 자료구조와 연산

  * 자료구조 : 자료를 선형으로 저장할 저장소

    * C언어에서는 배열 사용 가능
    * 저장소 자체를 스택이라 부르기도 한다.
    * 스택에서 마지막 삽인된 원소의 위치를 top이라 부른다.
    * 파이썬에서는 List 사용 가능

  * 연산

    * 삽입 : 저장소에 자료를 저장. push

      * 보통은 스택의 크기가 정해져 있지만, 파이썬 리스트는 크기가 가변적

      ```python
      def push(item):
          s.append(item)
      ```

    * 삭제 : 저장소에서 자료를 꺼낸다. pop

      ```python
      def pop():
          if len(s) == 0:
              # underflow
              return
         	else:
              return s.pop(-1)
      ```

      

    * 스택이 공백인지 아닌지 확인. isEmpty

    * 스택의 top에 있는 item(원소)를 반환. peek



### 고려 사항

* 1차원 배열을 사용하여 구현할 경우, 구현이 용이하지만 스택의 크기를 변경하기가 어렵다
  * 리스트 사용해도 가능
* 이를 해결하기 위해 저장소를 동적으로 할당하여 스택을 구현
  * 동적 링크드리스트를 이용
  * 구현이 복잡하지만 메모리를 효율적 사용



### 예제 1 : 괄호검사

* 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
* 같은 괄호에서 왼쪽 괄호는 오른쪽괄호보다 먼저 나와야한다.
* 괄호 사이에는 포함 관계만 존재한다.
* 풀이
  1. 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 삽입, 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제 후 짝이 맞는지 확인
  2. 스택에 비어 있으면 조건 1, 조건 2에 위배, 괄호의 짝이 맞지 않으면 조건 3에 위배
  3. 마지막 괄호까지를 조사한 후에도 스택에 괄호가 남아 있으면 조건 1에 위배

```python
def Parentheses(arr):
    stack = []
    for i in arr:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            s = stack.pop()
            if i == ')':
                if s != '(':
                    return False
            elif i == '}':
                if s != '{':
                    return False
            elif i == ']':
                if s != ']':
                    return False
    if stack:
        return False
    else:
        return True
print(Parentheses('((({})))'))
```



### 예제 2: function call

* **Function call**
  * 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
    * 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조
    * 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임(stack frame)에 저장하여 시스템 스택에 삽입
    * 함수 실행 후, 시스템 스택 top 삭제, 프레임에 저장된 복귀 주소로 복귀
    * 함수 호출과 복귀에 따라 과정 반복
    * 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택

```python
def func2():
    print('함수 2 시작')
    print('함수 2 종료')

def func1():
    print('함수 1 시작')
    func2()
    print('함수 1 종료')

print('메인시작')
func1()
print('메인끝')
```



### 재귀 호출

* 자기 자신을 호출하여 순환 수행
* 프로그램 크기를 줄이고 간단하게 작성
* 중복 호출이 일어날 수 있음

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
```

```python
def fibo(b):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```



### Memoization

* 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록
* 동적 계획법(DP)의 핵심

```python
memo = [0, 1]

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo1(n-2))
    return memo[n]
```

```python
memo = [-1] * n

def fibo2(n):
    global memo
    if memo[n] == -1:
        memo[n] = fibo2(n-1) + fibo2(n-2)
    return memo[n]
```



### DP(Dynamic Programming)

* 동적 계획 알고리즘은그리디 알고리즘과 같이 **최적화 문제**를 해결하는 알고리즘
* 입력 크키가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입렵의 문제를 해결하는 알고리즘

```python
def fibo2(n):
    f = [0, 1]
    
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    
    return f
```



### DFS(깊이우선탐색)

* 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색이 중요
  * 깊이 우선 탐색(depth First Search, DFS)
  * 너비 우선 탐색(Breadth First Search, BFS)
* 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색, 갈 곳이 없게 되면 마지막 갈림길 정점으로 되돌아와서 탐색을 반복하여 모든 정점을 반복하는 순회방법
* 스택 사용
* 순서
  1. 시작 정점 v를 결정하여 방문
  2. 정점 v에 인접한 정점 중
     1. 방문하지 않은 정점 w가 잇으면, 정점 v를 스택에 push, 정점 w 방문, w를 v로 하여 다시 반복
     2. 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해 스택을 pop하여 가장 마지막 방문 정점을 v로 하여 다시 반복
  3. 스택이 공백이 될 때까지 2 반복

```python
def dfs(graph, start, end):
    visit = []
    stack = [start]
    while stack:
        s = stack.pop()
        # 경로중 end를 만나면 종료
        if s == end:
            return 1
        # 방문하지 않았고 갈 수 있으면 stack에 추가
        if s not in visit and s in graph:
            visit.append(s)
            stack += graph[s]
    return 0

T = int(input())
for test in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for i in range(E):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
    start, end = map(int, input().split())
    print(f'#{test}',Graph_Route(graph, start, end))
```

* 딕셔너리 graph말고 2차원 인접 리스트로도 표현 가능



### 계산기

* 문자열로 된 계산식이 주어질 때

  1. 중위 표기법의 수식을 후위 표기법으로 변경(스택), A+B
     1. 피연산자이면 출력
     2. 연산지이면, 스택 top 연산자보다 우선순위가 높으면 스택에 push, 아니면 조건을 만족할 때까지 pop한 후 push, top이 연산자가 아니면 push
     3. ')'이면 스택 top에 왼쪽 괄호가 나올 때까지 pop, '('가 나오면 버림
     4. 중위 표기식 반복
     5. 스택에 남아 있으면 모두 pop
        * 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높음
        * 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮음

  ```python
  def Postfix_Notation(expression): # 후위 표기법
      stack = []
      result = []
      priority_in = {
          '(': 0,
          '+': 1,
          '-': 1,
          '*': 2,
          '/': 2,
          ')': '-'
      }
      priority_out = {
          '(': 3,
          '+': 1,
          '-': 1,
          '*': 2,
          '/': 2,
          ')': '-'
      }
  
      for i in expression:
          # 피연산자는 push
          if i not in priority_in:
              result.append(int(i))
          else:   # 연산자
  
              # 스택이 있을 때
              if stack:
                  # 닫는 괄호면 여는 괄호가 나올 때까지 pop
                  if i == ')':
                      while stack[-1] != '(':
                          result.append(stack.pop())
                      stack.pop()
                  else:
                      # top보다 우선순위가 클 때까지 pop
                      while stack:
                          if priority_in[stack[-1]] < priority_out[i]:
                              stack.append(i)
                              break
                          else:
                              result.append(stack.pop())
                      # 스택 비어지면 push
                      if not stack:
                          stack.append(i)
              else:   # 스택이 비었을 때
                  stack.append(i)
      # 스택에 남아있을 때 모두 pop
      while stack:
          result.append(stack.pop())
      return result
  ```

  

  2. 후위 표기법의 수식을 스택을 이용하여 계산, AB+
     1. 피연산자면 스택에 push
     2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산, 연산 결과를 스택에 push
     3. 수식이 끝나면 마지막으로 스택을 pop하여 출력

  ```python
  def calculator(expression):
      stack = []
      symbol = ['+', '-', '*', '/']
      for i in expression:
          # 피연산자는 스택에 push
          if i not in symbol:
              stack.append(i)
          else:
              # 연산자는 뒤에서부터 2개 계산해서 push
              a = stack.pop()
              b = stack.pop()
              if i == '+':
                  stack.append(b + a)
              elif i == '-':
                  stack.append(b - a)
              elif i == '*':
                  stack.append(b * a)
              elif i == '/':
                  stack.append(b / a)
      result = stack.pop()
      return result
  ```



### 백트래킹

* 백트래킹(Backtracking) 기법은 해를 찾는 도중에 **막히면**(즉, 해가 아니면) 되돌아가서 다시 해를 찾아가는 기법

* 최적화(optimization) 문제와 결정(decision) 문제를 해결할 수 있다.
* 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'로 답하는 문제
  * 미로 찾기
  * n-Queen 문제
  * Map coloring
  * 부분 집합의 합(Subset Sum) 문제 등
* DFS와의 차이
  * 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임(Prunning 가지치기)
  * 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
  * 깊이 우선탐색을 하기에는 경우의 수가 너무나 많음. N! 가지의 경우의 수를 가진 문제에 대해 깊으우선탐색을 가하면 당연히 처리 불가능
  * 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponentital Time)을 요하므로 처리 불가능
* 어떤 노드의 유망성을 점검한 후에 유망(promsing)하지 않다고 결정되면 그 노드의 부모의 다음 자식 노드로
* 어떠한 노드를 방문하였을 때, 그 노드를 포함한 경로가 답이 될 수 없으면 그 노드는 유망하지 않음.
* 가지치기(pruning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.
* 절차
  1. 상태 공간 트리의 DFS 실시
  2. 각 노드가 유망한지 점검
  3. 유망하지 않으면 부모 노드로 돌아가서 반복

#### powerset

* 어떤 집합의 공집합과 자기자신을 포하만 모든 부분집합을 powerset이라 한다.
* 2의 n승

```python
def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES # Yes or No
    
    if k == input: # 원하는 개수 만큼 뽑았는지
        process_solution(a, k) # 답이며 원하는 작업을 한다. 출력을 하던지 더하던지
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c) # 후보군 만들기(2)
        for i in range(ncandidates):
            a[k] = c[i] # ncandidates = 2, i가 0일 떄는 c[i] = True, 1일때는 c[i] = False
            # a[k]에 True로 한 번, False로 한 번해서 backtrack(a, k, input) 실행
            backtrack(a, k, input)
            
MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX #check, 이 원소를 사용했는지, 임의로 100개
backtrack(a, 0, 3) # 0은 a라는 원소의 index, 3은 몇 개 뽑을지
```

```python
N = 3
arr = [1, 2, 3]
sel = [0] * N

def powerset(idx):
    if idx == N:
        print(*sel) # 비트로 출력됨 [1, 0, 0], [0, 1, 0], .....위치를 찍은 것
        return
    
    # idx 자리의 원소를 뽑고 간다.
    sel[idx] = 0
    powerset(idx + 1)
    
    # idx 자리의 원소를 안뽑고 간다.
    sel[idx] = 1
    powerset(idx + 1)
    
    # ncandidates, a[k] = c[i] 와 같음
    
powerset(0)
```



#### 순열

* powerset과 매우 유사함

```python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        for i in range(1, k+1): # k개 출력
            print(a[i], end = ' ')
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a,k,input, c)
        # 사용하지 않은 개수만큼 반복해서 backtrack
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a,k,input)

def construct_candidates(a, k, input,c):
    in_perm = [False] * NMAX
    # 사용한 값 표시
    for i in range(1, k):
        in_perm[a[i]] = True

    ncandidates = 0
    # 0번 인덱스는 사용 x
    # 사용하지 않은 값 개수 계산
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

MAXCANDIDATES = 3
NMAX = 3
```

```python
arr = [1,2,3]
N = 3
sel =[0] * N
check = [0] * N

def perm(idx):
    # 다 뽑아서 정리했다면
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]  # 값을 써라, 값을 덮어쓰기 때문에 원상복구 안해도 됨
                check[i] = 1  # 사용했다는 표시
                perm(idx+1)
                check[i] = 0  # 다음 반복문을 위한 원상복구
perm(0)
```



### 분할 정복

* 분할(Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
* 정복(Conquer) : 나눈 작은 문제를 각각 해결한다.
* 통합(Combine) : (필요하다면) 해결된 해답을 모은다.

#### 거듭제곱

```python
def Power(Base, Exponent): # O(log N)
    if Exponent == 0 or Base == 0:
        return 1
    if Exponent % 2 == 0:
        # ex) 2의 10승은 2의 5승의 제곱
        NewBase = Power(Base, Exponent//2)
        return NewBase * NewBase
    else:
        NewBase = Power(Base, (Exponent-1) //2)
        return (NewBase * NewBase) * Base
print(Power(2, 10))  # 1024
```



#### 퀵정렬

* 주어진 배열을 두 개로 분할하고, 각각을 정렬
* 합병정렬은 그냥 두 부분으로 나누는 반면, 퀵정렬은 분할할 때, 기준 아이템(pivot item) 중심으로 이것보다 작은 것은 왼쪽, 큰 것은 오른쪽에 위치
* 각 부분 정렬이 끝난 후, 합병정렬은 "합병(merge)"이란 후처리 작업 필요, 퀵정렬은 없음.

```python
def partition(arr, start, end):
    pivot = (start + end) // 2
    L = start
    R = end
    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1
        while arr[R] >= arr[pivot] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            Arr[L], arr[R] = arr[R], arr[L]
    arr[pivot], arr[R] = arr[R], arr[pivot]
    return R
```

* [69, 10, 30, 2, 16, 8, 31, 22], L = 69, R = 22, pivot = 2
* L이 오른쪽으로 이동하면서 피봇보다 크거나 같은 원소를 찾고, R은 왼쪽으로 이동하면서 피봇보다 작은 원소를 찾는다.
* R이 pivot보다 작은 원소를 찾지 못했으므로 69에서 L과 만난다.
* L과 R이 만났으므로, 69를 pivot을 교환하고 2의 위치 확정, 2, [10, 30, 69, 16, 8, 31, 22]
* pivot 2의 왼쪽 부분 집합은 공집합, 퀵정렬 수행x
  * 오른쪽 부분 집합에 대해서 퀵정렬 수행
  * 오른쪽 부분집합 원소 7개, pivot = 16, L = 10, R = 22
  * L = 30, R = 8 서로 교환 2, [10, 8, 69, 16, 30, 31, 22]
  * 69에서 L과 R이 같아짐 2, [10, 8], 16, [69, 30, 31, 22]
* [10, 8]에서 L = 10, pivot = 10, R = 8
  * L과 R을 교환하는데, L이 pivot이므로 교환한 자리를 pivot 위치로 확정
  * 2, [8], 10, 16, [69, 30, 31, 22]
  * 왼쪽 부분집합은 원소가 한 개이므로 퀵정렬 수행x
* [69, 30, 31, 22], L = 69, R = 22, pivot = 30
  * 69, 22 교환
  * [22, 30, 31, 69]
  * pivot에서 L과 R이 만남
  * [22], 30, [31, 69], pivot 위치 확정
  * 왼쪽 원소 1개 확정
* [31, 69], L = 31, R = 69, pivot = 31
  * 31에서 L과 R이 만남
  * pivot 위치 확정
  * 31, [69], 오른쪽 원소 1개 확정
* 결과 : 2, 8, 19, 16, 22, 30, 31, 69
* 최악의 경우 O(n2)
* 평균 nlogn