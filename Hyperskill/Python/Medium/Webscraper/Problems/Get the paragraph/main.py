import requests

from bs4 import BeautifulSoup

word = input()
url = input()

# word = 'Solomon'
# url = 'https://stepik.org/media/attachments/lesson/372811/3._The_Gift_of_the_Magi.shtml'

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

paragraphs = soup.find_all('p')

for p in paragraphs:
    if word in p.text:
        print(p.text)
        break
