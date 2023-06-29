import random

colors = {"Белый": "Цвет, содержащий все остальные цвета", "Чёрный": "Один из цветов фигур в шахматах",
          "Синий": "Цвет неба", "Красный": "Цвет флага советского союза", "Жёлтый": "Самый заметный цвет"}

print(f"Возможные цвета: {', '.join(colors.keys())}")
rand_color = random.choice(list(colors.keys()))
print("Робот сделал выбор")
ans = input("Выберите цвет: ")
while ans != rand_color:
    print("К сожалению, вы не угадали")
    print("Подсказка:", colors[rand_color])
    ans = input("Выберите цвет: ")
print("Отлично!")
