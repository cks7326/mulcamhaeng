# Python 에서 데이터를 정제 하기 위해서 사용하는 모듈
# DB에서 가져오거나 또는 XML 문서 또는 JSON 파일 또는 인터넷에 있는 API 서버 가져옴
# Python 에서는 데이터 처리용 플랫폼 : Anaconda(아나콘다) - 1. 과학 계산용, 데이터 정제
# 데이터 분석용 중에 유명한 Pandas
# 실제 데이터를 가져올 때 해당 데이터 사용을 위해서 정제
# Python 그리고 기타 언어에서 행,열,면으로 할 경우 반복문을 중첩으로 처리하면 데이터 정제 가능
# Python 에서는 모듈을 이용하면 반복문을 안해도 가능함 = pandas를 쓰면 조금 편하다
# Bigdata 형식의 데이터로 정제 및 상업용 데이터 베이스 시스템으로 저장할 때 편리하다.

import pandas as pd
import numpy as np
data1 = [213,3232,123,54,12]

# pandas : 1차원 배열의 값에 해당하는 인덱스를 부여 또는 사용
resultData1 = pd.Series(data1)
print(resultData1)


# 데이터 프레임 : 2차원 배열 - 리스트 안에 데이터를 
# 행 / 열 두기 때문에 데이터베이스의 데이터를 행, 열 구문할 때 보통 처리
# json파일의 데이터 또는 외부의 데이터를 관계형 데이터베이스와 연동 또는 형식으로 출력할 때
# index 값이 컬럼(열), 실제 데이터 로우(행), 리스트 데이터
data2 = {
    "이름" : ["홍길동", "이찬행"],
    "나이" : [21,25],
    "주소" : ["서울","동탄"]
}

resultData2 = pd.DataFrame(data2)
print(resultData2)
# 행(데이터)
data3 = [["홍길동1","이찬행","홍길도3"], [20,21,25],["서울시 강남구","서울시 서초구","동탄"]]
# 왼쪽에 표시되는 항목 = index 
data4 = ["이름", "나이", "주소"] # 위에 표시되는 항목 = 컬럼
#data5 = []

resultData3 = pd.DataFrame(data3, columns=data4) #index=data4)#, columns=data5)
print(resultData3)
# 판넬 - panel : 3차원 배열
# import numpy as np
# 1차원 / 2차원/ 3차원 배열 
#resultData4 = np.array()

# data6 = np.random.rand(1,2,3)
# resultData5 = pd.Panel(data6)
# print(resultData5)


temp = []

