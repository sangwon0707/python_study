#결정제어구조
a = int(input("숫자 입력: "))
'''
if a > 0:
    y = a*4
    print(y)
else:
    y = a*3
    print(y)
'''
if a > 0:
    y = a*4
else:
    y = a*3
print(y)

#결정제어구조2
a = int(input())
b = int(input())
y = 0

if a > 0:
    y += 1
else:
    print("안녕 철수!")

if y > 0:
    print(y + 5)
    
y += 1

#DEAD CODE
if y <= 0:
    print(y + 12)