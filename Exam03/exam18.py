# class 이름
# 함수(Python 메서드로 부름) : 함수 만들 때 주의점은 self 를 사용해야한다는 것.

import ExamCLS # 파일이름

#객체를 만들어야 ExamCLS에 있는 함수를 사용할 수 있다.
data1 = ExamCLS.TestCLS() # 인스턴스 생성의 결과 -> 객체 data1이 객체
# 인스턴스 - ExamCLS.TestCLS()
# data1을 이용해서 TestCLS 클래스 안에 있는 클래스와 클래스 변수 사용
# data2 = data1.Method
data1.TestPrint() # data1.__TestMethos 쓰면 안된다(정보은닉 때문에)

# data2=ExamCLS.TestCLS()
# data3=ExamCLS.TestCLS()
# temp = data3.Method # 인스턴스 변수 호출(오류) : 속성

temp = 0