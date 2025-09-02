#부가세 + 팁(20%)
VAT = 0.10
TIP = 0.20
price_before = float(input("상품가격: "))
vat = price_before * VAT
tip = price_before * TIP

price_final = price_before + vat + tip

print("부가세:", vat)
print("팁:", tip)
print("판매가격:", price_final)


#화씨를 섭씨로 변환
fah = float(input("화씨 온도는?")) 
cel = (fah - 32 )/1.8
print("섭씨 온도는?", cel)