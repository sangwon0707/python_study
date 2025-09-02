'''
range()
range(b): 0~b 사이의 값의 배열을 반환한다.
range(a,b) a~b 사이의 값의 배열을 밴환한다. b는 미포함
RANGE(a,b,c) a ~ b 사이의 c간격의 값의 배열을 반환한다.
range의 인자 중 a와 c는 선택옵션으로 생략이 가능한 인자이다.
'''

a = range(1,6)
b = range(6)
c = range(0, 50, 10)
d = range(100, 80, -5)

print(list(a))
print(list(b))
print(list(c))
print(list(d))
