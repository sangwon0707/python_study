# round() 함수는 숫자를 가장 가까운 정수로 반올림합니다.
# .5의 경우, 짝수 정수로 반올림합니다 (Python 3).
#round 반올림
a = 5.9
print(round(a)) # a(5.9)를 반올림하여 6을 출력합니다.
print(round(5.3)) # 5.3을 반올림하여 5를 출력합니다.

# math.sin() 함수는 라디안 단위의 각도에 대한 사인 값을 계산합니다.
#sin 사인
import math
# 3 * pi / 2 라디안은 270도이며, 사인 값은 -1입니다.
b = math.sin(3 * math.pi / 2)
print(b) # b 값을 출력합니다. (-1.0)

# sqr 제곱
# 숫자를 제곱하려면 ** 연산자나 pow() 함수를 사용합니다.
# 예: 5 ** 2 또는 pow(5, 2)는 25를 반환합니다.
print(math.sqrt(9))
print(math.sqrt(16))