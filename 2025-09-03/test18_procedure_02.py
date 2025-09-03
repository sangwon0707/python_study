#프로시저는 리턴값을 반환하지 않기때문에 변수에 넣어서 쓸수 없다.
def test(a):
    print('프로시저 내부처리', a)
    # return a
    
y = test(5)
print(y)
print(test(7))