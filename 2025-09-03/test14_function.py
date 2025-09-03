# def display(color):
#     msg = "무지개에 " + color + "이 있다."
#     # print(msg)
#     return msg
    

# colors = ["빨간색","주황색","노란색","초록색","파란색","남색","보라색"]

# for element in colors:
#     msg = display(element)
#     print(msg)
    
def display(color, exists):
    # print(msg)
    neg = "이 있다."
    if exists == False:
        neg = "이 없다."
    msg = "무지개에 " + color + neg
    return msg

print    