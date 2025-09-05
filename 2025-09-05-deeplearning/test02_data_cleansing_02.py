import pandas as pd
file_path = "2025-09-05-deeplearning/dataset/bicycle.csv"
df = pd.read_csv(file_path, engine='python', encoding='cp949')
df
print(df)

#결측데이터 대체
df_1 = df.fillna(0)
print(df_1)

#특정 컬럼 결측값을 특정값(0)으로 대체
df_2 = df.이용거리.fillna(0)
print(df_2)

#결측값을 문자열('missing')으로 대체)
df_3 = df.fillna('missing')
print(df_3)

df_4 = df.fillna(df.mean)
print(df_4)

df_5 = df.이용거리.mean
print(df_5)

df_6 = df.fillna(df.이용거리.mean())
print(df_6)

df_7 = df.이용거리.fillna(df.이용거리.mean())
print(df_7)

