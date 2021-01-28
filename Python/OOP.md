

# OOP

* 객체(Object)
* 객체지향프로그래밍(Object Oriented Programming)
* 클래스(Class)와 객체(Object)
* 인스턴스 & 클래스 변수
* 인스턴스 & 클래스간의 이름공간
* 인스턴스 & 클래스 메서드(+ 스태틱 메서드)



## 객체(Object)

* Python에서 모든 것은 객체(Object)이다.
* 모든 객체는 타입(type), 속성(attribute), 조작법(method)을 가진다.

### 특징

* **타입(type)**: 어떤 연산자(operator)와 조작(method)이 가능한가?
* **속성(attribute)**: 어떤 상태(데이터)를 가지는가?
* **조작법(method)**: 어떤 행위(함수)를 할 수 있는가?



### 타입(Type)과 인스턴스(Instance)

#### 타입(Type)

* 공통된 속성(attribute)과 조작법(method)을 가진 객체들의 분류

#### 인스턴스(Instance)

* 특정 타입(type)의 실제 데이터 예시(instance)이다.
* 파이썬에서 모든 것은 객체이고, **모든 객체는 특정 타입의 인스턴스**이다.

```python
a = 10
b = 200
type(a) is int
```

* True

```python
isinstance(a, int)
```

* True
* a, b는 객체이면서 int type의 이스턴스



### 속성(Attribute)과 메서드(Method)

* 속성은 `.attribue`
* 메서드는 `.method()`

#### 속성(Attribute)

* 객체의 상태 / 데이터

#### 메서드(Method)

* 특정 객체에 적용할 수 있는 행위



## 객체지향프로그래밍(Object Oriented Programming)

* 객체가 중심이 되는 프로그래밍

### Object 중심

* 코드의 직관성
* 활용의 용이성
* 변경의 유연성 - 유지 보수



### 클래스(Class)와 객체(Object)

* `type` : 공통 속성을 가진 객체들의 분류(class)
* `class` : 객체들의 분류(class)를 정의할 때 쓰이는 키워드

#### 클래스(class) 생성

```python
class Person():
    def __init__(self):
        pass
```

#### 인스턴스(Instance) 생성

* 정의된 클래스에 속하는 객체를 해당 클래스의 인스턴스

```python
kim = Person()
```

* `Person()`을 호출함으로써 `Person`클래스의 인스턴스 생성
* `type()`으로 객체의 클래스 확인 가능



#### 메서드(Method) 정의

* 특정 데이터 타입(또는 클래스)의 객체에 공통적으로 적용 가능한 행위
* `self`
  * 인스턴스 자신
  * 인스턴스 메서드 호출 시 첫 번째 인자로 인스턴스 자신이 전달되게 설계
  * 보통 `self`를 첫 번째 인자로 설정

```python
class Person():
    def __init__(self, name):
    	self.name = name
```

* 생성자(constructor) 메서드
  * 인스턴스 객체가 생성될 때 호출 되는 함수
  * `__init__(self)`

* 소멸자(destructor) 메서드
  * 인스턴스 객체가 소멸되기 직전에 호출되는 함수
  * `__del__(self)`



### 속성(Attribute)

* 특정 데이터 타입(또는 클래스)의 객체들이 가지게 될 상태/데이터

```python
class Person():
    def __init__(self, name):
    	self.name = name
  
kim = Person('han')
print(kim.name)
```

* `han` 반환

#### 매직 메서드

- 더블언더스코어(`__`)가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드이기 때문에 `스페셜 메서드` 혹은 `매직 메서드`라고 불린다.
- 매직(스페셜) 메서드 형태: `__someting__`

* `__str__(self)`

  * 특정 객체를 출력할 때 사용할 수 있음

  * ```python
    class Person():
        def __init__(self, name):
        	self.name = name
          
        def __str__(self):
            return '객체 출력중'
       
    kim = Person('han')
    print(kim)
    ```

  * `객체 출력중` 반환



## 인스턴스 & 클래스 변수

### 인스턴스 변수

- 인스턴스의 속성(attribute)
- 각 인스턴스들의 고유한 변수
- 메서드 정의에서 `self.변수명`로 정의
- 인스턴스가 생성된 이후 `인스턴스.변수명`로 접근 및 할당

```python
class Person():
    def __init__(self, name):
    	self.name = name
      
kim = Person('han')
print(kim.name)
```

* `han` 출력



### 클래스 변수

