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
  * 사용하려면 `USE_I18N = True`되어 있어야함
  * USE_I18N는 국제화
  * USE_L10N는 현지화
    * 한국은 왼쪽부터 쓴다?
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



### 상속(Template inheritance)

* 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤
* 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함
* 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 "skeleton" 템플릿을 만들 수 있음

* base.html을 생성하여 기본 틀을 만들고

```html
    {% block content %}
    {% endblock  %}
```

* 하위 템플릿이 들어갈 공간을 지정

```html
{% extends 'base.html' %}
```

* 어떠한 상위 템플릿을 상속할 것인지 지정
* 꼭!!! 상속은 **최상단**에서 지정한다!!!!

### 설계 철학(Template System)

* 표현과 로직(view) 분리

  * 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이라 생각
  * 이러한 기본 목표를 넘어서는 기능 지원 x

* 중복 배제

  * header, footer 등 대다수의 동적 웹사이트의 공통 디자인
  * 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 제거
  * 템플릿 상속의 기초

  

## HTML Form

### Form

* 웹에서 사용자 정보를 입력하는 여러 방식을 제공
* 사용자로부터 할당된 데이터를 서버로 전송
* 핵심 속성
  * action : 입력 데이터가 전송될 URL 지정
  * method : 전달 방식 지정

### Input

* 사용자로부터 데이터를 입력 받기 위해 사용
* type 속성에 따라 동작
* 핵심 속성
  * name, name을 key로 하여 value를 넘겨준다
  * 중복 가능
  * GET/POST 방식
  * `?key=value&key=value`형태로 전달(주소창에 써져 있음)

### HTTP

* 웹에서 이루어지는 모든 데이터 교환의 기초
* request methods 정의
* GET, POST, PUT, DELETE .....

#### GET

* 서버로부터 정보 조회
* 데이터를 가져올 때 사용
* 데이터를 서버로 전송할 때 body가 아닌 Query String Parameters를 통해 전송



## URL

### urls

* Dispatcher(발송자, 관리자)로서의 URL
* 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서 시작
* 나중에 app이 많아지고 app의 view 함수가 많아지만 path()는 계속 많아진다. 이것을 모두 프로젝트 urls.py에서 관리하면 코드 유지보수에 좋지 않음
* app마다 urls.py 생성하여 작성

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls'))
]
```

* 기존 프로젝트의 urls.py
* `include`함수로 app경로로 가면 바로 경로로 이동시켜 준다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello')
]
```

* app에 있는 view 함수들로 이동시켜 준다.

* 이제부터는 무조건 이름을 설정시켜준다.

* **Variable Routing**

  * `path('hello/<str:name>/', views.hello, name='hello')`
  * hello경로를 가며 name을 입력 받아 사용

  ```python
  def hello(request, name):
      context = {
          'name': name,
      }
      return render(request, 'hello.html', context)
  ```

  * name을 인자로 받는다.

  

### Naming URL patterns

```python
 path('greeting/', views.greeting, name='greeting')
```

```html
<a href="{% url 'greeting' %}">greeting</a>
<a href="{% url 'dinner' %}">dinner</a>
```

* 링크에 직접 url을 적는게 아니라 path()함수의 name 인자를 정의하고 이를 url 태그로 쓴다.
* url 설정에 정의된 특정한 경로들의 의존성 제거



```html
{% extends 'base.html' %}

{% block content %}
  <h1>THROW</h1>
  <form action="{% url 'catch' %}" method='GET'>
    <label for="message">THROW: </label>
    <input type="text" name="message" id="message">
    <input type="submit">
  </form>
{% endblock %}
```

* 템플릿 상속
* 전송할 데이터를 `input`으로 받아서 전송
* `{% url 'catch' %}` catch url로 이동
* `name`은 message로 하여 전송

```python
path('catch/', views.catch, name='catch'),
```

* name이 catch인 url을 받아 views.catch 함수로 간다.

```python
def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)
```

* `request.GET`으로 데이터를 받음(딕셔너리 형태)
* message에 받은 데이터에서 `message` 저장
* 전송할 때에도 딕셔너리 형태로 넘겨줘야해서 딕셔너리로 만들어서 catch.html로 render

```html
{% extends 'base.html' %}

{% block content %}
  <h1>CATCH</h1>
  <h2>{{message}}를 받음</h2>

  <a href="{% url 'throw' %}">다시 돌아가기</a>
{% endblock %}
```

* 넘겨 받은 context 안에 key가 `message`로 담겨 있다.
* {{key}}로 데이터 사용
* `<a href="{% url 'throw' %}">다시 돌아가기</a>`url 태그 링크로 thorw path로 돌아갈 수 있다.



## Addition

### App 생성 순서

1. startapp으로 app 생성
2. settings.py의 INSTALLED_APPS에 app 등록, 절대 미리 등록하지 말 것!!! 생성이 안됨
3. app의 urls.py 생성
4. 사용할 함수 views.py에 정의, urls.py에 path 정의, templates 폴더 생성 후 html 생성

### 상속 방법

1. 프로젝트 폴더에 templates 폴더 생성
2. templates 폴더에 base.html 생성(상위 템플릿)
3. 상위 템플릿 구조 잡기
4. settings.py의 TEMPLATES속성에서 `'DIRS': [BASE_DIR(기본 경로) / '프로젝트 이름' / 'templates']`으로 해서 상속 경로 설정
5. BASE_DIR은 프로젝트 폴더의 상위 폴더. 즉, 프로젝트 폴더와 app 폴더를 가지고 있는 폴더

### Framework 성격

#### 독선적(Opinionated)

* 규제가 있다.

* Django는 다소 독선적

#### 관용적(Unopinonated)

* 다양한 방식으로 짤 수 있다.

* 개발자가 손이 많이 간다.
