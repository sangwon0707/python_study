'''
#Numpy 행렬 원소 접근
- 행렬 원소에 접근하는 방식으로 indexing과 slicing이 있음 (Vector DB?!)

# Indexing
# 행렬의 원소를 접근할 경우 대괄호 안에서 , 를 기준으로 
왼쪽은 행, 오른쪽은 열을 나태내고 있는 것을 알수있다.
ex) A[0,0] 은 인덱스 0행 0렬의 있는 요소를 가져오라고 하는 것.

# Slicing
# A[:,0] 의미는 모든 행(row)에 대해서 인덱스가 0인 열(column), 즉 1열인 원소 [10,30,50]을 가져오라는 의미
'''

import numpy as np

A = np.array([[10,20],[30,40],[50,60]])

print('A.shape==', A.shape)
print(A)

print(A[0,0]) #0번 행 인덱스의 0번열 인덱스 = 10
print(A[2, 1]) #2번 행 인덱스의 1번열 인덱스 = 60
print(A[ : ,0]) #모든행에 대해서 0번열 인덱스 = [10,30,50]
print[A[0 : -1, 1 : 2]] 
print(A[ : , :])
