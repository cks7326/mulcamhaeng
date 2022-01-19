#1
avg = {'국어':95,'영어':90,'수학':80, '과학':50}

average = sum(avg.values())/len(avg)

temp = 0

#2

ans2 = {i for i in range(1,101) if i%3==0} 
ans3 = {i for i in range(1,101) if i%5==0} 
ans = ans2 | ans3

temp2 = 0

#3
ans4 = [i for i in range(7,-9,-2)]

temp3 = 0

#4
ans5 = tuple(ans4)

