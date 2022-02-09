#클래스 선언
class Calc:
    total = 0 # 클래스 변수
    # Python에서는 클래스를 인스턴스 하면 생성자를 자동으로 만듬
    # Python은 초기자(Initializer) 인스턴스를 할 때 초기에 어떤 값을 가지고 시작할 지 정해야 사용할 수 있음
    # 초기자 메서드를 하기 위해선 특수 내장 함수인 __init__ 사용
    # __init__으로 초기값을 구현해야 밑에 result라는 객체를 생성했을 때 자동으로 호출되어 초기값을 설정할 수 있게 되는 것이다.
    # __init__ 파일에는 패키지 정보, 모듈 정보들을 확인 할 수 있도록 해야 함
    def __init__(self, inputData1, inputData2):
        #self = 자기 자신을 가리킴.
        #self로 선언한 변수는 인스턴스 변수이다.
        #메서드 내에서 선언하고, self.변수 이렇게 한다.
        #다른 메서드에서 접근 가능
        self.data1 = inputData1
        self.data2 = inputData2
        Calc.total = self.data1 + self.data2

    # 인스턴스
    def Plus(self):
        tempData = self.data1 + self.data2
        return tempData


    # 정적 메서드 : 인스턴스 하지 않고 바로 클래스 안에 있는 메서드를 사용하는 방법
    # self 파라미터를 사용하지 않는다.(사용할 수 없다.)
   
    @staticmethod
    def Minus(input1, input2): # inputData1 , inputData2는 초기자 메서드와 다른 변수
        return input1 - input2 

    # 클래스 메서드 : 정적 메서드는 정적끼리만 서로 사용 가능하지만, 클래스 메서드는 클래스 안에 있는 인스턴스를 사용할 수 있음.
    # self 대신 클래스 대표 이름을 변수로 선언한다.(여기서는 Mul) 
    @classmethod
    def Mul(cls): # self 대신 class 이름을 대신할 변수(파라미터를 선언)
        print(cls.total)

# 객체 생성 후에 메서드를 호출하는 과정 없이도, 
# 초기자를 통한 초기값 생성을 통해 클래스 내부의 다른 메서드 들도 호출이 가능해 졌다.
result = Calc(10,30) # 인스턴스를 할 때 초기값을 넣어줄 경우 사용 : 인스턴스 변수에 할당해서 사용

data1 = result.total # 사용할 때에는 보안 코드를 신경쓰기 때문에 클래스 메서드를 활용하는 것을 권장한다.(total은 클래스 변수)
data2 = result.Plus()
data3 = Calc.Minus(100,20) # 객체를 따로 선언해서 인스턴스 한 것이 아니라 바로 메서드를 호출한 예시

# 클래스 변수를 사용할 때 : 보안 코드 작성에서 직접 호출, 사용을 권장하지 않는다.

# 클래스 메서드는 인스턴스 사용 해야한다.
result.Mul()

# 디버깅 위한 임시 변수
temp = 0