# Python 에서는 함수를 많이 봐야함
# 2.6 이상 버전의 문서에서는 쉽게 JSON 파일을 처리하는 기능을 제공
# import json의 모듈을 호출하면 가능
# 데이터를 JSON으로 가져와서 정제하고, 데이터를 저장할 때 JSON 저장 가능

import json

jsonData1 = {
    "empid" : 12345678,
    "name" : '홍길동',
    "info" : [
        {"data1": "2022-01-21", "birth" : "1997-01-03"},
        {"data2": "2021-01-21", "age" : 20}
    ]
}
# json 인코딩 - 한글 데이터 (다국어 : 유니코드 처리하는 부분)
resultData1 = json.dumps(jsonData1) # dic(사전형)을 json 문자열로 반환 할때 dumps
# dic(사전형)데이터를 json 파일로 변환할 때(불러올 때) dump
# 문자열로 가져오기
# 문자열 기능 : join, split, partition .....
# 문자열 정제
resultData2 = json.dumps(jsonData1,indent=4)

# json 디코딩
jsonData2 = json.loads(resultData1) # ->  문자열을 사전형으로 읽기, load -> 파일을 사전형으로 읽기


temp = 0