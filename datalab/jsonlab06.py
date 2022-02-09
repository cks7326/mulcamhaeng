import json


try:
    jsonFile = open("datalab\\mydata.json", "rb")
    tempData = json.load(jsonFile) # 디코딩 할 때 loads 하지 않는다.(파일 안에서 뭔가를 할 때 loads 한다.)
    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData4 = tempData["email"]
    resultData5 = tempData["empcheck"]
except Exception as ex:
    print(ex)
else :
    jsonFile.close()



jsonData1 = {
    "empid" : 12345678,
    "name" : '홍길동',
    "info" : [
        {"data1": "2022-01-21", "birth" : "1997-01-03"},
        {"data2": "2021-01-21", "age" : 20}
    ]
}

try:
    writeFile = open("datalab\\mydata2.json","w") 
    json.dump(jsonData1,writeFile)
except Exception as ex:
    print(ex)
else :
    writeFile.close()

try:
    writeFile = open("datalab\\mydata2.json","w", encoding = "utf-8") 
    json.dump(jsonData1,writeFile)
except Exception as ex:
    print(ex)
else :
    writeFile.close()

try:
    writeFile = open("datalab\\mydata2.json","w") 
    json.dump(jsonData1,writeFile, ensure_ascii=False)
except Exception as ex:
    print(ex)
else :
    writeFile.close()

try:
    writeFile = open("datalab\\mydata2.json","w", encoding = "utf-8") 
    json.dump(jsonData1,writeFile, ensure_ascii= False)
except Exception as ex:
    print(ex)
else :
    writeFile.close()



temp = 0