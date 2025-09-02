"""
파이썬 불리언(Boolean) 식을 위한 비교 연산자

파이썬에서는 두 값을 비교하기 위해 비교 연산자를 사용합니다.
이 연산의 결과는 항상 불리언 값인 True 또는 False입니다.
"""

# 비교를 위한 변수 선언
a = 10
b = 5
c = 10

print(f"a = {a}, b = {b}, c = {c}\n")

# 1. == (같다)
# 두 값이 서로 같으면 True, 다르면 False를 반환합니다.
print(f"a == c : {a == c}")  # a와 c는 값이 10으로 같으므로 True
print(f"a == b : {a == b}")  # a(10)와 b(5)는 다르므로 False
print("-" * 20)

# 2. != (다르다)
# 두 값이 서로 다르면 True, 같으면 False를 반환합니다.
print(f"a != b : {a != b}")  # a(10)와 b(5)는 다르므로 True
print(f"a != c : {a != c}")  # a와 c는 값이 10으로 같으므로 False
print("-" * 20)

# 3. > (크다)
# 왼쪽 값이 오른쪽 값보다 크면 True, 아니면 False를 반환합니다.
print(f"a > b : {a > b}")   # a(10)가 b(5)보다 크므로 True
print(f"b > a : {b > a}")   # b(5)가 a(10)보다 크지 않으므로 False
print("-" * 20)

# 4. < (작다)
# 왼쪽 값이 오른쪽 값보다 작으면 True, 아니면 False를 반환합니다.
print(f"b < a : {b < a}")   # b(5)가 a(10)보다 작으므로 True
print(f"a < b : {a < b}")   # a(10)가 b(5)보다 작지 않으므로 False
print("-" * 20)

# 5. >= (크거나 같다)
# 왼쪽 값이 오른쪽 값보다 크거나 같으면 True, 아니면 False를 반환합니다.
print(f"a >= c : {a >= c}")  # a(10)가 c(10)와 같으므로 True
print(f"a >= b : {a >= b}")  # a(10)가 b(5)보다 크므로 True
print(f"b >= a : {b >= a}")  # b(5)가 a(10)보다 크거나 같지 않으므로 False
print("-" * 20)

# 6. <= (작거나 같다)
# 왼쪽 값이 오른쪽 값보다 작거나 같으면 True, 아니면 False를 반환합니다.
print(f"b <= a : {b <= a}")  # b(5)가 a(10)보다 작으므로 True
print(f"a <= c : {a <= c}")  # a(10)가 c(10)와 같으므로 True
print(f"a <= b : {a <= b}")  # a(10)가 b(5)보다 작거나 같지 않으므로 False
print("-" * 20)

# === 논리 연산자 (Logical Operators) ===
# 비교 연산의 결과를 조합하여 더 복잡한 조건을 만들 때 사용합니다.
# if, while과 같은 결정 제어 구조에서 매우 중요하게 사용됩니다.

print("\n=== 논리 연산자 (Logical Operators) ===\n")

# 1. and
# 두 조건이 모두 True일 때만 전체 결과가 True가 됩니다.
# 하나라도 False이면 결과는 False입니다.
print("True and True:", True and True)
print("True and False:", True and False)
print(f"a > b and a == c : {a > b and a == c}") # (10 > 5)는 True, (10 == 10)은 True -> True
print("-" * 20)


# 2. or
# 두 조건 중 하나라도 True이면 전체 결과가 True가 됩니다.
# 두 조건이 모두 False일 때만 결과가 False입니다.
print("True or False:", True or False)
print("False or False:", False or False)
print(f"a > b or a == b : {a > b or a == b}") # (10 > 5)는 True, (10 == 5)는 False -> True
print("-" * 20)


# 3. not
# 불리언 값의 결과를 반대로 뒤집습니다.
# True는 False로, False는 True로 바꿉니다.
print("not True:", not True)
print("not False:", not False)
print(f"not (a > b) : {not (a > b)}") # (10 > 5)는 True이므로, not True -> False
print("-" * 20)


# === if 조건문과 함께 사용하기 ===
# 논리 연산자는 if 문과 함께 사용하여 프로그램의 흐름을 제어합니다.

age = 25
is_student = True

print(f"age = {age}, is_student = {is_student}\n")

# and 예시: 19세 초과이면서 65세 미만일 경우
if age > 19 and age < 65:
    print("성인입니다.")

# and 예시: 30세 미만이면서 학생일 경우
if age < 30 and is_student:
    print("30세 미만의 학생입니다.")

# or 예시: 60세를 넘었거나 학생일 경우
if age > 60 or is_student:
    print("60세 이상이거나 학생입니다.")

