# 이미지 처리 : 바이너리 처리
# 글씨 일 경우에만 utf-8 합니다.

# with open("datalab\\pic.jpg","rb") as fileName:
#     byteProcess = fileName.read(1)
#     while byteProcess !=b"":
#         print(byteProcess)
#         byteProcess = fileName.read(1)


try :
    
    fileName1 = open("datalab\\pic.jpg","rb")
    a = [1,2,3]
    print(a[3])
except Exception as ex :
    print(ex)
else:
    fileName1.close()
    print("정상 작동")

temp = 0
