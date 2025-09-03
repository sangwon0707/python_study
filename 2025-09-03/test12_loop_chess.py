grains = 1
total = 0

for i in range(1,65):
    total = total + grains
    print(i,"번칸에는", grains,"의 밀알이 들어갑니다.")
    grains = grains * 2    
print("밀알의 총합:",total)