- 클래스의 속성(attribute)
- 모든 인스턴스가 공유
- 클래스 선언 내부에서 정의
- `클래스.변수명`으로 접근 및 할당

```python
class Person():
    po = 0
    def __init__(self, name):
    	self.name = name
      
print(Person.po)
```

* `0` 반환

```python
class Person():
    po = 0
    def __init__(self, name):
    	self.name = name
      	
kim = Person('han')
print(kim.po)
kim.po = 10
print(kim.po)
print(Person.po)
```

* '0'
* `10`
* `0`

* 인스턴스 변수가 없으면, 클래스 변수를 사용



## 인스턴스 & 클래스간의 이름공간

### 이름 공간 탐색 순서

- 클래스를 정의하면, 클래스가 생성됨과 동시에 이름 공간(namespace)이 생성

- 인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성

- 인스턴스의 속성이 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장

- 인스턴스에서 특정한 속성에 접근하게 되면 **인스턴스 => 클래스** 순으로 탐색
- 클래스와 인스턴스는 서로 다른 이름 공간을 가지고 있음



## 메서드의 종류

### 인스턴스 메서드(instance method)

- 인스턴스가 사용할 메서드
- 클래스 내부에 정의되는 메서드의 기본값은 인스턴스 메서드
- 주로 인스턴스 변수를 사용할 때 사용
- **호출시, 첫번째 인자로 인스턴스 자기자신 `self`이 전달됨**

```python
class NewClass():
    def instance_method(self):
        return self
```

* 인스턴스랑 인스턴스 메서드의 self 값은 같음



### 클래스 메서드(class method)

- 클래스가 사용할 메서드
- `@classmethod` 데코레이터를 사용하여 정의
- 주로 클래스 변수를 사용할 때 사용
- **호출시, 첫 번째 인자로 클래스 `cls`가 전달됨**

```python
class NewClass():
    @classmethod
    def class_method(cls):
        return cls
```



### 스태틱 메서드(static method)

- 클래스가 사용할 메서드
- `@staticmethod` 데코레이터를 사용하여 정의
- 주로 데이터를 사용하지 않을 때 사용
- **호출시, 어떠한 인자도 전달되지 않음**

```python
class NewClass():
    @staticmethod
    def static_method(arg):
        return arg
```

* 인스턴스는 스태틱 메서드에 접근 가능



### 인스턴스와 메서드

- 인스턴스는 3가지 메서드 모두에 접근 가능
- 인스턴스에서 클래스 메서드와 스태틱 메서드는 되도록 호출하지 않는다.
- 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계한다.



### 클래스와 메서드

- 클래스 3가지 메서드 모두에 접근 가능
- 클래스에서 인스턴스 메서드는 되도록 호출하지 않는다.
- 클래스가 할 행동은 다음 원칙에 따라 설계한다. (클래스 메서드와 정적 메서드)
  - 클래스 자체(`cls`)와 그 속성에 접근할 필요가 있다면 **클래스 메서드**로 정의한다.
  - 클래스와 클래스 속성에 접근할 필요가 없다면정적 메서드로 정의한다.
    - 정적 메서드는 `cls`, `self`와 같이 묵시적인 첫번째 인자를 받지 않기 때문

```python
class Dog:
    po = 0
    
    def __init__(self, name, breed='강아지'):
        self.name = name
        self.breed = breed
        Dog.po += 1
    
    def bark(self): # 인스턴스 변수를 활용하는 인스턴스 메소드
        print(f'멍멍 {self.name}!!! 나는 {self.breed}')
        
    @staticmethod
    def info():
		# 데이터를 사용하지 않을 때
        print('강아지입니다.')
        
    @classmethod
    def get_po(cls): 
        # 클래스 변수를 사용하는 클래스 메서드
        # self 대신 cls
        print(f'{cls.po}')
    
        
    def __del__(self):
        Dog.population -= 1
```

```python
p = Dog('댕댕이')
Dog.get_po()
```

* 1

```python
Dog.bark(p)
Dog.info()
```

* 멍멍 댕댕이!!! 나는 강아지
* 강아지입니다.

```python
p.bark()
p.get_po()
```

* 멍멍 댕댕이!!! 나는 강아지
* 1

```python
p.info()
```

* 강아지입니다.



## 상속

클래스에서 가장 큰 특징은 `상속`이 가능하다는 것이다.

부모 클래스의 모든 속성이 자식 클래스에게 상속 되므로 재사용성이 높아진다.

