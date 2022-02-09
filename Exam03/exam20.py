# 메서드, 함수는 같다 : self 있고 없고의 차이 점
# 메서드는 클래스 안에서 정의한 함수 - self 있다
# 메서드 : 파라미터가 있고, 리턴 값이 있는 메서드
#          파라미터 있고, 리턴 값이 없는 메서드 
#          파라미터가 없고, 리턴 값이 있는 메서드
#          파라미터가 없고, 리턴값이 없는 메서드

class Calc:
    # 클래스 변수 : 외부에서 접근 가능 | 사용 권장하지 않음 => 보안코드(시큐어 코딩) 작성 시 문제 발생
    total = 0
    def Plus(self,inputData1,inputData2):
        # 클래스 내에 선언하고, 다른 메서드에서 호출 가능(사용 및 저장)
        Calc.total = inputData1+inputData2
        return Calc.total

# 인스턴스 함
result = Calc()

data1 = result.Plus(200,820)
result.Plus(20,820) #Plus 메서드를 실행하면 값을 받아줄 변수를 선언하지 않았음 | 실행은 된다. 값을 저장할 변수가 없을 뿐이다.
data2 = result.total # 클래스 변수를 외부에서 호출하는 것은 권장하지 않는다.

temp = 0
