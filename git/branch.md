# Branch

* git 삭제할 때
  * `rm -rf .git`

## 수정

* 웹 IDE에서는 수정하지 말 것
* 같은 내용으로 수정했더라도 히스토리가 달라짐
  * 이를 해결하기 위해서 pull
  * pull하면 원격저장소에 있는 히스토리를 로컬 저장소로 끌고 오고 로컬의 수정본과 충돌이 일어남
  * 둘 중에 뭐로 남길 것인지 선택
    * `<<<<<<< HEAD` 로컬 저장소
    * `========`
    * `>>>>>>>> ` 원격 저장소
  * MERGING

## 리셋

### reset

* `git reset <log>`
* `git log --oneline`으로 log 확인
  * `git log --oneline --graph`
* 원하는 지점으로 돌아감
  * ROLLBACK이랑 비슷?
  * 과거로 돌아감

### revert

* `git revert <log>`
* 기억 순서는 그대로
* 과거 log 그때의 수정 내용을 알려줌
  * 내가 수정하고 log을 쌓음

## branch

* `git branch` : branch 확인
* `git branch <branch name>` : branch 생성
* `git switch <branch name>` : 이동
* `git branch -d <branch name>` : 삭제

* HEAD는 내가 보고 있는 데이터

### switch

* `git switch <branch name>`를 하고 수정을 하면 분기가 시작.
  * `git switch <branch name>`으로 바꾸고 수정하고 commit을 한 다음
  * 다시 master로 돌아가면 수정한 내용이 없다.
  * 다른 줄기로 나누어 만들고 있음
* master : 실제 진행하는 서비스, 배포된 서비스
  * 코드 수정할 때, 여기서 하면 안되고 develop이나 다른 branch에서 수정
  * 수정 후 버그 확인 후에 master에 새로운 버전
* develop, hotfixes, release branches, feature branches



## merge

* `git pull origin <branch name>` : 지명한 branch를 가져옴
* `git merge <branch name>`: 지명한 branch로 master 이동, 빨리감기?
  * 보통 merge할 branch에서 실행(상위 branch)
  * 병합되면 branch 기능이 다 했기 때문에 branch 삭제
  * `git branch -d <branch name>`
  * 현재에 master에 branch 수정본을 추가하는 느낌
    * master와 branch에서 수정한 파일이 다를 때에는 충돌이 일어나지 않음
* 같은 파일 수정해서 충돌이 일어날 때
  * 둘 중 하나의 수정본을 선택하거나, 둘 다 쓰거나 상황에 따라 선택해서
* 웬만하면 분기된 가지로 merge
  * 바로 master로 merge는 별로
* 원격 저장소에서도 병합 가능

