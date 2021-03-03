# Queue

## 특성

* 스택과 같이 삽입과 삭제의 위치가 제한적인 자료구조
  * 큐는 뒤에서는 삽입, 앞에서 삭제
* 선입선출구조(FIFO : First In First Out)
  * 삽입한 순서대로 저장하고 가장 먼저 삽입된 원소가 가장 먼저 삭제
* 머리 : Front, 꼬리 : Rear



## 구조 및 연산

### 기본 연산

* enQueue : 삽입 
* deQueue  : 삭제
* createQueue : 공백 상태의 큐 생성
* isEmpty : 공백상태인지 확인
* isFull : 포화상태인지 확인
* Qpeek : front에서 원소를 삭제 없이 반환



## 연산 과정

1. 큐 생성
   * front = rear = -1
2. 원소 A 삽입
   * [A]
   * front = -1
   * rear = 0
3. 원소 B 삽입
   * [A, B]
   * front = -1
   * rear = 1
4. 원소 반환, 삭제
   * front += 1
   * rear = 1
   * 인덱스 0 위치 삭제 및 반환(A)
5. 원소 C 삽입
   * front = 0
   * rear = 2
6. 원소 반환, 삭제
   * front += 1
   * rear = 2
   * 인덱스 1 위치 삭제 및 반환(B)
7. 원소 반환, 삭제
   * front += 1
   * rear = 2
   * 인덱스 2 위치 삭제 및 반환(C)



## 선형 큐

### 구현

* 1차원 배열을 이용한 큐
  * 큐의 크기 = 배열의 크기
  * front : 저장된 첫 번째 원소의 인덱스
  * rear : 저장된 마지막 원소의 인덱스
* 상태 표현
  * 초기 상태 : front = rear = -1
  * 공백 상태 : front = rear
  * 포화 상태 : rear = n-1

### 삽입 구현

```python
def enQueue(item):
    global rear
    if isFull():
        print("Queue_Ful")
    else:
        rear = rear + 1
        Q[rear] = item
```

### 삭제 구현

```python
def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = front + 1
        return Q[front]
```

### 공백 및 포화상태 검사

```python
def isEmpty():
    return front == rear

def isFull():
    return rear == len(Q) - 1
```

### 검색 구현

```python
def Qpeek():
    if isEmpty():
        print("Queue_Empty")
    else:
        return Q[front + 1] # front를 일시적으로 증가(삭제와 차이)
```



## 원형 큐

### 선형 큐 이용시 문제점

* 잘못된 포화상태 인식
  * 선형 큐를 이용하여 삽입, 삭제를 계속할 경우, 배여르이 앞부분에 활용할 수 있는 공간이 있음에도, rear = n-1인 상태
  * 즉, 포화 상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨

### 해결 방법 1

* 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동
* 원소 이동에 많은 시간 소요, 큐의 효율성 급격히 떨어짐

### 해결 방법 2

* 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용

### 구조

* 초기 공백 상태 : front = rear = 0
* Index의 순환
  * front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야함
  * 이를 위해 나머지 연산자 mod를 사용
* front
  * 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
* 삽입 및 삭제 위치
  * 선형 큐 : rear = rear + 1
  * 원형 큐 : rear = (rear + 1) mod n
  * 선형 큐 : front = front + 1
  * 원형 큐 : front = (front + 1) mod n

### 구현

* 초기 공백 큐 생성
  * 크기 n 1차원 배열 생성
  * front = rear = 0
  * 선형 큐는 -1

### 공백 상태 및 포화 상태 검사

```python
def isEmpty():
    return front == rear

def isFull():
    return ((rear+1) % len(cQ)) == front
```

### 삽입 구현

```python
def enQueue(item):
    global rear
    if isFull():
        print("Queue_Ful")
    else:
        rear = (rear + 1) % len(cQ)
        Q[rear] = item
```

### 삭제 구현

```python
def deQueue():
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front + 1) % len(cQ)
        return Q[front]
```



## 연결 큐

* 단순 연결 리스트(Linked List)를 이용한 큐
  * 큐의 원소 : 단순 연결 리스트의 노드
  * 큐의 원소 순서 : 노드의 연결 순서. 링크로 연결되어 있음
  * front : 첫 번째 노드를 가리키는 링크
  * rear : 마지막 노드를 가리키는 링크
* 초기 상태 : front = rear = None
* 공백 상태 : front = rear = None
* 공간 활용이 좋다.

### 연산 과정

1. 공백 큐 생성
   * front = rear = None
2. 원소 A 삽입
   * front = rear = 원소 A를 가리키는 링크
3. 원소 B 삽입
   * front = 원소 A를 가리키는 링크
   * rear = 원소 B를 가리키는 링크
4. 원소 삭제
   * front = 원소 B를 가리키는 링크
   * rear = 원소 B를 가리키는 링크
5. 원소 C 삽입
   * front = 원소 B를 가리키는 링크
   * rear = 원소 C를 가리키는 링크
6. 원소 삭제
   * front = 원소 C를 가리키는 링크
   * rear = 원소 C를 가리키는 링크
7. 원소 삭제
   * front = rear = None



## 우선순위 큐(Priority Queue)

### 특성

* 우선순위를 가진 항목들을 저장하는 큐
* FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나간다.

### 적용 분야

* 시뮬레이션 시스템
* 네트워크 트래픽 제어
* 운영체제의 테스크 스케줄링

### 구현

* 배열을 이용
  * 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
  * 가장 앞에 최고 우선순위의 원소가 위치
  * 문제점 - 배열을 사용하여, 삽입이나 삭제 연산이 일어날 때 원소 재배치 발생 -> 소요되는 시간이나 메모리 낭비가 크다.

* 리스트를 이용

### 연산

* 삽입 : 맨 마지막에 삽입
* 삭제 : 우선순위가 높은 원소를 삭제



## 버퍼(Buffer)

* 큐 활용
* 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
* 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미
* ex) 키보드, 입력 받은 순으로 전달 및 출력

### 자료 구조

* 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
* 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 큐 활용



## BFS(Breadth First Search)

* 너비 우선 탐색
* 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문
* 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비 우선 탐색을 진행하야 하므로, 선입선출 형태의 큐 활용

```python
def BFS(G, V): # 그래프 G, 탐색 시작점 V
    visited = [0] * n # n : 정점의 개수
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0) # front 반환
        if not visited[t]: # 방문허자 얺은 곳이면
            visited[t] = True # 방문
        for i in G[t]: # t와 연결된 모든 선에 대해
            if not visited[i]:
                queue.append(i) # 방문하지 않은 곳이면 큐에 넣기
```

