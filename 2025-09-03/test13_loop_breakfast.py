# 아침식사 비율조사
# 직업 학생(s) 직장인(b) 무직(n)
# 설문조사 인원 (n)
# 식사를 한다(Y), 식사를 안한다(N)
# 학생이 아침식사를 하는 비율을 계산하여 결과를 출력한다.


count_s = 0
count_no = 0
count_yes = 0

print("직업을 입력하시오.")

for i in range(1000):
    job = input("학생(S), 직작인(B), 무직(N):")
    if job.upper()=="S" or job == "학생":
        count_s = count_s +1
    else:
        break
    meal = input("식사 여부를 입력하세요.(Y/N)")
    if meal.upper() == "Y":
        count_yes = count_yes + 1
    elif meal.upper() =="N":
        count_no = count_no + 1
    else:
        meal = input("올바른 입력을 해주세요. (Y/N)")        