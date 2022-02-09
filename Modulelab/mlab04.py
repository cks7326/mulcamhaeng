# 차트 (시각적 요소)
# matplotlib 
# 데이터 활용하여 처리 및 출력 : pandas (numpy) , matplotlib

import pandas as pd
import matplotlib.pyplot as plt



# plt.title("랩 라인 플롯 출력")
# plt.plot([19,12,3,124,34],[123,43,123,432,532])
# plt.show()

# plt.title("Line Print Lab")
# plt.plot([19,12,3,124,34],[123,43,123,432,532])
# plt.xlabel = "x line"
# plt.ylabel = "y line"
# plt.legend(["1st","2nd"])
# plt.show()

csvData = pd.read_csv("modulelab\\data4.csv")
plt.bar(csvData.ID,csvData["수학"]) # x,y

temp = 0