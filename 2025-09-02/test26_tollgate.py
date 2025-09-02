v = input().upper()
#버스도 3000원 , 버스는 B

if v == "M":
    print("1000원을 지불하세요.")
elif v == "C":
    print("2000원을 지불하세요.")
elif v == "T" or v == "B":
    print("3000원을 지불하세요.")
else:
    print("차량 정보가 올바르지 않습니다.")


#y 값 찾기.

x = float(input())

y = (5 + x)/x + (x + 9)/(x - 4)
# y = int(y)

print("y의 값은?", y)