import pandas as pd
file_path = "2025-09-04_datahandling/dataset/bicycle.csv"
df1 = pd.read_csv(file_path, engine='python', encoding='cp949')
df1
# print(df1)
# print(df1.head())

#현재 데이터프레임을 xlsx로 내보내기, sample_data.csv
print("[DataFrame을 xlsx(엑셀)로 변환하여 읽어오기]")
df1.to_excel('2025-09-04_datahandling/dataset/sample_data.xlsx')

#내보내진 xlsx를 경로를 지정하여 읽어와지는지 확인하기
file_path = '2025-09-04_datahandling/dataset/sample_data.xlsx'
df2 = pd.read_excel(file_path)
print(df2)