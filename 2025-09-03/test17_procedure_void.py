#PROCEDURE 프로시져

def display_line():
    print("-----------")
    
print("안녕하세요!")
display_line()
    
print("어떻게 지내세요!")
display_line()

print("당신의 이름이 무엇입니까?!")
display_line()

#프로시져의 인자값은 여러개를 사용할 수 있다.
def add_and_display (n1, n2, n3, n4):
    result = n1 + n2 + n3 + n4
    print(result)
    
#메인 코드
a = float(input())
b = float(input())
c = float(input())
d = float(input())

add_and_display(a,b,c,d)