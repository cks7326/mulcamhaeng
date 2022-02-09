def LoginProc(inputUserID ,inputUserPWD ):
    # DB 처리해서 아이디와, 비밀번호 가져와야 한다.(별도의 함수 권장)
    if((inputUserID == 'abcde') & (inputUserPWD == '12345')):
        return '로그인 성공 : 이제 이용 가능 웹 사이트로 이동'
    else :
        return '로그인 실패 : 사용자 아이디 및 비밀번호가 잘못 됐습니다, 다시 로그인 이동'


def LoginProcLog(inputUserID ,inputUserPWD ):
    if(inputUserID == 'abcde'):
        if(inputUserPWD == '12345'):
            return '로그인 성공 : 이제 이용 가능 웹 사이트로 이동'
        else:
            print('관리자용 시스템 로그에 아이디 -> 비밀번호 잘못 입력함')
            return '로그인 실패 : 사용자 아이디 및 비밀번호가 잘못 됐습니다, 다시 로그인 이동'
    else :
         print('관리자용 시스템 로그에 아이디 -> 비밀번호 잘못 입력함')
         return '로그인 실패 : 사용자 아이디 및 비밀번호가 잘못 됐습니다, 다시 로그인 이동'