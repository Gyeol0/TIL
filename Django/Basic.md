# Basic

* **django**
* Dynamic Web을 만들어주는 프레임 워크
* 요청(requests)이 오면 응답(response)을 보내주는 Server 제작
* 기본적인 구조나 필요한 코드 제공

## how

* 파이썬으로 작성된 오픈 소스 웹 어플리케이션 프레임워크로, **모델-뷰-컨트롤러 모델 패턴**을 따르고 있다.
* 모델-뷰-컨트롤러(Model-View-Controller, MVC)는 소프트웨어 공학에서 사용되는 **소프트웨어 디자인 패턴**
* django는 Model-Template-View, MTV
* Model은 데이터베이스 관리
* Template는 레이아웃(화면)
* View는 중심 컨트롤러(심장)

![basic-django](img/basic-django.png)

* **urls.py**, **models.py**, **views.py** 중요!!(3대장)

## 명령어

* `django-admin startproject 프로젝트 이름`으로 django 생성
* `python manage.py runserver` 서버 작동(활성화)

* `python manage.py startapp 앱 이름` 앱 start
  * 새로운 앱 폴더 생성
  * 프로젝트 폴더와 동일 선상에 생성
  * **settings.py**의 INSTALLED_APPS 수정해야함
  * 앱 order 순서
    1. local apps
    2. 3rd-party apps
    3. django apps(기본)

## Setting

* `LANGUAGE_CODE = 'ko-kr'`
  * 한국어로 번역
  * 'en-us'가 기본
* TIME_ZONE = 'Asia/Seoul'
  * 시간
  * UTC가 기본

## urls.py

* django는 admin 페이지를 기본으로 제공
* 서버 주소/admin
* path('페이지/', 호출할 함수)

```python
from articles import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```



## views.py

* view 함수의 첫 번째 인자는 반드시 request
* render 함수의 첫 번째 인자는 반드시 request

```python
def index(request): # 첫 번째 인자는 반드시 request
    return render(request, '템플릿경로') # render 함수의 첫 번째 인자는 반드시 request
```



## templates

* 데이터 표현을 제어하는 도구이자 표현에 관련된 로직

### DTL

* Django template language(DTL)
* django template에서 사용하는 built-in template system
* python 문법 구조와 비슷

### Syntax

* **variable**
  * {{ variable }} 변수는 중괄호 2개로 감싸서 사용
* render()를 사용하여 views.py에서 정의한 변수를 templates 파일로 넘겨서 사용
* 변수명 영어, 숫자, 밑줄 사용 가능, 밑줄로 시작은 불가능
* dot(.)를 사용하여 변수 속성에 접근 가능
* render()의 세 번째 인자로 {'key' : value} 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨.
* **Filters**
  * {{variable|filter}}
  * 표시할 변수를 수정할 때 사용
  * ex)
    * {{name|lower}}
    * name 변수를 모두 소문자로 출력
  * 60개의 built-in template filters 제공
  * chained가 가능, 일부 필터는 인자를 받기도 함
    * {{variable|truncatewords:30}}
* **Tags**
  * {% tag %}
  * 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등  변수보다 복잡한 일들을 수행
  * 일부 태그는 시작 태그, 종료 태그가 필요
    * {% tag %} .... {%endtag%}
* **Comments(주석)**
  * {# lorem ipsum #}
  * django template에서 줄의 주석을 표현하기 위해 사용
  * 한 줄 주석에만 사용 가능(줄바꿈 허용x)
  * 템플릿 코드도 주석으로 달 수 있음
  * 여러 줄 주석은 {% comment %}와 {% endcomment %} 사이에 입력

### 생성

* 앱 폴더 안에 `templates` 폴더 생성
  * 이름 무조건 templates
* `templates` 폴더 안에 `index.html`파일 생성
* `index.html` 수정
* 템플릿 경로를 templates 폴더를 기준으로 설정
  * 'index.html'

```python
def index(request): # 첫 번째 인자는 반드시 request
    return render(request, 'index.html')
```

```python
def greeting(request):
    return render(request, 'greeting.html', {'name': 'Harry'})
```

```html
<h1>안녕하세요. 저는 {{name}} 입니다.</h1>
```

* 다음과 같은 방법으로도 가능

```python
def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    
    context = {
        'info': info,
        'foods': foods,
    }

    return render(request, 'greeting.html', context)
```

```html
<h1>안녕하세요. 저는 {{info.name}} 입니다.</h1>
<p>제가 좋아하는 음식은 {{foods}} 입니다.</p>
<p>{{foods.0}}를 가장 좋아합니다.</p>
```

#### Filters

* filter 사용

```python
def dinner(request):
    foods = ['족발', '피자',' 햄버거', '초밥']
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)
```

```html
<h1>오늘 저녁은 {{pick}} </h1>
<p>{{pick}}은 {{pick|length}}</p>
```

#### Tags

```html
  <p>메뉴판</p>
  <ul>
    {% for food in foods %}
      <li>
        {{food}}
      </li>
      {% endfor %}
  </ul>
```

#### comments

```html
  {# 이것은 주석입니다. #}
  {% comment "" %}
    <p>1</p>
    <p>2</p>
    <p>3</p>
  {% endcomment %}
```



## 상속

### Template inheritance

* 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤
* 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함
* 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 "skeleton" 템플릿을 만들 수 있음