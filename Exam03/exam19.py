class UserInfo:
    # 클래스 안에서 선언한 함수는 메서드로 표시
    # 파라미터가 없는 메서드도 무조건 첫번째에 self 써준다
    def Plus(self, inputData1, inputData2):
        return inputData1 + inputData2
    pass

# 클래스는 객체지향프로그래밍에서 나만의 데이터 타입을 만들 때 사용함
# 나만의 데이터 타입을 선언하고 사용
# 나만의 데이터 타입 선언 -> 인스턴스
# 인스턴스 한 결과물 -> 변수 이자 객체
# 인스턴스 하는 법 : 변수명 = 클래스명()
result = UserInfo()
result.Plus()