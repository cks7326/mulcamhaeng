extData11 = 100 # 클래스 안으로 못 가져온다. 호출 불가(self. 불가) - 전역 변수 (글로벌 변수는 호출 가능.)

class TestCLS():# 클래스를 생성함
    myData = 100 # 클래스 변수이자 글로벌 변수
    __myData2 = 200 # Private 선언한 클래스 변수

    def Plus(self, inputData1, inputData2) : #메서드와 함수의 차이는 파라미터에 self 있으면 메서드 이다.
        # myData = 2000 # 메서드 안에서 선언한 변수
        # self.myData = 1 # 이건 클래스 변수를 호출한 것
        self.Method = '데이터 넣기' # 인스턴스 변수 : 속성 - 메서드에서 사용가능, 호출하는 곳에서도 사용가능하다(지역변수와의 차이점)
        extData11
        pass

    def TestPrint(self): # 파라미터로 전달할 값이 없어도 무조건 self를 넣어줘야함 
        self.__TestMethos()

    # 원래 다 함수들 이지만, 클래스를 씌워 객체 지향을 하니까 메서드로 됐다. 함수가 적다면 굳이 클래스를 쓰지 않아도 된다.


#Python 에서는 모두 Public 메서드가 기본 / 객체지향에서 Private 으로 선언해서 노출을 하고 싶지 않다면,
    def __TestMethos(self):
        print('private 메서드')

# __를 통해 정보은닉(private 하게 한다.)
# private 으로 선언하는 방법은 클래스 안에 모든 자원(메서드,변수)을 __ 붙이면 정보은닉이 된다.