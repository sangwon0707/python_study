import pandas as pd
file_path = "2025-09-05-deeplearning/dataset/bicycle.csv"
df = pd.read_csv(file_path, engine='python', encoding='cp949')
df
print(df)
print(df.head())

#결측데이터 확인
print(df.isnull())

#결측데이터 확인
print(df.notnull())

#결측데이터 개수 확인
print(df.isnull().sum())

#행단위로 계측값 개수 구하기
print(df.isnull().sum(1))

#행단위로 계측값 개수 구하기
print(df.notnull().sum(1))

##결측데이터 행 제거
df_drop_allrow = df.dropna(axis = 0)
print(df_drop_allrow)

##결측데이터 열 제거
df_drop_allcolumn = df.dropna(axis = 1)
print(df_drop_allcolumn)

#행별 데이터 개수
print(df['대여거치대'].dropna())

# ------------------------------------------------------------
#특정 열에 대한 결측 데이터 행 제거
a = df[['대여소번호', '대여거치대', '이용시간']].dropna()
b = df[['대여소번호', '대여거치대', '이용시간']].dropna(axis=0)
print(a)
print(b)

#특정 열에 대한 결측 데이터 열 제거
c = df[['대여소번호', '대여거치대', '이용시간']].dropna(axis=1)
print(c)

#-------------------------------------------------------------
#결측값을 특정 값으로 채우기: df.fillna(0)
print(df.fillna(0))

#결측값을 특정 문자열로 채우기: df.fillna(' ')
print(df.fillna(' '))

#결측값을 변수별 평균으로 대체: df.fillna(df.mean)
print(df.fillna(df.mean))

