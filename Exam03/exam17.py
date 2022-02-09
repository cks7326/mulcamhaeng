# 모듈 가져오기 연습 - 지금은 패키지 갖다 쓰기(디렉터리)


from User_login.LoginProcess  import LoginProc, LoginProcLog

if __name__ == '__main__' :
    uid = 'abcde'
    pwd = '1234'

    result1 = LoginProc(uid,pwd)
    print(result1)
    result2 = LoginProcLog(uid,pwd)
    print(result2)

    temp = 0