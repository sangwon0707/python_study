# input() 함수는 항상 문자열(string) 형태로 값을 반환합니다.
x = input("a?")
y = input("b?")

# 아래 주석 처리된 라인처럼 문자열을 바로 곱하면, 우리가 원하는 숫자 계산이 아니라
# 문자열 반복이나 오류가 발생합니다.
# print("a*b=", x*y)

# 따라서 숫자 계산을 위해서는 int() 함수를 사용해
# 문자열을 정수(integer)로 변환해 주어야 합니다. (이 과정을 '형 변환' 또는 'Type Casting'이라고 합니다.)
new_x = int(x)
new_y = int(y)

# 정수로 변환된 두 변수를 곱하여 원하는 결과를 얻습니다.
print("a*b=", new_x*new_y)

x2 = float(input("a?"))
y2 = float(input("b?"))
print("a*b=", x2*y2)
