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