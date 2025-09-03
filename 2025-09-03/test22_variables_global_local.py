# global 키워드를 사용하여 전역 변수를 함수내에 지정해준다.
def display_value():
    global test #글로벌 전역변수 설정! 
    print(test) 
    #첫 print(test)에서는 내부에서 test변수가 선언되지 않아 사용할수 없다. 
    #사용하려면 Global test 전역 변수수 설정이 필요하다. 
    test = 20
    print(test)
    
test = 10
display_value()
print(test)