#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import xlrd

df = pd.DataFrame() #판다에서 데이터 프레임 만들기

for f in ['excelMerge01.xlsx','excelMerge02.xlsx']: # 엑셀파일을 하나씩 반복하여 불러오기
    data = pd.read_excel(f, 'Sheet')                # 파일의 'sheet'시트를 읽음. #todo  특정 행만 읽고 싶다. 어떻게?
    data.index = [os.path.basename(f)] * len(data)  # 파일이름을 데이터 갯수만큼 복사하여 인덱스
    df = df.append(data)                            # 데이터를 데이터 프레임에 붙이기

df.to_excel('all.xlsx')                             # all.xlsx파일로 저장하기