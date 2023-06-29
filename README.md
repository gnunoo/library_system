# -library_system-

# 프로젝트 소개

- Do it! 장고 + 부스트랩 파이썬웹 개발의 정석 책으로 공부한 django를 복습할 겸, 대학교 DB전공과목에서 내준 도서관리 시스템 만들기 과제를 하기 위해서 프로젝트를 진행하게 되었다. 또한 sqlite3가 아닌 DB전공과목에서 배운 Ms-sql DBMS를 연동하고 사용해보았다. 그리고 소셜 로그인이 아니라 UserCreationForm, authenticate, login, logout, redirect 라이브러리를 이용하여 로그인, 회원가입, 로그아웃의 알고리즘을 배워 보았다. 


# 프로젝트 구조
![image](https://github.com/gnunoo/library_system/assets/97424506/75c81d4c-0b2f-4ae0-b294-5ca0ea9ac44f)


-DB 테이블<br/>
![image](https://github.com/gnunoo/library_system/assets/97424506/964fab74-21e8-4ca3-8fb3-2913e2d4980e)<br/>

![image](https://github.com/gnunoo/library_system/assets/97424506/ebb16205-e154-495f-b031-d0fd0224d86f)<br/>

![image](https://github.com/gnunoo/library_system/assets/97424506/d56aa982-afd4-4801-98a3-1ee74b7337f3)<br/>

![image](https://github.com/gnunoo/library_system/assets/97424506/36ba6b5c-f9e8-4f52-982a-ec6b1e63c286)



# 개발 툴 및 사용 언어
개발 툴: &nbsp; <img alt="pycharm" src ="https://img.shields.io/badge/pycharm-000000.svg?&style=for-the-badge&logo=pycharm&logoColor=whithe"/><br/>
프레임워크: &nbsp; <img alt="django" src ="https://img.shields.io/badge/django-092E20.svg?&style=for-the-badge&logo=django&logoColor=black"/><br/>
언어: &nbsp; <img alt="python" src ="https://img.shields.io/badge/python-3776AB.svg?&style=for-the-badge&logo=python&logoColor=black"/>&nbsp;<img alt="javascript" src ="https://img.shields.io/badge/javascript-F7DF1E.svg?&style=for-the-badge&logo=css3&logoColor=black"/>&nbsp; <img alt="bootstrap" src ="https://img.shields.io/badge/bootstrap-7952B3.svg?&style=for-the-badge&logo=bootstrap&logoColor=black"/><br/>

그 외: &nbsp;<img alt="html5" src ="https://img.shields.io/badge/html5-E34F26.svg?&style=for-the-badge&logo=html5&logoColor=black"/>&nbsp;<img alt="css3" src ="https://img.shields.io/badge/css3-1572B6.svg?&style=for-the-badge&logo=css3&logoColor=black"/>






#  구현 방법
-로그인: 데이터를 가져와서 DB에 있는지 없는지 확인<br/>
-회원가입: UserCreationForm라이브러리 사용<br/>
-책 리스트 보기: &nbsp; ListView를 상속 받아서 구현(get_context_data 오버라이딩)<br/>
-도서 등록 : &nbsp; CreateView를 상속받아서 도서를 추가할 수 있도록 구현 관리자만 등록 할 수 있게 UserPassesTestMixin 라이브러리 사용<br/>
-대여: <br/>
1.Post 통신으로 받아온 데이터(chekbox에 cheack된 데이터)를 split함수로 제목,id 값을 분리<br/>
2. borrowPost 테이블에 save()함수를 이용해서 데이터를 저장 합니다.(omr 사용)<br/>
3. 도서테이블에 데이터를 get()으로 갖고 와서 삭제<br/>
-반납: <br/>
대여 기능이랑 많이 비슷합니다.<br/>

1.Post 통신으로 받아온 데이터(chekbox에 cheack된 데이터)를 split함수로 제목,id 값을 분리합니다.<br/>
2. 도서 테이블(post)에 저장 합니다.<br/>
3.대여 테이블(borrowpost)에는 삭제 합니다.<br/>



# 결과물 
-Login<br/>
<img src='https://github.com/gnunoo/library_system/assets/97424506/bd244cb1-0212-4794-9711-f05edccdbcc4' width='600px' height='400px'><br/>
-Signup<br/>
<img src='https://github.com/gnunoo/library_system/assets/97424506/0c42e55c-bed4-46ea-acde-642585dd0493' width='600px' height='400px'><br/>
-책 등록, 수정(관리자 계정)<br/>
<img src='https://github.com/gnunoo/library_system/assets/97424506/626cf9be-0566-4453-8f2b-482202863ad4' width='600px' height='400px'><br/>  
![image](https://github.com/gnunoo/library_system/assets/97424506/a3cc305e-d078-4113-a362-0aaaa06399fc)<br/>

![image](https://github.com/gnunoo/library_system/assets/97424506/5e3f50a2-4831-473a-a526-3fb541329de5)<br/>

![image](https://github.com/gnunoo/library_system/assets/97424506/448d57ae-bd1f-4c88-9aa5-1d65f6280f1e)<br/>

-대여,반납<br/>
클릭하고 대여 버튼을 누르면 대여함으로 이동하고 반납누르면 반납화면으로 이동합니다.<br/>
![image](https://github.com/gnunoo/library_system/assets/97424506/255317ad-2606-443e-9913-7c3990c48314)<br/>
대여 후<br/>
![image](https://github.com/gnunoo/library_system/assets/97424506/9af3b02e-e310-4c36-b35e-ccd4df45fa96)<br/>
반납 누르고 난 후<br/>

![image](https://github.com/gnunoo/library_system/assets/97424506/804aca4b-76a8-4254-8c94-126a662495b5)<br/>
![image](https://github.com/gnunoo/library_system/assets/97424506/b997a449-09f9-4e2e-a39e-26068bee9d5d)<br/>














