#데이터프레임의 행의 개수 확인 df.count()
#데이터프레임의 인덱스 정보 보기 df.index
#데이터프레임의 컬럼 정보 보기 df.columns
#데이터프레임의 데이터 내역 보기 df.values

import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt # 데이터 시각화를 위한 라이브러리
import seaborn as sns # Matplotlib을 기반으로 한 데이터 시각화 라이브러리
import numpy as np

tips = sns.load_dataset("tips") #tip data
print(tips)
print("----------------------------------------------------------------")
print("행의 갯수:")
print(tips.count())
print("----------------------------------------------------------------")

print("인덱스정보")
print(tips.index)
print("----------------------------------------------------------------")

print("컬럼정보")
print(tips.columns)
print("----------------------------------------------------------------")

print("데이터내역")
print(tips.values)

'''
결과
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

[244 rows x 7 columns]
----------------------------------------------------------------
행의 갯수:
total_bill    244
tip           244
sex           244
smoker        244
day           244
time          244
size          244
dtype: int64
----------------------------------------------------------------
인덱스정보
RangeIndex(start=0, stop=244, step=1)
----------------------------------------------------------------
컬럼정보
Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='object')
----------------------------------------------------------------
데이터내역
[[16.99 1.01 'Female' ... 'Sun' 'Dinner' 2]
 [10.34 1.66 'Male' ... 'Sun' 'Dinner' 3]
 [21.01 3.5 'Male' ... 'Sun' 'Dinner' 3]
 ...
 [22.67 2.0 'Male' ... 'Sat' 'Dinner' 2]
 [17.82 1.75 'Male' ... 'Sat' 'Dinner' 2]
 [18.78 3.0 'Female' ... 'Thur' 'Dinner' 2]]
'''