# 상속 이론 - 저작권 때문에 클래스를 직접적으로 건드리지 못하는 상황이 있을 때 사용한다.


class MyInfo :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def UserName(self):
        return self.name

# 상속 (파생) 만들때는 클래스 이름 뒤에 (부모 클래스 이름)을 넣어준다
class ExtMyInfo(MyInfo) : # 부모(base class : 기본) 클래스를 상속한다.

    def UserAge(self):
        return self.age

class Ext2MyInfo(ExtMyInfo):

    def Userdouble(self):
        return self.age**2

# 요구사항 : 나이를 출력했으면 좋겠다.
# 이 때 MyInfo 클래스를 건드리지 말고 기능을 추가 함. : 이 때 쓰는 것이 상속

result = Ext2MyInfo('홍길동',20) # 자식을 인스턴스 할 경우 부모 클래스의 모든 Public 메서드와 변수를 사용 가능
# 가장 하위 클래스를 인스턴스 해야 상위 클래스의 모든 메서드와 변수를 사용할 수 있다.

data1 = result.UserName() # 인스턴스 메서드 호출함
data2 = result.UserAge()
data3 = result.Userdouble()
#디버깅을 위한 화면 출력
print(data1)


# 상속 : 할아버지 -> 아버지     -> 나
# 다중상속        -> 작은아버지  -> 나(특정 프로그래밍 언어에서는 불가능)