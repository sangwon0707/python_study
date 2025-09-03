'''
10명의 몸무게를 입력받고 1~100사이일때만 가장 많이 나가는 몸무게를 출력한다.
'''

import re

IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$" #Regex 숫자가 아닌거 걸러내기
maximum = -1

for i in range(10):
    inp = input("몸무게 값을 입력:")
    while not re.match(IS_NUMERIC, inp) or float(inp) < 0 or float(inp) > 100:
        inp = input("부적절한 값! 1-100사이의 몸무게값 입력하세요: ")
        
    w = int(inp)
    
    #첫로테이션에서 -1보다 크면 현재 몸무게가 maximum에 저장된다. 
    #두번째 로테이션부터는 W에 저장된 값을 maximum 비교하여 
    #크면 maximum 에 새 w 값을 저장하여 최종적으로 가장 큰 값이 최종적으로 남는다.
    if w > maximum: 
        maximum = w
        
print(maximum)