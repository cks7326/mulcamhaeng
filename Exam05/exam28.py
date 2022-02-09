# 리스트 자료형의 반복문 사용
listData1 = [26,12,345,4,'홍길동']

# 반복문 for - 몇번 반복하는지 알 때 사용
# 반복문 while - 몇번 발복하는지 모를 때 사용
# for구문은 - for 별칭 in 원본데이터 :
listData2 = [] # 리스트의 자릿수는 0 (빈 리스트)
count = 0

#count, index 함수는 검색을 위한 함수(기능)
#count를 이용해서 특정 데이터가 몇개 있는지 확인
cnt = listData1.count(4) 
indexData = listData1.index('홍길동')
mydata = listData1[indexData]

for data in listData1:
    if data == '홍길동':
        mydata = data

for data in listData1:
    #listData2 = data # 리스트에 데이터를 추가해야하는데 이건 변경하는 구문이기 때문에
    listData2.append(data) # 이렇게 써줘야 데이터 추가

# 리스트의 특정 데이터 삭제하는 방법 : del 리스트명[몇번째 요소]

del listData1[2]

#listData2.clear() ->모든 데이터 삭제
#listData2[0] = 1111 -> 수정
# 디버깅을 위한 임시 변수
temp = 0