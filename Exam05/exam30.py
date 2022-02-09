# 튜플(Tuple) 리스트와 비슷함
# 리스트는 [] 튜플은 () 안에 요소를 저장 사용
# 튜플은 읽기 전용이라서, 수정 삭제 추가 불가능하다.
# 리스트 : 읽기,수정,삭제,추가 가능

tupleData1 = (135,24324,'홍길동')
tupleData2 = (213213) # 정수형 데이터
tupleData3 = (213213, ) # 튜플 타입 데이터

tupleData4 = (123,524,54,658,23)
#인덱스
resultData1 = tupleData4[0]
resultData2 = tupleData4[4]
resultData3 = tupleData4[-1] # 마지막 요소 get
#슬라이스
resultData4 = tupleData4[2:4] # 리스트와 같다
resultData5 = tupleData4[2:]
resultData6 = tupleData4[:4]

#합치기(병합)
tupleData5 = tupleData4 + tupleData1 # 병합
tupleData6 = tupleData5*5 # 튜플 데이터 * n 반복

# 값에 변수 할당 가능
tupleData7 = ("홍길동",20)
resultData6[:]
# 튜플의 값을 변수에 하나씩 할당 가능
resultData6, resultData7 =  ("홍길동",20)
resultData6[:]
resultData7[:]

#수정
changeData = list(tupleData4) # 튜플 데이터를 리스트형으로 변경 후 수정
tupleData6 = tuple(changeData) # 기존 것은 최대한 그대로 둔다.(실무)
tupleData7 = tuple(changeData) # 권장

#디버깅을 위한 임시 변수
temp = 0