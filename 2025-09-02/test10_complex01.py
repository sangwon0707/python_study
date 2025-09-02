'''
입력값 700005초 
=> 8일 2시간 26분 45초

초단위 시간을 입력받는ㄴ다
일수를 산출한다.
시간을 산출한다.
분을 산출한다.
초를 산출한다.
'''
number = int(input("경과시간 초를 입력"))
# number = 700005
d = 24 * 60 * 60
h = 60 * 60
m = 60
w = 7 * d

weeks, r = divmod(number, w)
days, r = divmod(r, d)
hours, r = divmod(r, h)
minutes, seconds = divmod(r, 60)

print(weeks,"주",days, "일", hours, "시간", minutes, "분", seconds, "초")
