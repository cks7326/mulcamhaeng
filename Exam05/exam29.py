# Python 에서 슬라이스(slice)
# 리스트의 요소들을 잘라서 가져오기 - 범위를 지정해서 가져오는 방법

listData1 = [213,432,54,654,23,123,'홍길동']

listData2 = listData1[2:5]
listData3 = listData1[:3]
listData4 = listData1[2:]


#List Comprehension
# [표현식(표현해야할 방식 또는 데이터를 정의) for 별칭 in 컬렉션(range) 옵션 if 조건식]
listData5 = [i for i in range(10)]
listData6 = [i for i in range(len(listData1)) if i % 2 == 0]
temp = 0
