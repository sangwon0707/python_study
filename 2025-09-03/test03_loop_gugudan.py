#구구단
i = 1
for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
    print("-"*20)
    
#10000부터 1가지 100식 줄어들면서 1~9로 나누기
i = 1
for i in range(10000,1,-100):
    for j in range(1,10):
        print(i,"/",j,"=",i/j)
        

