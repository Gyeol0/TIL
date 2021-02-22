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



