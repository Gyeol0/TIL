# Bootstrap

### CDN

* Content Delivery(Distribution) Network
* 컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템

### spacing

* mt-1
  * margin-top : 0.25rem 
    * 16 * 0.25 = 4px
    * 브라우저 html의root 글꼴 크기는 16px
* margin
  * m-1 : 0.25rem
  * m-2 : 0.5rem
  * m-3 : 1rem
  * m-4 : 1.5rem
  * m-5 : 3rem

* mx
  * margin-left
  * margin-right
* my
  * margin-top
  * margin-bottom
* ms(start), me(end), mt(top), mb(bottom)
* .mx-auto
  * 수평 중앙 정렬
* p
  * padding
* color
  * primary : 파랑
  * secondary : 회색
  * success : 초록
  * info : 하늘
  * warning : 노랑
  * danger : 빨강
  * light : 흰색
  * dark : 검정



## Grid system

* flexbox로 제작됨
* `container`, `rows`, `column`으로 컨텐츠를 배치하고 정렬
* 12개의 column을 가지고 있음
* 6개의 grid breakpoints
  * xs : <576px
  * sm : >=576px
  * md : >=768px
  * lg : >=992px
  * xl : >=1200px
  * xxl : 1400px