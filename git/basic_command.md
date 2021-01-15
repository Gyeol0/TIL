# git command

> git 기초 명령어 정리



## 기본

### cd

* `cd <폴더명>`
* 하위 폴더로 진입



### ls

* `ls`
* 현재 directory에 있는 모든 파일, 폴더 조회
* `ls -a`
  * 숨겨진 파일, 폴더까지 조회



### touch

	* `touch <파일이름.확장자>`
	* <파일이름>의 파일 생성



### mkdir

	* `mkdir <폴더 이름>`
	* <폴더 이름>의 폴더 생성





## 설정

### init

* `git init`
* 폴더를 git으로 관리하기 위해 `.git` 폴더를 생성하는 명령어
* 최초에 한 번만 실행하면 된다.



### status

* `git status`
* 현재 git의 상태를 출력



### log

* `git log`
* 현재 쌓여있는 commit history를 출력



### diff

* `git diff`
* 마지막 commit과 현재 working directory의 상태를 비교



### remote add

* `git remote add <별명> <주소>`
* 원격저장소 주소를 등록



## 조작

### add

* `git add <파일이름>`
  * <파일이름>에 `.`을 입력하면 전체 파일이 추가된다.

* working directory에 있는 파일을 staging area(INDEX)에 올림
  * `git status`를 통해 직관적으로 확인 가능.



### commit

* `git comit`
  * `git commit -m "<message>"`
  * `<message>`에 메시지 저장 가능(옵션)
* staging area에 올라간 파일들을 스냅샷으로 저장



### puch

* `git push <원격저장소 이름> <올릴 브랜치 이름>`
  * `git push origin master`
* commit history를 원격 저장소에 업로드