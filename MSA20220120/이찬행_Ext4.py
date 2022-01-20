hong1 = [95, 90, 80, 50]
hong2 = [100, 50, 90, 90]
hong3 = [99, 60, 100, 40]
hong4 = [55, 80, 80, 60]

sum1=[]
sum2=[]
sum3=[]
sum4=[]
sum_all = 0
avg_all = 0

if len(hong1) > 1 :
    for i in range(len(hong1)):
        sum1.append(hong1[i])
        sum_all += sum1[i]
        

if len(hong2) > 1 :
    for i in range(len(hong2)):
        sum2.append(hong2[i])
        sum_all += sum2[i]

if len(hong3) > 1 :
    for i in range(len(hong3)):
        sum3.append(hong3[i])
        sum_all += sum3[i]

if len(hong4) > 1 :
    for i in range(len(hong4)):
        sum4.append(hong4[i])
        sum_all += sum4[i]


