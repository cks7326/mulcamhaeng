# 산술 연산자
# Python +,-,*,/,**제곱,
# % 나눗셈을 하고 나머지 값만 가져오기, // 나누기 후에 소숫점을 버리고 가져오기

# 비트 연산자 : Bitwise 연산자 &,|,^,~,<<,>> shift 연산
# 실제 값을 2진수로 변경후 그 값을 연산하는 것
data2 = 65
data3 = 64
data4 = data2 & data3
data5 = data2 | data3

# 멤버쉽 연산자 : in
data6 = [1,2,3,4,5,6,7,8]
data7 = 5 in data6 # 결과는 True

# Identity 연산자 : is, is not
data8 = "홍길동"
data9 = "나이는 20"
data10 = data8 is data9 # 결과는 ? : 결과를 bool 형식으로 줌

data11 = 1999
data12 = 99.9999
data13 = data11 is data12 # 결과는 ?

data14 = 99
data15 = data14
data16 = data14 is data15 # 결과는 ?

data = 0