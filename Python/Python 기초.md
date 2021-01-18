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

    * 에러(invalid syntax)

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

  * 변수의 개수와 동일한 개수의 데이터를 할당해야 한다.
  
    * ```python
      a,b = 1
      ```
  
    * 에러(cannot unpack non-iterable int object)

#### swap

```python
# 임시 변수 활용
x = 1
y = 20
tmp = x
x = y
y = tmp
```

```python
x = 1
y = 20
x,y = y,x
```

* 같은 결과

#### 식별자

* 변수, 함수, 클래스 등을 식별하는데 사용되는 이름(name)
* 영문알파벳(대문자와 소문자), 밑줄(_), 숫자로 구성
* 대소문자 구별
* 첫 글자에는 숫자 불가
* `True` `as` `try` 등의 키워드 사용 불가
* 되도록 내장함수나 모듈의 이름으로 만들지 않는다.

### 데이터 타입

* Number

* String

* Boolean

  #### Number

  * `int`

    * `long`타입 없이 모두 `int`로 표기

    * ```python
      binary_number = 0b10
      octal_number = 0o10
      decimal_number = 10
      hexadecimal_number = 0x10
      print(f"""
      2진수 : {binary_number}
      8진수 : {octal_number}
      10진수 : {decimal_number}
      16진수 : {hexadecimal_number}
      """)
      ```

  * `float`

    * 실수

    * 부동소수점을 사용하여 항상 같은 값으로 일치되지 않는다.

    * ```python
      a = 3.5 - 3.12 # 0.3799999999999999
      b = 0.38
      a == b # False
      ```

  * 복소수(complex)

    * 실수부와 허수부
    * 쓸 일이 없을 것 같다!
    * 허수부는 j로 표현

  #### String

  * 주로 `'`나  `"`를 사용
  * 둘중 하나로 통일해라, 섞어서 쓰지 마라
  * 

  

