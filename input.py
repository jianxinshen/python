# Guass the Number
num = 6
n = 0
print("Guass the number ?")
while n < 1:
    answer = int(input())  # 加入int()强行转为数值，避免之后出错
    if answer > num:
        print("It's too high!")
        n = 0
    elif answer < num:
        print("It's too low!")
        n = 0
    else:
        print("Bingo!!!")
        n = 1
