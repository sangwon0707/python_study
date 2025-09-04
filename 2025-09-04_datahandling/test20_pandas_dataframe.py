import pandas as pd

#dictionary (데이터프레임)
dic_df = {'동물':['Dog','Cat','Tiger','Lion'], '나이':[7,9,2,3], '키':[50,30,100,110]}
df1 = pd.DataFrame(dic_df)
print(type(df1))
print(df1)

#list (데이터프레임)
lst_df = [['Dog','7'],['Cat','9'],['Tiger','2'],['Lion','3']]
clm_titles = ['동물', '나이']
df2 = pd.DataFrame(lst_df, columns=clm_titles)
print(type(df2))
print(df2)
