import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt # 데이터 시각화를 위한 라이브러리
import seaborn as sns # Matplotlib을 기반으로 한 데이터 시각화 라이브러리
import numpy as np

tips = sns.load_dataset("tips") #tip data
print(tips)
print("----------------------------------------------------------------")
print('total_bill기준으로 axis=0 인덱스를 오름차순(기본설정)으로 정렬')
print(tips.sort_values(by=['total_bill'], axis=0))

print("----------------------------------------------------------------")
print('total_bill기준으로 axis=0 인덱스를 내림차순으로 정렬')
print(tips.sort_values(by=['total_bill'], axis=0, ascending=False))

print("----------------------------------------------------------------")
print('컬럼을 알파벳 순으로 정렬')
print(tips.sort_index(axis = 1))

print("----------------------------------------------------------------")
print('한행의 값들의 합계를 계산(숫자인 열만 계산)')
print(tips.sum(axis=1, numeric_only=True))

print("----------------------------------------------------------------")
print('한열의 값들의 합계를 계산(숫자인 열만 계산)')
print(tips.sort_index(axis = 1))