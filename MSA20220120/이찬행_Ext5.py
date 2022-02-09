hong1 = {'국어':95, '영어':90, '수학':80, '과학':50}
hong2 = {'국어':100, '영어':50, '수학':90, '과학':90}
hong3 = {'국어':99, '영어':60, '수학':100, '과학':40}
hong4 = {'국어':55, '영어':80, '수학':80, '과학':60}

all_hong = [hong1, hong2, hong3, hong4]
all_sum = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
all_average = 0
for i in range(len(all_hong)):
    all_sum += all_hong[i].values()
    if i == 0:
        sum1 = all_sum
        avg1 = all_sum/(len(hong1))
        all_average += avg1
    elif i == 1:
        sum2 = all_sum
        avg2 = all_sum/(len(hong2))
        all_average += avg2
    elif i == 2:
        sum3 = all_sum
        avg3 = all_sum/(len(hong3))
        all_average += avg3
    else :
        sum4 = all_sum
        avg4 = all_sum/(len(hong4))
        all_average += avg4

all_average /= 4 

