import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt # 데이터 시각화를 위한 라이브러리
import seaborn as sns # Matplotlib을 기반으로 한 데이터 시각화 라이브러리
import numpy as np

tips = sns.load_dataset("tips") #tip data
print(tips)

'''
 * titanic: 타이타닉호 승객들의 생존 여부, 좌석 등급, 성별, 나이 등의      
     정보를 담고 있습니다. (분류 문제에 많이 사용)
   * tips: 레스토랑에서 팁을 지불한 손님의 정보를 담은 데이터입니다. (총     
     결제액, 팁, 성별, 흡연 여부, 요일 등)
   * iris: 붓꽃의 품종과 꽃받침, 꽃잎의 크기 정보를 담고 있습니다.
     (머신러닝의 고전적인 분류 예제)
   * flights: 1949년부터 1960년까지의 월별 국제선 항공 승객 수
     데이터입니다. (시계열 분석에 사용)
   * penguins: 펭귄의 종, 서식지, 부리 길이, 몸무게 등 다양한 측정값을       
     포함합니다.
   * diamonds: 다이아몬드의 캐럿, 컷, 색상, 투명도, 가격 등의 특성
     정보를 가지고 있습니다.
   * mpg: 자동차 모델별 연비(갤런 당 마일)와 실린더, 마력, 무게 등의
     정보를 담고 있습니다.
'''