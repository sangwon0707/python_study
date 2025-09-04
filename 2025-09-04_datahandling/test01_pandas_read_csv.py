# =================================================================
# Pandas 주요 기능 요약 (Pandas Key Features Summary)
# =================================================================

# 1. 데이터 구조 (Data Structures)
# - Series: 1차원 배열 형태의 데이터 구조. (예: df['컬럼명'])
# - DataFrame: 2차원 테이블 형태의 데이터 구조. (가장 많이 사용)

# 2. 데이터 입출력 (Data I/O)
# - pd.read_csv('file.csv'): CSV 파일 읽기
# - df.to_csv('file.csv'): DataFrame을 CSV 파일로 저장
# - pd.read_excel('file.xlsx'): Excel 파일 읽기
# - df.to_excel('file.xlsx'): DataFrame을 Excel 파일로 저장
# - pd.read_json('file.json'): JSON 파일 읽기
# - df.to_json('file.json'): DataFrame을 JSON 파일로 저장
# - pd.read_sql(query, connection): SQL 데이터베이스에서 데이터 읽기

# 3. 데이터 선택 및 인덱싱 (Data Selection & Indexing)
# - df['컬럼명']: 특정 컬럼 선택 (Series 반환)
# - df[['컬럼1', '컬럼2']]: 여러 컬럼 선택 (DataFrame 반환)
# - df.loc[행_레이블, 열_레이블]: 레이블 기반 선택 (예: df.loc[0, '컬럼명'])
# - df.iloc[행_인덱스, 열_인덱스]: 정수 인덱스 기반 선택 (예: df.iloc[0, 1])
# - 조건부 선택 (Boolean Indexing):
#   - df[df['나이'] > 30]: '나이'가 30보다 큰 행만 선택
#   - df[(df['나이'] > 30) & (df['도시'] == '서울')]: 여러 조건 결합

# 4. 데이터 정제 (Data Cleaning)
# - df.isnull().sum(): 결측치(NaN) 개수 확인
# - df.dropna(): 결측치가 있는 행 또는 열 제거
# - df.fillna(값): 결측치를 특정 값으로 채우기

# 5. 데이터 조작 및 변환 (Data Manipulation & Transformation)
# - df.groupby('컬럼명'): 특정 컬럼으로 데이터 그룹화
#   - 예: df.groupby('부서')['월급'].mean(): 부서별 평균 월급 계산
# - pd.merge(df1, df2, on='기준컬럼'): 두 DataFrame을 특정 컬럼 기준으로 병합
# - pd.concat([df1, df2]): 두 DataFrame을 위아래 또는 옆으로 이어붙이기
# - df.apply(함수): 각 행 또는 열에 함수 적용
# - df.sort_values(by='컬럼명'): 특정 컬럼 기준으로 데이터 정렬
# - df.drop('컬럼명', axis=1): 특정 컬럼 제거

# 6. 기초 통계 (Basic Statistics)
# - df.describe(): 주요 기술 통계량 요약 (개수, 평균, 표준편차, 최소/최대값 등)
# - df.mean(), df.sum(), df.min(), df.max(), df.std(), df.var(): 각 통계량 계산
# - df['컬럼명'].value_counts(): 특정 컬럼의 값별 개수 계산

# 7. 시각화 (Visualization)
# - df.plot(kind='line', x='x축', y='y축'): 간단한 그래프 그리기 (matplotlib 기반)
#   - kind 종류: 'line', 'bar', 'hist', 'scatter', 'pie' 등

# =================================================================

# pandas에서 DataFrame을 csv 파일로 저장하는 방법
# DataFrame.to_csv('파일이름.csv', index=False, encoding='utf-8-sig')
# index=False: DataFrame의 인덱스를 파일에 포함하지 않음
# encoding='utf-8-sig': Excel에서 한글이 깨지지 않도록 설정
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#pandas.read_csv

import pandas as pd
file_path = "2025-09-04_datahandling/dataset/bicycle.csv"
df1 = pd.read_csv(file_path, engine='python', encoding='cp949')
df1
print(df1)
print(df1.head())
