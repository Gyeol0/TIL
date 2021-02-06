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

  

박스모델

컨텐츠

마지

ㄴ패딩

보더





디스플레이

블락 전체 컨테이너처ㅇ럼 차지

인라인

한줄의 자기 컨텐츠 영역만 차지



속성에 따라  정렬

마진, 그리드 

