from openpyxl import Workbook
from random import *

wb = Workbook()
ws = wb.active

# 1줄씩 넣기
ws.append(["번호", "영어", "수학"]) # 한줄씩 넣을 때 리스트 형태로 입력
for i in range(1, 11):
	ws.append([i, randint(0, 100), randint(0, 100)])
