import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt # 데이터 시각화를 위한 라이브러리
import seaborn as sns # Matplotlib을 기반으로 한 데이터 시각화 라이브러리
import numpy as np

tips = sns.load_dataset("tips") #tip data
print(tips)
print("**'smoker'의 타입이 Category로 분류된 오리지날 데이터 프레임")
print(tips.dtypes)
print("----------------------------------------------------------------")
print("**현재 행을 그대로 타입변경(object(str))")
tips['smoker'] = tips['smoker'].astype(str)
print(tips.dtypes)

print("----------------------------------------------------------------")
print("**타입(object(str)으로 변경된 행을 추가")
# 이름을 다르게 하면 변수가 행이름이 추가된다?!!!
tips['smoker_str'] = tips['smoker'].astype(str)
print(tips.dtypes)
print("----------------------------------------------------------------")
print("**타입(object(str))이 변경된 새로운 행(smoker_str)이 추가된 데이터프레임")
print(tips)