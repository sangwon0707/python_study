#함수와 프로시져를 이용한 환율 변환기
# 다음 메뉴 출력
# 1. KRW를 USD
# 2. KRW를 EUR
# 3. KRW를 JPY
# 4. KRW를 CNY

def display_menu():
    print("[  환율 변환기  ]")
    print("원하시는 서비스 번호를 선택하세요!")
    print("1. KRW를 USD 로 변환")
    print("2. KRW를 EUR 로 변환")
    print("3. KRW를 JPY 로 변환")
    print("4. KRW를 CNY 로 변환")

def calculator(choice, krw):
    if choice == 1:
        cal = krw * 1.4
    elif choice == 2:
        cal = krw * 1.6
    elif choice == 3:
        cal = krw * 0.9
    elif choice == 4:
        cal = krw * 0.1        
    else:
        print("잘못된 입력입니다.")
        cal = krw
    return cal
    
display_menu()
choice = float(input("선택: "))
krw = float(input("금액입력: "))
cal = calculator(choice, krw)
print("환율은", cal,"입니다")