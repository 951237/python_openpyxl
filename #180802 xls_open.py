import openpyxl

#시트 열기
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))