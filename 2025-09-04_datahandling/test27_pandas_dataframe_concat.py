import pandas as pd
s1 = pd.Series([0,1], index=['A','B'])
s2 = pd.Series([2,3,4], index=['c','d','e'])

print("[ concat 수직연결 결과 ]")
print(s1)
print("----------------------------------------------")
print(s2)
print("----------------------------------------------")
s3 = pd.concat([s1, s2])
print(s3)

print("")

print("----------------------------------------------")
print("[ concat 수평연결 결과 ]")

df1 = pd.DataFrame([['Dog',3],['Bird',10],['Tiger',6]], index=['0','1','2'], columns=['동물','나이'])
print(df1)
print("----------------------------------------------")

df2 = pd.DataFrame([['집',0],['초원',0],['수풀',0]], index=['0','1','2'], columns=['사는곳','뿔의 개수'])
print(df2)
print("----------------------------------------------")

df3 = pd.concat([df1, df2], axis=1)
print(df3)

# s1과 s2의 concat은 두 Series를 수직으로(위아래로) 연결합니다.
# 기본 axis=0으로 동작하며, s2가 s1의 아래에 붙는 형태로 새로운 Series가 생성됩니다.
#
# df1과 df2의 concat은 axis=1 옵션으로 인해 두 DataFrame을 수평으로(좌우로) 연결합니다.
# 두 DataFrame의 인덱스가 동일하므로, 각 인덱스에 해당하는 행들이 옆으로 합쳐져서
# '동물', '나이', '사는곳', '뿔의 개수' 열을 모두 포함하는 새로운 DataFrame이 생성됩니다.
