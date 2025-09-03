#무한 루프 회피하기
i = 0 
while i != 10:
    print("안녕하세요~")
# "i" is always 0, so the loop won't stop.

i = 1
while i != 10:
    print("안녕하세요~")
    i += 2
#1 3 5 7 9 11 12
# "i" will never be 10 in the loop.
    
i = 1
while i < 10:
    print("안녕하세요~")
    i += 2
    
#1 3 5 7 9 