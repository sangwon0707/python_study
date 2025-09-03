def get_fullname():
    first_name = input("영문 이름 입력: ")
    last_name = input("영문 성 입력: ")
    return first_name, last_name

fname, lname = get_fullname()
print("영문이름:", fname)
print("영문성:", lname)