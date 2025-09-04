# pandas의 read_excel() 함수는 내부적으로 엑셀 파일을 처리하기 위한 '엔진'을 사용합니다.
# .xlsx 확장자의 경우, 'openpyxl' 라이브러리가 기본 엔진으로 사용됩니다.
# 따라서 'pip install openpyxl'로 라이브러리가 설치되어 있기만 하면,
# 코드에 직접 'import openpyxl'을 하지 않아도 pandas가 알아서 해당 엔진을 찾아 실행합니다.
# pip install openpyxl

import pandas as pd
file_path = "2025-09-04_datahandling/dataset/bicycle.xlsx"

df = pd.read_excel(file_path)
print(df.head())
