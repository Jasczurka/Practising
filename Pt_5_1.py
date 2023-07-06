import pandas as pd

df = pd.DataFrame({"Книга": ["Мастер и Маргарита", "Робинзон Крузо", "451 градус по Фаренгейту", "Дом, в котором…",
                             "Убить пересмешника"],
                   "Автор": ["М. А. Булгаков", "Даниэль Дефо", "Рэй Брэдбери", "Мариам Петросян", "Харпер Ли"],
                   "Год выпуска": [1967, 1719, 1953, 2009, 1960]})
df.to_csv("books.csv", index=False)
