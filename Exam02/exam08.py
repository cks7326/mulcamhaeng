# Python 에서 논리적으로 묶어서 관리하는 함수의 집합
# 하나의 Python 파일에서 하나의 모듈
# 모듈 => 함수,클래스,변수

# import 모듈을 가져오는 예약어
# from 모듈이름 import 함수명 => 해당하는 모듈 안에 import 다음에 오는 함수만 사용한다
# 모듈 =>
# 1) Python에서 제공하는 모듈(함수들)
# 2) 내가 만든 모듈(소스코드를 주는 것이 아니라 결과물만 주는 것)=> 패키지
# 패키지를 모아서 준다 -> API 준다(Application Programming Interface) 함수 목록을 준다
# 패키지 + 함수목록 + 함수 사용 방법(파라미터, 리턴 값 설명)
# MSA => 패키지 안에 함수를 Web으로 노출 도는 API로 노출함 - 함수 이름만
# 홍길동.com/login/login.py?uid=''&pwd=''

# 모듈이 없을 경우 - Python.org에서 제공하는 모듈이 없을 경우
# 상업적으로 판매하는 소프트웨어 회사에서 Python 모듈을 제공하는 것 찾기
# 오픈소스에서 Python 모듈을 제공하는 것 찾기

# import math # 모듈 호출
# from math import factorial
# factorial(100)

from math import (factorial,acos) # math 모듈 안에 1개가 아니라 n개 이상으로 할 때에는 , 를 사용하여 정의 : () 해도 되고 안해도 됨

# 현재 위치도 확인 1순위
# 모듈 위치는 설치 폴더 (Pytho 경로)
# 2순위 : 환경변수 - PythonPath
# 3순위 : Python 설치 폴더의 lib 폴더