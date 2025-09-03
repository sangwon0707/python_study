'''
행성의 이름을 입력받아 가장뜨거운
행성의 이름을 출력한다. 
입력의 종료는 행성의 이름에 STOP 을 입력
'''
import re
IS_NUMERIC = "^[-+]?\d+(\.\d+)?$" # Regex로 숫자 형식인지 확인

# 최고 온도를 기록할 변수, 매우 낮은 값으로 초기화
max_temp = -274
# 가장 뜨거운 행성의 이름을 저장할 변수
max_name = ""

while True: # 무한 루프 시작
    name = input("행성의 이름을 입력하세요 (종료는 STOP): ")
    
    # 'STOP'을 입력하면 루프 종료
    if name.upper() == "STOP":
        break

    temp_str = input(f"{name}의 온도를 입력하세요: ")

    # 입력된 온도가 숫자 형식이 될 때까지 반복해서 다시 입력받기
    while not re.match(IS_NUMERIC, temp_str):
        print("잘못된 입력입니다. 숫자로 다시 입력해주세요.")
        temp_str = input(f"{name}의 온도를 다시 입력하세요: ")

    # 문자열 온도를 숫자(실수)로 변환
    temp = float(temp_str)

    # 현재 온도가 이전에 기록된 최고 온도보다 높은지 확인
    if temp > max_temp:
        max_temp = temp  # 최고 온도 업데이트
        max_name = name  # 최고 온도 행성 이름 업데이트

# 루프가 끝난 후 결과 출력
if max_name != "":
    print(f"가장 온도가 높은 행성은 {max_name}이고, 온도는 {max_temp}도 입니다.")
else:
    print("입력된 행성 정보가 없습니다.")
