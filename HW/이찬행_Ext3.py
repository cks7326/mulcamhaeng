hong1 = {'국어':95, '영어':90, '수학':80, '과학':50}
hong2 = {'국어':100, '영어':50, '수학':90, '과학':90}
hong3 = {'국어':99, '영어':60, '수학':100, '과학':40}
hong4 = {'국어':55, '영어':80, '수학':80, '과학':60}

sum1=0
sum2=0
sum3=0
sum4=0
sum_all = 0
avg_all = 0

i=0
while i < len(hong1):
    sum1 += hong1.values(i)
    i += 1
avg1 = sum1/(len(hong1))

j=0
while j < len(hong2):
    sum2 += hong2.values(j)
    j += 1
avg2 = sum2/(len(hong2))

k=0
while k < len(hong3):
    sum3 += hong3.values(k)
    k += 1
avg3 = sum3/(len(hong3))

x=0
while x < len(hong4):
    sum4 += hong4.values(x)
    x += 1
avg4 = sum4/(len(hong4))

sum_all = (hong1.values())+(hong2.values())+(hong3.values())+(hong4.values())
avg_all = (sum_all / len(hong1))/4