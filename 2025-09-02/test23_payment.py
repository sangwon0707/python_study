'''
주 40시간 이상 근무한 시간은 기본 시급의 1.5배를 지급
시급, 시간을 입력받아 주급을 출력하는 프로그램을 작성
'''

pay = int(input("시급: "))
hours = int(input("일한 시간:"))

if hours <= 40:
    total_pay = pay * hours
else:
    base = pay * 40
    print("기본임금: ", base)
    extra = pay * (hours - 40) * 1.5
    print("초과수당: ", extra)
    total_pay = base + extra
    
print("주급", total_pay)