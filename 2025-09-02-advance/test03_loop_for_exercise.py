#사용자로부터 n개의 정수를 입력받아
#0부터 n까지의 제곱근을 각각 계산하고 출력

import math

n = int(input("입력할 정수의 갯수: "))
list=[]

# for i in range(n + 1):
#     a = int(input("숫자를 입력하시오."))
#     print(math.sqrt(a))
    
for i in range(n + 1):    
    a = int(input("숫자를 입력하시오."))
    list.append(a)

print(list)

for element in list:
    print(math.sqrt(element))