```python
class Person:
    po = 0
    
    def __init__(self, name='누구'):
        self.name = name
        Person.po += 1
        
    def hello(self):
        print(f'안녕하세요. {self.name}입니다.')
       
    
class Student(Person):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
```

* 부모 클래스 `Person`
* 자식 클래스 `Student`

```python
kim = Person('김사람')
Person.po
```

* `1` 반환

```python
park = Student('박학생', '200101')
park.student_id
```

* `'200101'` 반환

```python
park.hello()
```

* 안녕하세요 박학생입니다.

```python
Person.population
```

* `1`

```python
Student.population
```

* `1`
* 부모 클래스의 속성, 자식 클래스의 속성 각각

### 상속 관계 확인

* `issubclass(Student, Person)`

* `isinstance(park, Student)`

* `isinstance(park, Person)`

* 모두 `True` 반환



### super()

* 자식 클래스에 메서드를 추가로 구현 가능
* 부모 클래스의 내용을 사용하고자 할 때, `super()`를 사용

```python
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.po += 1
        
    def hello(self):
        print(f'안녕하세요. {self.name}입니다.')

class Student(Person):
    # 학생은 생성할 때, 학번을 추가로 받고 싶어 새로 init
    def __init__(self, name, student_id):
        self.name = name
        Person.po += 1
        self.student_id = student_id
```

* `self.student_id = student_id` 한 줄 때문에 새로 `init`하며 같은 코드를 작성

```python
class Person:
    population = 0
    
    def __init__(self, name):
        self.name = name
        Person.po += 1
        
    def hello(self):
        print(f'안녕하세요. {self.name}입니다.')

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        # 추가 작업
        self.student_id = student_id
```

* `super()`를 통해 추가 작업을 편하게 작성할 수 있다.



## 메소드 오버라이딩

* 자식 클래스에서 부모 클래스의 메서드를 재정의
* 상속 받은 메서드를 재정의 할 수도 있다.
* 상속 받은 클래스에서 같은 이름의 메서드로 덮어쓰기

```python
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.email = email 
        
    def hello(self):
        print(f'안녕하세요, {self.name}입니다.')
```

```python
class Soldier(Person):
    def __init__(self, name, age, number, email, level):
        super().__init__(name, age, number, email)
        self.level = level	# level만 추가
        
    def hello(self):	# 메소드 덮어쓰기
        if self.level == '병장':
            print('집합.')
        else:
            print(f'충성! {self.level} {self.name}입니다.')
           
```

```python
p1 = Person('김학생', 10, '0101234', 'stu@gmail.com')
p1.hello()
```

* 안녕하세요, 김학생입니다.

```python
p2 = Soldier('김이병', 23, '010123', 'sol@gmail.com', '이병')
p2.hello()
```

* 충성! 이병 김이병입니다.

```python
p3 = Soldier('박병장', 25, '010123456', 'sol2@gmail.com', '병장')
p3.hello()
```

* 집합.

  

### 상속 관계에서의 이름 공간

- 기존의 `인스턴스 -> 클래스` 순으로 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 확장된다.
- 인스턴스 -> 클래스 -> 전역
- 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역



### 다중 상속

* 두 개 이상의 클래스를 상속 받는 경우

```python
class Person:
    
    def __init__(self, name):
        self.name = name
        
    def hello(self):
        print('안녕하세요.')
```

```python
class Mom(Person):
    ge = 'XX'
    
    def swim(self):
        print('첨벙첨벙')
```

```python
class Dad(Person):
    ge = 'XY'
    
    def walk(self):
        print('씩씩하게 걷기')
```

```python
mommy = Mom('박엄마')
mommy.swim()
mommy.gene
```

* 첨벙첨벙
* 'XX'

```python
daddy = Dad('김아빠')
daddy.walk()
daddy.gene
```

* 씩씩하게 걷기
* 'XY'

```python
daddy.hello()
```

* 안녕하세요.

```python
daddy.swim()
```

* 에러 발생

```python
class FirstChild(Mom, Dad):
    
    def cry(self):
        print('응애')
        
    def walk(self):
        print('아자아장')
```

```python
baby = FirstChild('김아기')
baby.cry()
```

* 응애

```python
baby.swim()
```

* 첨벙첨벙

```python
baby.walk()
```

* 아장아장
* 자식 클래스에서 메소드가 다시 정의(오버라이딩)

```python
baby.gene
```

* 'XX'
* 앞에 오는 부모 클래스 먼저 접근
* 상속의 순서에 따라