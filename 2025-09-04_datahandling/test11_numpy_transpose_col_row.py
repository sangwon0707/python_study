#Numpy 전치 행렬_transpose
#원본 행렬의 열은 행으로, 행은 열로 바꾼것을 전치 행렬이라고 하며
#numpy에서는 원본행렬에 T연산자를 이용하여 구할 수 있다.

import numpy as np

A = np.array([[1,2],[3,4],[5,6]])
B = A.T

print("A.shape==",A.shape)
print("B.shape==",B.shape)

print(A)
print(B)