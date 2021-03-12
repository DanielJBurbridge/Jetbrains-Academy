import requests
from bs4 import BeautifulSoup

# Used 100 Gems to see a solution, modified it to my own
movie = {}
try:
    r = requests.get(input())
    soup = BeautifulSoup(r.content, 'html.parser')

    movie['title'] = soup.find('div', id="star-rating-widget").get("data-title")
    movie['description'] = soup.find('div', class_='summary_text').text.strip()

    print(movie)
except:
    print('Invalid movie page!')
