# Python 기초

## Syntax

### 주석(Comment)

* `#`한 줄 주석

* 여러 줄 주석

  1. 한 줄씩 `#`사용
  2. `'''`또는 `"""` 사용

* ```python
  # 한 줄 주석
  '''여러 줄
  주석
  여러 줄
  '''
  ```

### 코드 라인

* 파이썬에서는 `;`을 작성하지 않는다.

* 한 줄로 표기할 때는 `;` 작성이 가능하다.

* 출력

  * print(변수)
  * print('문자')

* 코드 1줄에 1문장을 원칙으로 한다.

  * ```python
    print('hello')print('hi')
    ```

    * 오류(invalid syntax)

  * ```python
    print('hello');print('hi')
    ```

    * 출력

## 변수(Variable)

* 할당 연산자 `=`을 통해서 변수를 할당

* type()을 통해서 데이터 타입 확인 가능

  * ```python
    a = 10
    type(a)
    ```

  * int

* id()를 통해서 메모리 주소 확인 가능

* 동시에 할당 가능

  * ```python
    a,b, = 1, 4
    x,y,z = 1,2,3
    p = q = 10
    ```

  * 

