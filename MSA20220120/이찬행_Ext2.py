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

for i in range(len(hong1)):
    sum1 += hong1.values(i)
    sum_all += sum1
    avg1 = sum1

avg1 = sum1/4

for j in range(len(hong2)):
    sum2 += hong2.values(j)
    sum_all += sum2
    avg2 = sum2

avg2 = sum2/4

for k in range(len(hong3)):
    sum3 += hong3.values(k)
    sum_all += sum3
    avg3 = sum3

avg3 = sum3/4

for x in range(len(hong4)):
    sum4 += hong4.values(x)
    sum_all +=sum4
    avg4 = sum4

avg4 = sum4/4

avg_all = (avg1+avg2+avg3+avg4)/len(hong1)