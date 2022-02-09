import sys

# 문자열 복습 : 이스케이프 시퀀스를 무시하는 Python 문법은 r을 붙인다.
path = r'c:\Lab'
urlpath = sys.path
urlpath1 =  sys.path[0]
urlpath2 = sys.path.append(path)

temp = 0