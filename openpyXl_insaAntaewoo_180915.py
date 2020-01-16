#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import xlrd
import glob

df = pd.DataFrame() #판다에서 데이터 프레임 만들기
sheetWanted = 'DATA'

print('파일 불러오는 중...')
excelFiles = glob.glob('안산*.xls')               #excel로 시작하는 파일 모두 부르기

for f in excelFiles: # 엑셀파일을 하나씩 반복하여 불러오기
    data = pd.read_excel(f, sheetWanted)                # 파일의 'sheet'시트를 읽음. #todo  특정 행만 읽고 싶다. 어떻게?
    df = df.append(data, ignore_index=True)                            # 인덱스를 0부터 넘버링하여 데이터를 데이터 프레임에 붙이기 todo 1부터 넘버링은 어떻게???
    print('%s을 쓰는 중...' %(f))

print(df)
df.to_excel('result_insaAntaewoo.xlsx')                             # all.xlsx파일로 저장하기
print('파일 %s개 합치기 완료.' %(len(excelFiles)))