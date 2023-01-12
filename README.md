# Markdown
- 텍스트 기반의 가벼운 마크업 언어
- 문서의 구조와 내용을 같이 쉽고 빠르게 적고자 탄생
  
>[마크다운 작성법](https://gist.github.com/ihoneymon/652be052a0727ad59601)

---

# GIT
  ![git](https://velog.velcdn.com/images/crosstar1228/post/969185d2-d80f-41cc-b234-f5fb71f1304e/image.png)
  
  - "Test" 저장소 만들기 (git->local)
  1. 현재 목록 확인하기 (요기서 cd ..같은 명령어 사용)
   
        *cd = change directory*

  2. git clone https://github.com/nachocatee/Test.git (클론 생성)
  3. cd Test (Test 폴더로 이동)
  4. touch README.md (파일 생성)
  5. 편집 후 git add README.md
  6. git commit -m "README.md"
  7. git push origin main
  8. **완성!**

---

- "Test" 저장소 만들기 (local->git)
  
1. mkdir Test
2. cd Test
3. touch README.md
4. git init
5. git remote add origin https://github.com/nachocatee/Test.git
6. git add README.md
7. git commit -m "README.md"
8. git push origin main
9. **완성!**