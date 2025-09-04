import pandas as pd

file_path = "2025-09-04_datahandling/dataset/read.json"
df1 = pd.read_json(file_path)

print(df1)