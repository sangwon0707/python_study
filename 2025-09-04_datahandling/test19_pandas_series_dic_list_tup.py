import pandas as pd

# ---------------------------------------------
#Series 시리즈 - 모든 데이터유형 (정수, 문자열, 부동소수점 숫자, 객체등)을 저장 할 수 있는
#1차워 레이블이 지정된 배열
sd1 = pd.Series(['Dog','Cat','tiger','Lion','Monkey'], index=['0','1','2','3','4'])
print(type(sd1))
print(sd1)

# ---------------------------------------------
#딕셔너리 (시리즈)
dic = {1:'a', 2:'b', 3:'c'}

sd2 = pd.Series(dic)
print(type(sd2))
print(sd2)

# ---------------------------------------------
#리스트 (시리즈)
list_data = ['a','b','c']
sd3 = pd.Series(list_data)
print(type(sd3))
print(sd3)

#----------------------------------------------
#튜플 (시리즈)
tup_data = ('a','b','c')
sd4 = pd.Series(tup_data)
print(type(sd4))
print(sd4)