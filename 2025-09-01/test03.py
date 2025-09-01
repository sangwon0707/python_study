#키보드에서 정보를 입력

# input() 함수는 사용자로부터 키보드 입력을 받아 변수에 저장하는 역할을 합니다.
# 괄호 안의 문자열은 사용자에게 보여줄 안내 메시지(프롬프트)입니다.
name = input("your name ?")
major = input("your major ?")
st_number = input("your student number ?")

print("Hi", name)
print("your major is", major)
print("your student number is", st_number)

#입력받은 결과를 출력

#
# [참고] Python의 input() vs Java의 Scanner
#
# Q: Python의 input()은 Java의 Scanner와 같은 건가요?
# A: 네, 사용자로부터 키보드 입력을 받는다는 점에서 같은 목적을 가진 기능입니다.
#
# 주요 차이점:
# 1. 반환 타입: input()은 항상 문자열(String)로 반환하지만, Scanner는 nextInt(), nextDouble() 등 원하는 타입으로 받을 수 있습니다.
# 2. 사용법: input()은 바로 사용 가능하지만, Scanner는 객체를 생성한 후 사용해야 합니다.
# 3. 단순성: input()이 더 간단하고 직관적이며, Scanner는 더 다양한 기능을 제공합니다.
#
# 결론: 하는 일은 같지만, Python의 input()이 더 단순하고 Java의 Scanner가 더 유연합니다.
