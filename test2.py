s = "3people unFollowed me"

s = s.lower()
ans = ''
answer = s.split(' ')
for i in range(len(answer)):
    temp = answer[i][0].upper()
    temp = temp + answer[i][1:]
    ans += temp + ' '
tmp = 0