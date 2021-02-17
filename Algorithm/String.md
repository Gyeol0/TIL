# String

## Basic

* Python은 char 타입 없음
* 텍스트 데이터의 취급방법이 통일
* 홑따옴표 또는 쌍따옴표
* 홑따옴표 및 쌍따옴표 3개는 여러 줄의 문자열
* `+`: 문자열 `+` 문자열, 이어주는 역할
* `*` : 문자열`*` 수, 수만큼 문자열 반복
* C는 아스키 코드로 저장, JAVA는 유니코드(UTF16, 2byte)로 저장, 파이썬은 유니코드(UTF8)로 저장

```python
a = '안녕'
print(a*3) #'안녕안녕안녕'

b = '하세요'
print(a+b) #'안녕하세요'
```



## 처리

* 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산 사용 가능
* replace(), split(), isalpha() 등 메소드 사용 가능
* 요소 값 변경 불가(immutable)

```python
string = '안녕하세요'
print(string.replace('세','시')) # '안녕하시요'
# 원본은 변하지 않는다.

print(string.find('녕')) # 1
print(string.index('녕')) # 1

print(string.find('냥')) # -1
print(string.index('냥')) # 에러
```



### 문자열 뒤집기

1. 원본을 뒤집기
   * C에서는 swap을 위한 임시 변수 필요, 문자열 길이의 반만을 수행
   * 파이썬은 .reverse() 또는 s[::-1]로 가능
2. 새로운 빈 문자열을 만들어 뒤에서부터 읽기

```python
string = '안녕하세요'
new_string = ''
for i in string:
    new_string += i
```

### 문자열 비교

* `==` 연산자와 `is` 연산자를 사용
* `==`연산자는 값을 비교
* `is`는 주소, 참조를 비교

### 문자열 숫자를 정수로 변환

* int('123'), float('3.14')
* C에서는 atoi() 사용

```python
def atoi(num_str):
    # 최종 값을 담을 변수
    value = 0
    for i in range(len(num_str)):
        value *= 10
        value += ord(num_str[i]) - ord('0')
       
    return value

num_str = '1234'
num_int = atoi(num_str)
print(num_int, type(num_int)) # 1234 <class: int>
```

### 정수를 문자열 숫자로 변환

*  str(123), repr(123)

* C에서는 itoa() 사용 

```python
def itoa(num):
    num_str = ''
    while num:
        num_str = chr(num % 10 + 48) + num_str
        num //= 10
    return num_str
num = 1234
num_str = itoa(num)
print(num_str, type(num_str)) # 1234 <class 'str'>
```



## 패턴 매칭

### 브루트 포스

```python
def Pattern1(p, t):
    p = 'is' # 찾을 패턴
    t = 'This is a book~!' # 전체 텍스트
    M = len(p)
    N = len(t)
    # i는 텍스트 인덱스, j는 패턴 인덱스
    i = 0
    j = 0
    while j < M and i < N:
        # 틀렸을때
        if t[i] !=p[j]:
            i = i - j # 텍스트 인덱스 다시 제자리로
           	j = -1 # 패턴 인덱스는 다시 처음으로
        # 한 칸 앞으로
        i += 1
        j += 1
	if j == M:
        return i - M # 검색 성공
    else:
        return -1 # 실패
```

### KMP 알고리즘

* 불일치가 발생한 텍스트 문자열의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
* 패턴을 전처리하여 배열 next[M]을 구해서 잘못된 시작을 최소화함
  * next[M] : 불일치가 발생했을 경우 이동할 다음 위치
* 시간 복잡도 : O(M+N)

* 실패 했을 때의 접미사와 패턴의 접두사를 비교

* a  b  c  d  a  b  c  e  f
* -1 0  0  0  0  1  2  3  0
  * 잘랐을 때 접두사와 접미사가 같은 최대 길이
  * ex) 두 번째 c(6)에서 잘랐을 때, 접두사(ab) 접미사(ab)가 최대 길이 2
  * ex2) e에서 잘랐을 때,  접두사(abc) 접미사 (abc)가 최대 길이 3
