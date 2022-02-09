# 함수 : 기능을 정의하고 필요할 때 호출 - def 함수를 만들 때 사용하는 예약어

# 우리가 만든 함수는 사용자 정의 함수 / Python 내부에서 지원하는 함수 = 내장 함수
# 이름 : 규칙 - 예약어는 절대 안됨, 권장 - 영어 단어의 뜻에 맞게 정의하여 사용

# 매개변수 있고, 돌려주는 값이 있다(파라미터)
def Sum():
    total = 100 + 200
    return total

# 매개변수 있고, 돌려주는 값이 없다
def Sum2():
    total = 100 - 10

def Sum3():
    pass

SumData = Sum() # 함수를 호출 돌려 받는 값이 있는 것
Sum2() # 함수를 호출 그냥 끝
Sum3() # 함수를 호출 아무것도 하지 않음 = pass
Sum() # 돌려 받는 값을 저장하는 곳을 선언하지 않음 그래도 될까?

# 매개변수 있고, 리턴값이 있는 함수
def Sum4(inputData1,inputData2):
    total = inputData1 + inputData2
    return total

# 매개변수 있고, 리턴값이 없는 함수
def Sum5(inputData1, inputData2):
    total = inputData1 + inputData2

sumData2 = Sum4(500,600)
Sum5(900,99)

# 교육용 / 실무는 권장하지 않음
# 기본 매개변수 / Default Parameter
def calc(inputData1, inputData2, inputData3 = "+"):
    if (inputData3 == "+"):
        return inputData1 + inputData2
    elif(inputData3 == "-"):
        return  inputData1 - inputData2
    elif(inputData3 == "*"):
        return  inputData1 * inputData2
    elif(inputData3 == "/"):
        return  inputData1 / inputData2

result = calc(100,200,"-")
result2 = calc(100,200) # 기본 세팅인 "+" 적용

# 명명된 매개변수, Named Parameter
# 매개변수(파라미터)를 호출할 때에는 순서에 맞게 호출
def UserData(name, age):
    name += "남"
    result = name + " " + age
    return result

result3 = UserData("홍길동","20")
result4 = UserData(age="50", name="길동이") # 순서 다르지만 변수 지정 했으므로 정상 작동함(권장하지 않음)

# 가끔 사용하는 방법 - 입력 데이터가 몇개인지 상황에 따라 다를때 사용하는 매개변수 입력 방법
# 가변길이 매개변수(파라미터) - 같은 데이터 형식으로 보낼 경우 매우 유용

def TotalProcess(*datas):
    total = 0
    for i in datas:
        total +=i

    return total

return5 = TotalProcess(1,34,43,325,54,63,324,123,32,5)