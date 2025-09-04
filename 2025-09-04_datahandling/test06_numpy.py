# =================================================================
# NumPy 주요 기능 요약 (NumPy Key Features Summary)
# =================================================================

# NumPy(Numerical Python)는 파이썬에서 과학 계산을 위한 핵심 라이브러리입니다.
# 다차원 배열(ndarray) 객체를 중심으로 다양한 데이터 처리 기능을 제공합니다.

import numpy as np

# 1. ndarray 생성 (Creating ndarrays)
# - 리스트나 튜플로부터 생성
arr = np.array([1, 2, 3, 4, 5])
print(f"1. 리스트로 생성: {arr}")

# - 특정 값으로 채워진 배열 생성
zeros_arr = np.zeros((2, 3))  # 2x3 크기의 0으로 채워진 배열
ones_arr = np.ones((3, 2))   # 3x2 크기의 1로 채워진 배열
print(f"   0으로 채운 배열:\n {zeros_arr}")
print(f"   1로 채운 배열:\n {ones_arr}")

# - 연속된 값으로 배열 생성
range_arr = np.arange(0, 10, 2)  # 0부터 10까지 2씩 증가하는 배열
linspace_arr = np.linspace(0, 1, 5) # 0과 1 사이를 5개의 일정한 간격으로 나눈 배열
print(f"   arange 배열: {range_arr}")
print(f"   linspace 배열: {linspace_arr}")


# 2. 배열의 속성 (Array Attributes)
# - arr.shape: 배열의 각 차원의 크기 (튜플)
# - arr.dtype: 배열 요소의 데이터 타입
# - arr.ndim: 배열의 차원 수
# - arr.size: 배열의 전체 요소 개수
print(f"\n2. 배열 속성: shape={arr.shape}, dtype={arr.dtype}, ndim={arr.ndim}, size={arr.size}")


# 3. 인덱싱 및 슬라이싱 (Indexing and Slicing)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n3. 2D 배열:\n {arr2d}")
# - 특정 요소 접근
print(f"   arr2d[1, 2]: {arr2d[1, 2]}" ) # 2번째 행, 3번째 열 -> 6
# - 슬라이싱
print(f"   arr2d[:2, 1:]:\n {arr2d[:2, 1:]}") # 처음 2개 행과, 2번째 열부터 끝까지
# - 불리언 인덱싱 (Boolean Indexing)
print(f"   arr2d[arr2d > 5]: {arr2d[arr2d > 5]}") # 5보다 큰 요소만 선택


# 4. 배열 연산 (Array Operations)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# - 요소별 연산 (Element-wise operations)
print(f"\n4. 요소별 덧셈: {a + b}")
print(f"   요소별 곱셈: {a * b}")
# - 유니버설 함수 (Universal Functions, ufunc)
print(f"   제곱근: {np.sqrt(a)}")
print(f"   지수: {np.exp(a)}")


# 5. 주요 함수 (Key Functions)
# - 통계 함수
print(f"\n5. 합계: {arr.sum()}, 평균: {arr.mean()}, 표준편차: {arr.std()}")
# - 배열 형태 변경
reshaped_arr = np.arange(6).reshape(2, 3)
print(f"   형태 변경 (2,3):\n {reshaped_arr}")
# - 전치 행렬
print(f"   전치 행렬:\n {reshaped_arr.T}")
# - 선형대수 (dot product)
print(f"   벡터 내적: {np.dot(a, b)}")

# =================================================================
