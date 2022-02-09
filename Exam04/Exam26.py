# 다형 이론 : 메서드 오버라이드(오버라이딩)

class MyInfo :
    def __init__(self, name):
        self.name = name
        

    def UserName(self):
        return self.name

    def UserAge(self):
        return self.age

# 상속 (파생) 만들때는 클래스 이름 뒤에 (부모 클래스 이름)을 넣어준다
class ExtMyInfo(MyInfo) : # 부모(base class : 기본) 클래스를 상속한다.

    #메서드 오버라이드
    def UserName(self): # 부모 클래스의 메서드와 똑같은 이름, 파라미터도 똑같이 한 메서드(리턴도)
        dataTemp = super().UserName() + "님" 
        return dataTemp

    def UserEmail(self):
        pass

result1 = MyInfo('홍길동')
data1 = result1.UserName()

result2 = ExtMyInfo('홍길동')
data2 = result2.UserName()


temp = 0