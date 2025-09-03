i = 1
s = 0
a = 0

a = int(input("a를 입력하시오.: "))
i += 1

while i < 90:
    s = s  + a * i
    a = int(input())
    # a = a +1
    # print(a)
    i += 1

print(s)