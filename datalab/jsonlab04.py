with open('datalab\\data3.txt',mode='wt',encoding='utf8') as fileName:
    fileName.write("문서쓰기")
    fileName.write("fe3q23wda")


#문자열을 결합
tempData = "홍길동 \n"
tempData += "이름 인데 \n"
#tempData = tempData + "추가 문자열"
with open('datalab\\data4.txt', mode='wt', encoding='utf-8') as fileName:
    fileName.writelines(tempData)
    
    
readFileName = open("datalab\\data.txt", mode="rt", encoding="utf-8")
count = None # 문서 읽기 (숫자가 아니므로)
while count != '':
    count = readFileName.readline()
    temp = count.strip('\n')# 한줄씩 읽어 들이면서 조정 가능
readFileName.close()