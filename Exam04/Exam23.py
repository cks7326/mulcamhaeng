class MyCLS:
    def __init__(self, name , age):
        __data2 = 0 # 클래스 인스턴스를 통해서 사용 : 보안코드 (시큐어 코딩)에서 권장
        # 인스턴스 변수 선언 : 주의점 - 파라미터의 변수를 그대로 사용하면서 self를 붙인다.
        self.name = name
        self.__age = age # 인스턴스 변수 private 타입의 변수

    def __MyMethod1(self): # private 타입의 메서드
        pass
        


result = MyCLS('홍길동',20)
result2 = MyCLS(age=10,name = '길동이') # 초기자 메서드이기 때문에 명명된 파라미터의 응용

#data1 = result.__age # -> 오류 : 정보은닉
#result.__MyMethod1() # -> 오류 : 정보은닉
#data3 = MyCLS.__data2 # -> 오류 : 정보 은닉

temp = 0