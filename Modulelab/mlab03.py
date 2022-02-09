# 엑셀을 받아서 처리하는 것 보다 쉽게 Pandas 해보면 어떨까?

import pandas as pd # 별칭으로 쉽게 사용할 수 있도록 줄여서 쓴다.

resultData = pd.read_excel("modulelab\\data4.xlsx")

#print(resultData)
resultData.to_csv("modulelab\\data4.csv")
