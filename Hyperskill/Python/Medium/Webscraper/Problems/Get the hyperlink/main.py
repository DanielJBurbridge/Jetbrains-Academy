import requests

from bs4 import BeautifulSoup

num = input()
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

anchors = soup.find_all('a')

for i in anchors:
    if num in str(i.get("href")):
        print(i.get("href"))
