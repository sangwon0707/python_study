import math # math 모듈을 사용하기 위해 import

# math.cos() 함수는 라디안 값을 인자로 받아 코사인 값을 반환합니다.
p = 3.14159265 # 원주율(pi)의 근사값
a = math.cos(2 * p) # cos(2 * pi)는 1

print(a)

b = math.cos(0) # cos(0)은 1

print(b)

c = math.cos(math.pi) # math.pi는 정확한 원주율 값, cos(pi)는 -1

print(c)