* e에서 매칭이 실패하면 인덱스 3으로 돌아간다. d의 위치
  * 3개는 접두사와 같기 때문에
* f에서 실패하면 처음으로
* c에서 실패하면 c로

```python
def make_table1(pat):
    # 최대 길이를 저장할 lps, 실패하였을 때 돌아갈 위치
    table = [0] * len(pat)
    # 접두사와 접미사가 같은 최대 길이
    length = 0
    for i in range(1, len(pat)):
        # length가 0보다 크다는 것은 바로 전까지는 일치했기 때문에
        # 다음부터 일치하지 않으므로
        # l을 줄여나가면서 짧게 만들면서 확인
        # 끝가지 접두사와 접미사가 맞는 것이 없으면 0으로 가게됨
        while length > 0 and pat[i] != pat[length]:
            length = table[length-1]

        # 일치할 때에는 최대 길이 1 증가
        if pat[i] == pat[length]:
            length += 1
            table[i] = length
        # 일치하지 않으면 그대로 둠, 모두 0으로 초기화 되어 있어서
    return table
```

* next 배열을 만드는 함수1



```python
def make_table2(pat):
    max_length = 0  # 접두사와 접미사가 같은 최대 길이
    # 최대 길이를 저장할 lps, 실패하였을 때 돌아갈 위치
    table = [0] * len(pat)
    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    # i가 0일 떄에는 -1, 길이가 1이어서 접두사와 접미사가 같다.
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pat[i] == pat[max_length]:
            max_length += 1
            table[i] = max_length
            i += 1
        else:
            # 일치하지 않는 경우
            if max_length != 0:
                # 이전 인덱스에서는 같았으므로 length를 줄여서 다시 검사
                max_length = table[max_length-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 table[i]는 0 이고 i는 1 증가
                table[i] = 0
                i += 1
    return table
```

* next 배열을 만드는 함수2

```python
def KMP(txt, pat):
    table = make_table1(pat)
    # 패턴 인덱스
    j = 0
    count = 0
    idx = []
    # i는 패턴이 시작할 위치를 찾음
    for i in range(len(txt)):
        while j > 0 and txt[i] != pat[j]:
            # 앞으로 이동
            j = table[j-1]
        # 일치 했을 때
        if txt[i] == pat[j]:
            # 패턴 인덱스 끝까지 같을 때
            if j == len(pat)-1:
                count += 1
                # 패턴 시작 위치
                idx.append(i - len(pat) + 1)
                j = table[j]
            else:
                j += 1
    return idx
```

* 텍스트 처음부터 패턴 검색
* KMP 알고리즘
* 패턴 위치 반환



### 보이어-무어 알고리즘

* 오른쪽에서 왼쪽으로 비교
* 대부분 상용 소프트웨어에서 사용
* 패턴에 오른쪽 끝에 있는 문자가 불일치하고 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 패턴의 길이 만큼
  * a b **c** d e f g h
  * p q r
  * c와 r이 다르고 패턴이 c가 없음
  * a b c d e **f** g h
  * .. .. .. p q r
  * 3칸 이동

* 오른쪽 끝에 있는 문자가 불일치 하고 이 문자가 패턴에 존재할 경우
  * 이 문자의 위치를 기준으로 패턴을 위치 시켜서 비교
  * a b c **d** e f g h
  * .. **d** e f
  * 오른쪽 끝에 d가 불일치하지만 패턴에 있음
  * a b c d e **f** g h
  * .. .. .. d e **f**
  * d를 기준으로 이동해서 확인
* 그러나, 최악의 경우에는 브루트 포스와 같아짐 O(MN)
  * a a a a a a a a a a .......
  * b a a a a
  * 찾을때 한 칸씩 이동하면서 비교하여 브루트 포스와 같아짐
* 일반적인 경우에는 O(N+M)보다 짧아진다.