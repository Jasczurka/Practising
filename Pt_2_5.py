import random

loses = 0
res = 0
while (res == 0 or res == 1) and loses != 3:
    res = int(input("Орёл или решка? "))
    bot_res = random.randint(0, 1)
    if res == bot_res:
        print("Вы выиграли")
        loses = 0
    else:
        loses += 1
        print("Вы проиграли")
