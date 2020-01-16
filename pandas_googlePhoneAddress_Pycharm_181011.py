#!/usr/bin/env python
# coding: utf-8

# 판다스 임포트 #pandas
import numpy as np
import pandas as pd
import chardet
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

# 불러올 파일 지정하기 #pandas
inputFile = 'pandas_googleAddress.csv'

# CSV파일을 df(데이터 프레임)로 부르기 #pandas
df = pd.read_csv(inputFile, encoding='utf-8')

# 데이터 프레임에서 원하는 열을 뽑아서 다른 데이터 프레임으로 저장 #pandas #느낀점
dfSel_01 = df[['First Name', 'Middle Name','Last Name','Mobile Phone','Other Phone','Notes','E-mail Address','E-mail 2 Address']]

# 데이터 프레임의 정보를 확인하기
dfSel_01.info()

# 특정열의 빈값을 삭제하여 반영하기 #느낀점 #pandas
dfSel_01.dropna(subset=['Mobile Phone'], inplace=True)

# 좌측 열의 값을 우측 열의 빈칸에 채우기 #느낀점 #pandas
dfSel_01['First Name'].fillna(dfSel_01['Middle Name'], inplace = True)

# 두개의 열을 한꺼번에 지우기 #느낀점 #pandas
dfSel_01.drop(['Last Name','Middle Name'], axis=1, inplace=True)

# 데이터 프레임의 인덱싱을 새롭게 지정하기 #느낀점 #pandas
dfSel_01.reset_index(drop=True, inplace=True)

dfSel_01.drop('index', axis=1, inplace=True)

# 데이터 프레임 엑셀파일로 저장하기 #pandas
dfSel_01.to_excel('pandas_googleAddress_181012.xlsx')


# In[ ]:




