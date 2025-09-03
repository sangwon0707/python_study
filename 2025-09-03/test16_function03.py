'''
함수의 수행 흐름
- 함수의 호출이 되면 메인 코드의 실행은 중단된다. 
- 인자 값이 함수쪽에 전달된 후 함수의 내용이 실행된다.
- 함수의 실행이 끝난 후 결과 값을 메인 코드로 리턴한다.
- 결과 값을 리턴 받은 메인 코드는 다음 단계를 실행한다.
'''

def total(a,b):
    s = a + b
    return s

#main code
n1 = float(input())
n2 = float(input())

result = total(n1, n2)

print(n1,"+",n2,"+", result)