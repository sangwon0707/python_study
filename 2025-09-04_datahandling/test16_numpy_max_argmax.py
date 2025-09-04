#Numpy 의 함수 - max(), argmax()
#벡터나 형렬의 최대값을 알기위해 max()사용
#최댓값을 가지고 잇는 벡터 또는 행렬의 인덱스 값을 알게 argmax()함수 사용

import numpy as np

A = np.array([2,6,3,1])

print("np.max(A)==", np.max(A))
print("np.argmax(A)==", np.argmax(A))

'''
np.max(A)== 6
np.argmax(A)== 1
'''