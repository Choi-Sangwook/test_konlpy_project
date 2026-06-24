# Github에서 'create repository'로 프로젝트 저장소 생성
# url 주소 복사

# 파이참에서 '새프로젝트 생성'
# 터미널 열기

# 내 컴퓨터와 github저장소 연결
git remote add origin git주소
git remote add origin https://github.com/Choi-Sangwook/test_konlpy_project.git

# 연결 확인
git remote -v
# 표시되면 연결 성공
origin  https://github.com/Choi-Sangwook/test_konlpy_project.git (fetch)
origin  https://github.com/Choi-Sangwook/test_konlpy_project.git (push)

# .gitignore 작성 : git에 업로드하면 안되는 파일들 설정

# git 메뉴 -> commit -> 커밋 메세지 작성 -> 커밋 클릭
# 터미널로 하면 : 
git add .
git commit -m "Initial Commit"

# 브렌치(branch)
git branch
# 출력 확인
*master
또는
*main

# 만약 마스터라면 main으로 변경
git branch -M main
# 확인
git branch

# 최초 업로드 : Main 브렌치 push
git push -u origin main
# 옵션 설명
# -u : 현재 branch(main)와 Github의 main을 연결

# 브라우저 Github에서 새로고침하고 업로드 확인

# 최초 업로드 이후 작업 방법
# 1. 코드 파일 추가 | 코드 수정 작업 -> 저장
# 2. 지역저장소에 추가 -> commit
# 커밋방법 3가지중 선택 사용함
# 방법1 : Git메뉴에 있는 commit클릭
# 방법2 : 왼쪽 commit View -> 변경파일 중 선택하고 commit
# 방법3 : terminal에서 commit명령어 입력
# git add .
# git commit -m "commit message"

# 3. 커밋한 다음, Github로 전송 : push
# push 방법 3가지 중 선택
git push

# 깃에 파일 잘못올렸는데 로컬에는 가지고 있어야 하는경우(git에서만 삭제 원하는 경우)
git rm -r --cached folder_name/
git commit -m "Remove ignored folder from tracking"
git push