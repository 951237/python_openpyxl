# 201208_TIL_openpyxl_셀의 갯수를 모를 때 
```python
from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

#셀의 개수를 모를때 
for x in range(1, ws.max_row+1): #엑셀의 셀은 1부터 시작. 가장 끝줄은 +1
	for y in range(1, ws.max_column +1):
		print(ws.cell(row=x, column=y).value, end=" ")
		print()
```

#코딩/TIL #snippet/python/openpyxl