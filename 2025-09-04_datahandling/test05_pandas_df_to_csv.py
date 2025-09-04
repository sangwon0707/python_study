import pandas as pd
file_path = "2025-09-04_datahandling/dataset/bicycle.csv"
df1 = pd.read_csv(file_path, engine='python', encoding='cp949')
df1
# print(df1)
# print(df1.head())

#현재 데이터프레임을 csv로 내보내기, sample_data.csv
print("[DataFrame을 csv로 내보내기]")
df1.to_csv('2025-09-04_datahandling/dataset/sample_data.csv')

#내보내진 csv를 경로를 지정하여 읽어와지는지 확인하기
file_path = '2025-09-04_datahandling/dataset/sample_data.csv'
df2 = pd.read_csv(file_path)
print(df2)