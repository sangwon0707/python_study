#문자열 추출
a = "Hello World"

print(a[7:9])
print(a[4:10:2])
print(a[7])
print(a[:3])

#개별 인덱스 접근
s = input("네 개 문자를 가진 단어를 입력")
s_rev = s[3] + s[2] + s[1] + s[0]
print(s_rev)

#개별 변수에 할당
s = input("네 개 문자를 가진 단어를 입력")
a, b, c, d = s
s_rev = s[3] + s[2] + s[1] + s[0]
print(s_rev)

#음수 인덱싱으로 추출
s = input("네 개 문자를 가진 단어를 입력")
s_rev = s[::-1]
print(s_rev)

