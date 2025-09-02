#아이디 생성기 

import random
name = input("영문이름을 입력: ")
name5 = name[:5]
lower_name = name5.lower()

temp1 = name5[:2].upper();
temp2 = name5[2:5].lower();
print("앞두글짜 대문자:", temp1)
print("뒷글짜 소문자:", temp2)
new_name = temp1 + temp2

random_int = random.randrange(100, 1000)
new_id = lower_name + str(random_int)
print("새로운아이디_소문자: ", new_id)

new_id2 = new_name + str(random_int)
print("새로운아이디_대소문자", new_id2)

