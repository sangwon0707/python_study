#환율 변환기

def display_menu():
    print("[환율 변환기]")
    print("1. 달러를 유로로 변환하기!")
    print("2. 유로를 달러로 변환하기!")
    print("3. 종료")
    print("-"*70)
    print("원하시는 메뉴를 선택하세요.", end ="") 
    
rate = 0.72

while True:
    display_menu()
    choice = int(input())
    if choice == 1:
        amount = float(input("금액을 숫자로 입력하시오.: "))
        print(amount,"달러는", amount * rate, "유로입니다.")
    elif choice == 2:
        amount = float(input("금액을 숫자로 입력하시오.: "))
        print(amount,"유로는", amount * (1/rate), "달러입니다.")
    elif choice == 3:
        print("종료합니다.")
        break
    else:
        print(">>>잘못된 선택입니다. 메뉴에 있는 1, 2, 3 중에서 선택해주세요.")
