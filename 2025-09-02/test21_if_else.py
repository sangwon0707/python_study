import math
x = int(input())

print("-"*70)
print("테스트1")
if x < 0:
    print("입력한 숫자는 음수 입니다.")
    x = math.sqrt(x**2)
    x = int(x)
else:
    print("입력한 숫자는 양수 입니다.")

print(x)

print("-"*70)
print("테스트2")

b = int(input())
if b > 0:
    print("양수")
elif b < 0:
    print("음수")
else:
    print("0입니다.")
    
