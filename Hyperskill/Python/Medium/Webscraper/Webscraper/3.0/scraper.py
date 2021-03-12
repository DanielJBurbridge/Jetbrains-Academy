import requests
from bs4 import BeautifulSoup

url = input("Input the URL:\n")

r_status = requests.get(url).status_code
r_content = requests.get(url).content

file = open('source.html', 'wb')

if r_status == 200:
    file.write(r_content)
    print("Content saved.")
else:
    print(f"The URL returned {r_status}")

file.close()
