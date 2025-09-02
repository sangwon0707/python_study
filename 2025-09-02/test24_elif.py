#elif (else if) 다중택일구조
name = input("이름이 무엇인가요?")

if name =="홍길동":
    print("나의 삼촌이군요!")
elif name =="김영희":
    print("나의 누나군요!")
elif name =="김숙자":
    print("나의 어머니시군요!")
else:
    print("너는 누구냐?")
    
#다중 택일 결정 구조와 추적표 (요일 출력하기))
day = int(input("1-7사이의 숫자: "))

if day == 1:
    print("월요일")
elif day == 2:
    print("화요일")
elif day == 3:
    print("수요일")
elif day == 4:
    print("목요일")
elif day == 5:
    print("금요일")
elif day == 6:
    print("토요일")
else :
    print("일요일")
