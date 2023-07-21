import requests
from bs4 import BeautifulSoup as bs

url = input(
    "Введите ссылку на вашего любимого исполнителя на сайте яндекс музыки: ")
if not url.endswith("/tracks"):
    url += "/tracks"
try:
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    songs = soup.find_all("a",
                          class_="d-track__title deco-link "
                                 "deco-link_stronger")
    for i in range(10):
        print(i + 1, songs[i].text)
except Exception:
    print("Упс, что-то пошло не так")
