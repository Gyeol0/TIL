# CSS

* 스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어

```css
h1 {
    color:blue;
    font-size: 15px;
}
```

* 세미클론으로 구분
* 선택자 h1
* color, font-size 속성
* 15px 값



### 정의 방법

1. 인라인(inline)
2. 내부 참조(embedding) 
   * head 부분에서 style 지정
3. 외부 참조(link file) - 분리된 CSS 파일



#### 인라인(inline)

```html
<body>
  <h1 style="color:blue; font-size: 10px">인라인</h1>
</body>
```

*  두 가지 이상의 속성을 정의할 때에는 `;(세미클론)` 사용
*  body 내부 각 태그마다 지정

#### 내부 참조

```html
  <style>
    .blue {
      color: blue;
    }
    .bold {
      font-weight: bold;
      font-size: 50px;
    }
  </style>

</head>
<body>
  <h1 class="blue bold">인라인</h1>
</body>
```

* 스타일 태그에 정의
* 클래스, 요소 등의 스타일 지정
* 여러 개의 클래스일 때에는 `스페이스`로 구분

#### 외부 참조

* 단독적인 외부 파일을 참조
* `<head>`내의 `<link>`를 통해 참조



## 선택자(Selector)

* HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서 사용
* 기본 선택자

  * 전체 선택자(문서 전체`*`), 요소 선택자(태그 선택자)
  * 클래스 선택자, 아이디 선택자, 속성 선택자
* 결합자(Combinarors)

  * 자손 결합자, 자식 결합자 - **자식 결합자까지만.**
    * 자손결합자 : 하위 모든 요소
    * 자식 결합자 : 바로 한 단계 하위 요소
  * 일반 형제, 인접 형제 결합자
* 의사 클래스/요소(pseudo class)

  * 링크, 동적 의사 클래스
  * 구조적 의사 클래스


### 적용 우선순위

1. `!important`
2. 인라인
3. id 선택자
4. class선택자
5. 요소선택자
6. 소스 순서



## 상속

* CSS는 상속을 통해 부모 요소의 속성을 자식에서 상속한다. 모두x
* 상속 되는 것
  * Text 관련 요소(font, color), opacity, visibility 등
* 상속 되지 않는 것
  * Box model 관련 요소(width, height)
  * position 관련 요소(position, top, left, z-index)



## 단위

### 크기 단위

* px
* %
* em
  * 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐.
* rem
  * 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐.
* viewpoin기준 단위
  * vw, vh, vmin, vmax

### 색상 단위

* 색상 키워드
* RGB 색상
  * `#` + 16진수 표기법, `#000`
  * rgb() 함수형 표기법, rgb(0, 0, 0), 검정
  * rgb 숫자가 높을 수록 빛이 없음, 흰색

* HSL 색상
  * 색상, 채도, 명도

### 문서 표현

* 텍스트
* 컬러, 배경
* 목록



## Box model

### 구성

* Margin

  * 테두리 바깥의 외부 여백
  * 배경색을 지정할 수 없음
* Border

  * 테두리 영역
* Content

  * 글이나 이미지 등 요소의 실제 내용
* Padding

  * 테두리 안쪽의 내부 여백
  * 요소에 적용된 배경색
  * 이미지는 padding까지 적용


### box-sizing

* 모든 요소의 `box-sizing`은 `content-box`
  * padding을 제외한 순수 contents 영역만을 box로 지정
* border까지의 너비까지 합하여 보기를 원하면 `box-sizing`을 `boder-box`로 설정

### 마진 상쇄(Margin collapsing)

* 인접 형제 요소 간의 margin이 겹쳐서 보임



## Layout

* 웹 페이지에 포함되는 요소들을 취합하고, 그것들이 어느 위치에 놓일 것인지를 제어하는 기술

* Display

* Position

* Float

* Flexbox

* Grid

* Table layout

* Multiple-column layout

  

### DIsplay

* 모든 요소는 박스모델이고, 어떻게 보여지는지(display)에 따라 문서에서의 배치가 달라질 수 있다.
* HTML 요소들을 시각적으로 어떻게 보여줄지 결정하는 속성

* `display`: `block`
  * 줄 바꿈이 일어나는 요소
  * 화면 크기 전체의 가로 폭을 차지한다.
  * 블록 레벨 요소 한에 인라인 레벨 요소가 들어갈 수 있음.
* `display`: `inline`
  * 줄 바꿈이 일어나지 않는 행의 일부 요소
  * content 너비만큼 가로 폭을 차지한다.
  * width, heigth, margin-top, margin-bottom을 지정할 수 없다.
  * 상하 여백은 `line-height`로 지정한다.

* 블록 레벨 요소
  * div / ul, ol, li / p / hr / form  등
* 인라인 레벨 요소
  * span  / a / img / input, label / b, em, i, strong 등
* `display`: `inline-block`
  * block과 inline 레벨 요소의 특징을 모두 갖는다.
  * inline처럼 한 줄에 표시 가능
  * block처럼 width, height, margin 속성을 모두 지정할 수 있다.
* `display`: `none`
  * 해당 요소를 화면에 표시하지 않는다. (공간조차 사라진다)
  * visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.



### Position

* 문서 상에서 요소를 배치하는 방법을 지정
* `static`: default
  * 기본적인 요소의 배치 순서에 따름(좌측 상단)
  * 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 된다.
* `relative`: static 위치를 기준으로 이동(상대 위치)
  * top, bottom, left, right를 사용하여 이동 가능
  * 기본 위치를 기준으로
* `absolute`: static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(절대 위치)
  * top, bottom, left, right를 사용하여 이동 가능
* `fixed` 부모 요소와 관계 없이 브라우저를 기준으로 이동(고정 위치)
  * 스크롤시에도 항상 같은 곳에 위치
  * top, bottom, left, right를 사용하여 이동 가능



### Float

* 이미지 좌, 우측 주변으로 텍스트를 둘러싸는 레이아웃을 위해 도입
* 이미지가 아닌 다른 요소들에도 적용해 웹 사이트의 전체 레이아웃을 만드는데까지 발전
* 속성
  * `none`: 기본값
  * `left`: 요소를 왼쪽으로 띄움
  * `right` : 요소를 오른쪽으로 띄움
* 위로 띄워서 아래에 있는 이미지가 위로 올라와서 겹쳐보임



### Flexbox

* 요소 간 공간 배분과 정렬 기능을 위한 1차원(단방향) 레이아웃
* **요소**
  * Flex Container(부모 요소)
  * Flex Item(자식 요소)
* **축**
  * main axis(메인축)
  * cross axis(교차축)
* `display`: `flex`
* 배치 방향 설정
  * **flex-direction**
    * row(row reverse)
    * column(column reverse)
    * default : row
* 메인축 방향 정렬
  * **justify-content**
* 교차축 방향 정렬
  * **align-items**, align-self, align-content
* 기타
  * **flex-wrap**, flex-flow, flex-grow, order, flex-shrink, flex-basis
* **justify-content**
  * flex-start, flex-end, center, space-between, space-around, space-evenly
* **align-items**
  * flex-start, flex-end, center, stretch, baseline
* **align-content**
  * flex-start, flex-end, center, stretch, space-between, space-around
* **align-self**
  * auto, flex-start, flex-end, center, stretch, baseline