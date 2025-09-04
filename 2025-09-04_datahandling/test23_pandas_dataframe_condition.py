import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt # 데이터 시각화를 위한 라이브러리
import seaborn as sns # Matplotlib을 기반으로 한 데이터 시각화 라이브러리
import numpy as np

tips = sns.load_dataset("tips") #tip data
print(tips)

print('데이터프레임에서 tip 이 5이상인 데이터 추출')
a = tips[tips.tip > 5]
print(a)

print('남자 손님이면서 비흡연자인 데이터 추출')
b = tips[(tips['sex']=='Male') & (tips['smoker']=='No')]
print(b)

print(' *.isin* *데이터프레임에서 팁을 1달러 지불한 고객 데이터 추출')
c = tips[tips['tip'].isin([1])] 
#영어로 is in "그게 데이터 안에 있냐???"
print(c)