#실행 중에 문제가 발생하면 예외 처리로 문제를 해결
# try : catch 또는 exception
# try :
# 정상일 때 코드 수행
# exception :
# 예외 발생 시 코드 수행
# ------------기본
# 옵션으로 finally -> 정상 또는 예외가 발생해도 꼭 실행해야 하는 것
# else : 비교문하고 예외에서 try 모두 끝나고(정상적으로 실행되고)
# 꼭 실행해야 하는 경우인데 exception 가 발생하면 else 실행되지 않습니다.
# try ~ exception 주로 사용 : 추가 finally 까지만 보통 많이 사용
# 예외가 발생하는 시점은 반복문, 기능을 호출할 때 예외가 발생할 비율이 높음.
# 코드의 가독성 때문에 예외를 남발하지 않는다.




try:
    fileName = open("datalab\\data.txt",mode = "rt" , encoding="utf-8")
except: # 모든 예외사항 처리
    print("오류입니다")
else:
    print("정상적으로 처리 됐습니다.")
    fileName.close()


try:
    #fileName = open("datalab\\data.txt", mode="rt", encoding="utf-8")
    fileName = open("data.txt", mode="rt", encoding="utf-8")
    print("정상")
except: #종합 보험 - 모든 예외 상황 처리하는 사용
    print("비정상")
else:
    fileName.close()
    print("else 구문 실행됨")
#finally: # try 또는 exception 발생해도 무조건 함
    

try:
    fileName = open("data.txt", mode="rt", encoding="utf-8")
except (IndexError,Exception) as ex: # as 별칭: 오류 내용을 ex 저장(문자열 사용 가능)
    error = str(ex)
    print("오류입니다.")
finally: # try 또는 exception 발생해도 무조건 함
    fileName.close() 

# 권장하지 않음
# try:
#     fileName = open("data.txt", mode="rt", encoding="utf-8")
# except Exception as ex: # 다중 예외 처리하고 마지막에 무조건 종합 예외처리를 함
#     error = str(ex) # 종합보험이 먼저 오지 않는다 절대로~
# except IndexError as ex: # as 별칭: 오류 내용을 ex 저장(문자열 사용 가능)
#     error = str(ex)
# finally: # try 또는 exception 발생해도 무조건 함
#     fileName.close()
