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



## 구현

### 선형 큐

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
  * 선형큐