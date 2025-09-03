#1 + 2 + 3 +...100 
# while
print("while 문으로 1부터 100까지 더하기")
i = 1
s = 0
while i <= 100:
    s = s + i
    i = i + 1
    
print(s)

print("-"*70)
# for
print("for문으로 1부터 100까지 더하기")
s = 0
for i in range(1,101):
    s = s + i

print(s)