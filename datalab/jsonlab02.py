#파일 열기 - 기본적으로 제공

# fileName = open("파일명",mode="",encoding="utf-8")
# mode : 읽기 r ,쓰기 w 또는 x ,내용추가 a ,수정 +
# mode : 파일 형식도 지정 : t - 텍스트 형식의 파일, b-이미지, 영상 같은 것(바이너리 파일)
# 실무에서 주의점 : 파일 위치를 찾기 import os 에 있는 Path를 활용
# 파일을 읽고 쓰고 나면 거의 대부분 close 기능을 호출 하는 것을 습관

import os
import sys


test = os.path.abspath(__file__) # 현재 경로의 파일 이름
test1 = os.getcwd()

# 최상위 경로는 C:LAB\\
fileName = open("datalab\\data.txt",mode = "rt", encoding = "utf-8")


#data1 = fileName.readlines()

for i in fileName:
    sys.stdout.writelines(i) # stdout은 출력

# with open("datalab\\data.txt",'rt', encoding = "utf-8"):
    

fileName.close()

temp = 0