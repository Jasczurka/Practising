import pandas as pd

df = pd.read_csv("books.csv", delimiter=",")
n = int(input("Сколько записей вы хотите добавить в список: "))
for i in range(n):
    if i == 0:
        print("Введите данные в следующем формате\nКнига,Автор,Год выпуска")
    df.loc[len(df.index)] = input().split(",")
name = input("Введите автора: ")
try:
    res = df.loc[df["Автор"] == name]
    if res.empty:
        raise Exception
    print(res)
except Exception:
    print("В списке нет книг этого автора")
