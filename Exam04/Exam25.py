# 상속 추가

class CLS1: # 할아버지
    def __init__(self, name):
        self.name = name
        print(self.name)

class CLS2(CLS1): # 아버지
    def __init__(self, age):
        super().__init__(self) # 자식 클래스에서 init 쓸 때 super().__init() 써줘야한다. 
        # -> super 쓰면 부모 메서드 접근 가능하다. 꼭 써야함
        self.age = age
        print(self.age)

class CLS3(CLS2):
    pass

result = CLS1('홍길동')
result = CLS2(20)

temp = 0

