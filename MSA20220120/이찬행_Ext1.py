hong1 = {'국어':95, '영어':90, '수학':80, '과학':50}
hong2 = {'국어':100, '영어':50, '수학':90, '과학':90}
hong3 = {'국어':99, '영어':60, '수학':100, '과학':40}
hong4 = {'국어':55, '영어':80, '수학':80, '과학':60}


sum1 = sum(hong1.values())
avg1 = sum(hong1.values())/len(hong1)

sum2 = sum(hong2.values())
avg2 = sum(hong2.values())/len(hong2)

sum3 = sum(hong3.values())
avg3 = sum(hong3.values())/len(hong3)

sum4 = sum(hong4.values())
avg4 = sum(hong4.values())/len(hong4)


sum_all = sum1+sum2+sum3+sum4
avg_all = (sum_all/4)/4

temp = 0