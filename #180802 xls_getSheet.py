import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

#시트 이름 알아내기
print('1', wb.get_sheet_names())

#데이터 시트를 sheet로 부르기
print('2', type(wb.get_sheet_by_name('데이터')))
print('3', wb.get_sheet_by_name('데이터'))

sheet = wb.get_sheet_by_name('데이터')

#시트 이름 출력
print('4', sheet.title)

#활성시트 알아보기
print('5', wb.get_active_sheet())


