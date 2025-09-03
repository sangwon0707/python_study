#5회동안 매번 두개의 정수를 입력받아
count_a = 0
count_b = 0

for i in range(5):
    print("[",i+1,"번째 비교]")
    a = int(input("첫번째 숫자: "))
    b = int(input("두번째 숫자: "))
    if a > b:
        count_a = count_a + 1
    else:
        count_b = count_b + 1
    print("첫번째VS두번째:",count_a,":",count_b) 
    
if(count_a > count_b):
    print("- 첫벗째 숫자들이 더 큽니다. - ")
else:
    print("- 두번째 숫자들이 더 큽니다. -")
print("[최종결과",count_a,":",count_b,"]") 