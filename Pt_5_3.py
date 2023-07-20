import pandas as pd

df = pd.read_csv("books.csv", delimiter=",")
begin, end = map(int, input(
    "Введите начальный и конечный год через пробел: ").split())
try:
    res = df.loc[(df["Год выпуска"] >= begin) & (df["Год выпуска"] <= end)]
    if res.empty:
        raise Exception
    print(res)
except Exception:
    print("В списке нет книг, выпущенных в заданный период")
