#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import xlrd
import glob

df = pd.DataFrame() #판다에서 데이터 프레임 만들기

print('파일 불러오는 중...')
excelFiles = glob.glob('excel*.xlsx')               #excel로 시작하는 파일 모두 부르기

for f in excelFiles: # 엑셀파일을 하나씩 반복하여 불러오기
    data = pd.read_excel(f, 'Sheet')                # 파일의 'sheet'시트를 읽음. #todo  특정 행만 읽고 싶다. 어떻게?
    # data.index = [os.path.basename(f)] * len(data)  # 파일이름을 데이터 갯수만큼 복사하여 인덱스
    df = df.append(data, ignore_index=True)                            # 인덱스를 0부터 넘버링하여 데이터를 데이터 프레임에 붙이기 todo 1부터 넘버링은 어떻게???
    print('%s을 쓰는 중...' %(f))

a = df[df['PRODUCE'] == 'Okra'].head()
print(a)
# b = df.head()                                                         # 대표적인 값만 보여줌????
# c = df.describe()                                                     # 데이터를 통계값을 정리

#
# df.to_excel('result_excelMergeAll_temp.xlsx')                             # all.xlsx파일로 저장하기
# print('파일 %s개 합치기 완료.' %(len(excelFiles)))