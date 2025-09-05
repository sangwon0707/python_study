import pandas as pd

data = {'key1':['a','b','b','c','c'], 'key2':['v','w','w','x','y'], 'col':[1,2,3,4,5]}
df = pd.DataFrame(data, columns=['key1', 'key2','col'])

print(df)
print('-'*50)
#중복데이터가 있는지 확인
df1 = df.duplicated('key1')
print(df1)
print('-'*50)

df2 = df.duplicated('key2')
print(df2)
print('-'*50)

df3 = df.duplicated(['key1','key2'])
print(df3)

print('-'*50)
#중복데이터 시작과 끝 확인
df.duplicated(['key1'], keep='first')
df.duplicated(['key1'], keep='last')
df.duplicated(['key1'], keep=False)

#중복데이터 제거
df.drop_duplicates(['key1'], keep='first')
df.drop_duplicates(['key1'], keep='last')
df.drop_duplicates(['key1'], keep=False)