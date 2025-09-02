for i in range(1,3):
    for j in range(1,4):
        print(i, j)
        

print("-"*70)

a = 1
for i in range (1,5,2):
    for j in range (7):
        a = a*j + i
        i += 1
        print(a)