# 딕셔너리(Dictionary) : 책이 목차
# 키 - 값의 쌍으로 연결
# 키 사용할 수 있는 것 Tuple 키로 사용 가능 : List는 키로 불가능
# 해시테이블 : 자료구조
# 중괄호 {}

dicData1 = {"이름":"홍길동", "나이":20}
# 값을 가져올 때에는 인덱스에 키 값을 이용해서 가져옴
resultData1 = dicData1["이름"]
dicData1["이름"] = "길동이"
dicData1["나이"] = 25


userData = [('홍길동',20),('홍길',25),('홍동',30)]
dicData2 = dict(userData) # List와 Tuple로 이루어진 데이터를 Dic로 변경

dicData3 = dict(name = "홍길동" , age = 20, birth = "20220119")
resultData2 = dicData3["birth"]

del dicData3["name"] # 삭제

# 디버깅 위한 임시 변수
temp = 0