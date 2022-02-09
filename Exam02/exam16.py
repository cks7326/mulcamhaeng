import exam16ext





# 전역변수 / 글로벌 변수(다른 파일에서 가져와서 사용할 수 있는 변수라는 점이 차이점) 
# -> Python에서는 두 개가 같다고 보지만, 다른 언어는 차이점이 있고, 글로벌 변수는 잘 쓰지 않는다
result1 = exam16ext.Add(100,200)

def MyFunction():
    print('함수1')
    re = exam16ext.Add(20,10)
    print(exam16ext.data1)
    exam16ext.data1 = 999999
    print(re)
    print(result1)

#print(re) #오류 : re 는 함수 안에 있는 지역 변수

# 실제 코드 작성
if __name__ == '__main__':
    print(__name__)
    MyFunction()
    exam16ext.Add(200,200)
    print('전역변수 result1 을 다른 값으로 변경')
    result1 = 1
    print(result1)


temp = 0



