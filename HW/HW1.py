class Info:
    def __init__(self,name,age,area,email):
        self.name = name
        self.age = age
        self.area = area
        self.email = email
    
    def UserName(self):
        return self.name

    

    
    

class Phone(Info):
    def __init__(self,name,age,area,email,number):
        Info.__init__(self,name,age,area,email)
        self.number = number

class Add(Phone):
    def UserName(self):
        add = super().UserName() + "님 안녕하세요"
        return add



result = Info('홍길동',20,'동탄','wayrkks@naver.com')
result2 = Phone('홍길동',20,'동탄','wayrkks@naver.com','010-7166-7326')
return3 = Add('홍길동',20,'동탄','wayrkks@naver.com','010-7166-7326')
data3 = return3.UserName()

temp = 0