'''
*행데이터 조작
1) 인덱스 읽기 (위치 location)
loc로 행 데이터 추출하기
df.loc[인덱스이름]
df.loc[인덱스이름1, 인덱스이름2, 인덱스이름n]

2) 행번호 읽기 (information in location)
- iloc 속성으로 행 데이터 읽어오기
df.iloc[행번호]
- iloc을 통해 마지막 행 데이터 가져오기
df.iloc[-1]

3) 특정행 범위 영역을 선택
df[시작행: 마지막행]

4) 조건을 이용하여 선택하기
기본 조건식: and(&), or(|), not(~), 비교(==)

5) 특정 조건 선택
df.isin(values)
'''
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt # 데이터 시각화를 위한 라이브러리
import seaborn as sns # Matplotlib을 기반으로 한 데이터 시각화 라이브러리
import numpy as np

tips = sns.load_dataset("tips") #tip data
print(tips)

print("-"*70)
print("데이터프레임에서 3개의 행을 추출")
print(tips[0:3]) #데이터프레임에서 3개의 행을 추출

print("-"*70)
print("데이터프레임에서 행번호 0부터 3개를 추출")
print(tips.iloc[0:3]) #데이터프레임에서 행번호 0부터 3개를 추출

print("-"*70)
print("데이터프레임에서 인덱스번호 0부터 3까지 추출")
print(tips.loc[0:3]) #데이터프레임에서 인덱스번호 0부터 3까지 추출

print("-"*70)
print("데이터프레임에서 인덱스 번호0부터 3까지 데이터에서 total_bill, day 컬럼 내용 추출")
print(tips.loc[0:3,['total_bill', 'day']])
#데이터프레임에서 인덱스 번호0부터 3까지 데이터에서 total_bill, day 컬럼 내용 추출

'''
매우 중요한 포인트입니다. .iloc를 사용하는 이유는 코드의 명확성과 예측 가능성을 높이기
위함이며, 특히 인덱스가 기본 정수(0, 1, 2...)가 아닐 때 그 차이가 명확해집니다.
인덱스가 숫자가 아닐 경우
만약 데이터프레임의 인덱스가 아래와 같이 문자열이라면 어떻게 될까요?

**정리:
df[...]는 간단해 보이지만, 행을 찾는지 열을 찾는지, 위치를 쓰는지 레이블을 쓰는지
헷갈릴 수 있습니다. 반면 .loc와 .iloc는 항상 정해진 규칙대로만 작동하므로, 누가 봐도
명확하고 안정적인 코드를 작성할 수 있게 해줍니다.
'''


print("-"*70)
print("데이터프레임에서 인덱스 번호의 0의 데이터에서 total_bill, day 컬럼의 데이터 추출")
print(tips.loc[0,['total_bill', 'day']])
#데이터프레임에서 인덱스 번호의 0의 데이터에서 total_bill, day 컬럼의 데이터 추출

print("-"*70)
print("데이터 프레임에서 특정 인덱스 번호, 컬럼(time)의 데이터 추출")
print(tips.loc[0,'time'])
#데이터 프레임에서 특정 인덱스 번호, 컬럼(time)의 데이터 추출