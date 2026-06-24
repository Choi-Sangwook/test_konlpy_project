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
