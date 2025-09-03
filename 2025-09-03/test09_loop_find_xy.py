# -20 에서 20범위 내에서
# 다음 방정식을 만족하는 X 와 Y 의 정수값을 찾아 출력한다.
# X^2 - 6Y^2 = 6

for x in range(-20, 20):
    for y in range(-20, 20):
        if 3*x**2-6*y**2==6:
            print(x,y)