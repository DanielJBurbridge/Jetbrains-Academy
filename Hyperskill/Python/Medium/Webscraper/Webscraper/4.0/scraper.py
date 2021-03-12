import requests
import string
from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles'



r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

article_div = soup.find('div', attrs={'data-container-type':'article-list'})
articles = article_div.find_all('article')
anchors = []
for article in articles:
    span = article.find('span')
    if span.text == 'News':
        # print("this one has news")
        anchor = article.find('a')
        anchors.append(anchor)

news_articles = []
for anchor in anchors:
    news_articles.append({'title': anchor.text.strip().translate(str.maketrans(' ', '_', string.punctuation + "'")), 'link': f"https://nature.com{anchor.get('href').strip()}"})

for index, article in enumerate(news_articles):
    # print(f"Scraping article, {index + 1}")
    # file = open(article['title'] + '.txt', 'w', encoding='utf-8')
    file = open(article['title'] + '.txt', 'wb')
    r = requests.get(article['link'])
    soup = BeautifulSoup(r.content, "html.parser")
    body = soup.find('body')
    content = soup.find("div", id="content")
    article_body = soup.find("div", class_="article__body")
    paragraphs = article_body.find_all('p')

    my_string = ''
    for paragraph in paragraphs:
        my_string += (paragraph.text.strip()+'\n')

    text = article_body.text.strip()
    file.write(text.encode('utf-8'))
    file.close()

print("Successfully Scraped")
