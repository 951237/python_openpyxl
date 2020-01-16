#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 판다스 임포트 #pandas
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

# 불러올 파일 지정하기 #pandas
inputFile = 'lawFather.csv'

# CSV파일을 df(데이터 프레임)로 부르기 #pandas
df = pd.read_csv(inputFile)

# 데이터 프레임에서 소속칼럼에서 특정 문자를 포함한 데이터 인덱싱하기 #pandas #느낀점
kangSchool = df.loc[(df['소속'].str.contains('안산대월초'))]

# 데이터 프레임에서 소속칼럼에서 특정 문자를 포함한 데이터 인덱싱하기 #pandas
choiSchool = df.loc[(df['소속'].str.contains('화현초'))]

# 데이터 프레임에서 소속칼럼에서 특정 문자를 포함한 데이터 인덱싱하기 #pandas
seokSchool = df.loc[(df['소속'].str.contains('학현초'))]

# 안산대월초 부의 금액 #pandas
kangSchool.금액.sum()

# 화현초 부의금액 #pandas
choiSchool.금액.sum()

# 학현초 부의 금액 #pandas
seokSchool.금액.sum()

# CSV파일로 저장하기 #pandas
outFile.to_csv('pandas_lawFile_181008.csv')

# 칼럼의 값을 필터링 하기 #pandas #느낀점
seokAll = df[ df['코드'] == 3 ]

# 칼럼의 값을 합산하기 #pandas
seokAll.금액.sum()

# 칼럼 추출하여 저장하기 #pandas #느낀점
seokAll = seokAll[ [ '소속', '이름','금액' ]]

# 칼럼의 갯수 카운트 하기 #pandas
seokAll.이름.count()

# 값으로 정렬하기 #pandas #느낀점
df.sort_values('소속')

# 값으로 정렬하기 #pandas #느낀점
df.sort_values('소속', ascending=False)

# 값으로 정렬하기 1순위 = 소속, 2순위 = 이름 #pandas #느낀점
df.sort_values(by=['소속', '이름'])

# 값의 숫자를 세어줌 #pandas #느낀점
df2['소속'].value_counts()

# 소속의 중복없는 값을 뽑아내기 #pandas #느낀점
df2['소속'].unique()

# 소속이 초지초인 값만 뽑아내기 #pandas #느낀점
df2.loc[ df2['소속'].isin( [ '초지초' ] ), : ]

# 소속이 초지초인 값만 뽑아내기 #pandas #느낀점
df2.loc[ df2['소속'].isin( [ '초지초', '화현초', '정지초' ] ), : ]

#데이터 프레임에서 원하는 칼럼을 추출하거나, 칼럼 순서 정하기 #pandas #느낀점
df = df[[ '소속', '이름', '금액', '코드']]

#데이터 타입 체크하기 #pandas #느낀점
df.info()

#데이터 null값 체크하기 #pandas #느낀점
df.isnull().sum()

# 빈셀의 값을 더해서 인덱싱 다시 하기 #pandas #느낀점
missing_df = df.isnull().sum().reset_index()

# missing_df 데이터 프레임 칼럼 이름 정하기 #pandas #느낀점
missing_df.columns = ['column', 'count']

# missing_df 데이터 프레임의 비율 칼럼 추가하기 #pandas #느낀점
missing_df['ratio'] = missing_df['count'] / df.shape[0]

# missing_df 데이터 프레임에서 빈셀이 있는 행만 추출하기 #pandas #느낀점
missing_df.loc[ missing_df['ratio'] != 0 ]

#금액별로 그래프 그리기 #pandas #느낀점
df['금액'].value_counts().plot(kind='bar')

#열에서 'object' 타입만 변수로 지정하기 #pandas #느낀점
category_feachure = [col for col in df.columns if df[col].dtypes == 'object']

# todo merged_processed[col]이 의미하는 것음 무엇일까? 
for col in category_feachure:
    merged_processed[col].value_counts().plot(kind='bar')
    plt.title(col)
    plt.show()

# 그래프 그리기 #pandas #느낀점
m_df = seokSchool.groupby( [ '금액', '소속' ] )['소속'].count().unstack('소속')

# 그래프 그리기 제목달고 그래프 크기 정하기 #pandas #느낀점
m_df.plot(kind='bar', figsize=(20,10))
plt.title('money')
plt.show()

# 소속 열에서 학현초, 인교 미술95 값이 들어간 값만 뽑아내기 #pandas #느낀점
df.loc[df2['소속'].isin( ['학현초','인교 미술95'] )]

# 이름열을 정렬하기 #pandas #느낀점
df2_hak.sort_values('이름')

