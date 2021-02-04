# HTML

> Hyper Text Markup Language

* 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
* 프로그래밍 언어와는 다르게 단순하게 데이터를 표현하기만 한다.
* 웹 페이지를 작성하기 위한 언어(구조를 잡기 위한)
* 웹 컨텐츠의 의미와 구조를 정의



## 기본 구조

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

* `head`와 `body` 부분으로 구분
* `head`
  * 문서 제목, 인코딩과 같이 해당 문서 정보를 담고 있음
  * 브라우저에 표현되지 않는다.
  * `CSS`선언 혹은 외부 로딩 파일 지정
* `body`
  * 브라우저 화면에 나타나느 정보로 실제 내용에 해당된다.
* `DOM(Document Object Model)` 트리
  * 부모관계
  * 형제 관계
* 태그와 요소로 구성
  * 여는 태그
  * 닫는 태그
  * content
* 태그별로 속성이 다르다.



### 시맨틱 태그

* header
  * 문서 전체나 섹션의 헤더
* nav
  * 네비게이션
* aside
  * 사이드 공간
* section
  * 문서 구분, 컨텐츠 그룹
* article
  * 문서, 페이지
* footer
  * 문제 전체나 섹션의 마지막 부분
* Non semantic
  * span
  * div



### 시맨틱 웹

* 웹 상에 존재하는 수많은 웹 페이지들에 메타데이터를 부여
* `의미`와 `관련성`을 가지는 거대한 데이터베이스로 구축



## 태그

### 그룹

* p
  * 문단을 나눌 때 사용
  * 위, 아래 한 줄 띄움
* hr
  * 수평 줄 넣기, 주제 바뀜을 나타냄

* ol, ul

  * 리스트

  * ol은 순서가 있는 리스트

  * ul은 순서가 없는 리스트

  * ```html
      <ul>
        <li>없음</li>
        <li>순서</li>
      </ul>
    
      <ol>
        <li>1번</li>
        <li>2번</li>
      </ol>
    ```

* pre, blockquote

  * 여백이나 줄간격을 고정

* div

  * 컨텐츠 영역이나 그룹화

### 텍스트

* a
  * 하이퍼링크
* b, strong
  * bold
* i, em
  * 이탤릭체
  * 기울임
* span, br, img
  * span : 다른 텍스트와 구별
  * br : 줄바뀜
  * img : img 삽입

### 테이블

* tr, td, th
* thead, tbody, tfoot
* caption
* colspan, rowspan
* scope
* colm colgroup

### form

* 서버에서 처리될 데이터를 제공하는 역할
* action
* method

### input

* label
  * 서식 입력 요소의 캡션
* name, placeholder
* required
* autofocus
  * 자동 클릭