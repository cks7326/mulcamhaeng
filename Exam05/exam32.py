# Set : 중괄호 사용 - 중복값이 없는 1차원 배열

setData1 = {1,2,234,543,654,1,2,25,43,6} # 중복 제거 후 새로운 데이터 넣기

# 추가(여러개 추가), 삭제, 모두 삭제
setData2 = {1,2,3,4,5}
setData2.add(6)
setData2.update({7,8,9,10}) # 여러개 동시에 추가
setData2.remove(1) # 한개 삭제
#setData2.clear() # 모두 삭제

# 합 , 교, 차 집합
resultData1 = setData1 & setData2 # 교집합
resultData2 = setData1 | setData2 # 합집합
resultData3 = setData1 - setData2 # 차집합

#디버깅을 위한 임시 변수
temp= 0
