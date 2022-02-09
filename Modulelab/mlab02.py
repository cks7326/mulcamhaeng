import openpyxl

#엑셀 파일 열기
sheetData1 = openpyxl.load_workbook("modulelab\\data.xlsx") # 경로 주의

#열기가 된 엑셀파일의 시트 가져오기
worksheet1 = sheetData1.active
# 특정 시트를 가져올때에는 get_

for data in range(1,5):
    for info in range(1,5):
        worksheet1.cell(row=data, column=info, value=1)

sheetData1.save("modulelab\\data22.xlsx")
sheetData1.close()

