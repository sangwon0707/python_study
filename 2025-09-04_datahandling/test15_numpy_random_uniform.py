'''
#노이즈가 있는 데이터 생성에 응용할 수 있다.
#random.rand() 함수는 0~1사이의 임의의
#실수값을 얻고자 할때 사용하는 넘파이 함수
'''

import numpy as np

number1 = np.random.rand(3)
number2 = np.random.rand(1,3)
number3 = np.random.rand(3,1)
print("random_number1 ==", number1)
print("random_number2 ==", number2)
print("random_number3 ==", number3)

'''
`numpy.random.rand()`를 사용한 예제 코드:
10과 20 사이의 난수 5개 생성
(20 - 10) * np.random.rand(5) + 10
'''
random_numbers = 10 * np.random.rand(5) + 10
print(random_numbers) # [15.6136111  12.12899536 18.99886849 14.94368995 17.8535621 ]

'''
#numpy.random.uniform() 사용하기 (권장)
#Numpy는 특정 범위 내에서 균일 분포의 난수를 생성하는 uniform() 함수를 직접
#제공합니다. 이 방법이 더 명확하고 직관적입니다.
#np.random.uniform(low, high, size)

# *low: 범위의 최솟값 (기본값 0.0)
# *high: 범위의 최댓값 (이 값은 범위에 포함되지 않음)
# * size: 생성할 난수의 개수 또는 형태
'''

# 10과 20 사이의 난수 5개 생성
random_numbers = np.random.uniform(10, 20, 5)
print(random_numbers) #[11.55966441 19.82339328 10.74947892 13.24779892 16.87249348]