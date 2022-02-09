#1
avg = {'국어':95,'영어':90,'수학':80, '과학':50}

average = sum(avg.values())/len(avg)

temp = 0

#2
ans = {i for i in range(1,101) if (i%3==0) or (i%5==0)}
ans2 = ans = {i for i in range(1,101) if (i%3==0) and (i%5==0)}

temp2 = 0

#3
ans3 = [i for i in range(7,-9,-2)]

temp3 = 0

#4
ans4 = tuple(ans3)
print(type(ans4))
