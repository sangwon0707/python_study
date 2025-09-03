#1~10000값들의 평균값을 계산한다.

s = 0

for i in range(1,10001):
    s = s + i
    
average = s / 10000
print(average)

#루프 정리하기
n = int(input("N값을 입력: "))

s = 0
for i in range (i, n+1):
    denom = 0
    for j in range(1, n+1):
        denom += j ** j
        
    s += i / denom
    
print(s)