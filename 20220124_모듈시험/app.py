from flask import Flask
import json
import requests


# 변수 선언 - 프로그램의 이름 저장하는 변수(파일 이름 저장 변수)
# application server 개발 app 변수를 많이 사용

app = Flask(__name__) # flask 프로그램 시작 app.py로 파일 시작

# 함수 선언
#  시작할 때 경로 선언해야함
@app.route("/") # 웹 사이트 경로를 지정한다 - 앞에서 선언한 app 변수를 사용
def Flasklab(): # 요청 - 메서드 이름이 요청 단계에서 사용하는 것
    return "Flask 데이터 응답" #응답 - return 에서 돌려주는 데이터

@app.route("/data1", methods=['GET'])
def FlaskData():#startPage, pageCount, address): # 요청 받음
    keyValue = r"j8b0Mnuz7av0XrUSk4VM9HSQ7UpBFVu%2F0ZpDOwjCMyrOcKc4hjTvlQcmeaYlI9paTOk%2Bb%2FxVQs7omZ0zJNQPcQ%3D%3D"   

    dataURL = "http://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond%" + r"5BorgZipaddr%3A%3ALIKE%5D=%ED%99%94%EC%84%B1%EC%8B%9C" 
    dataURL += "&serviceKey=" + keyValue
    #tempURL = r"https://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=10
    # &cond=""
    # &serviceKey=""
    # https://api.odcloud.kr/api/apnmOrg/v1/list?페이지 그리고 인증 값 연결
    # page=1
    # &perPage=10
    # &cond%5BorgZipaddr%3A%3ALIKE%5D=%ED%99%94%EC%84%B1%EC%8B%9C
    # &serviceKey=j8b0Mnuz7av0XrUSk4VM9HSQ7UpBFVu%2F0ZpDOwjCMyrOcKc4hjTvlQcmeaYlI9paTOk%2Bb%2FxVQs7omZ0zJNQPcQ%3D%3D
    dataResult = requests.get(dataURL)

    dataResult2 = json.dumps(dataResult.json(), ensure_ascii=False, indent=10)

    

    return dataResult2 
