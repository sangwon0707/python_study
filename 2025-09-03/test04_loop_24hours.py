for hour in range(1,25):
    print("현재시간은 ", hour,"시 입니다.")
    if hour >= 4 and hour < 12:
        print("좋은 아침입니다.")
    elif hour >= 12 and hour < 20:
        print("좋은 오후입니다.")
    elif hour >= 20 and hour < 24:
        print("좋은 저녁입니다.")
    else:
        print("편히 주무세요")    
    
# for hours in range(1,25):
#     print("현재시간은 ", hours,"시 입니다.")
    