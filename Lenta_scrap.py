import requests
from bs4 import BeautifulSoup
import time

floats = []
link_ = "lenta.ru"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
}

for page in range(1, 3):
    url = f'https://lenta.ru/parts/news/{page}/'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    print(response.status_code)
    news_links = soup.find_all('a', class_='card-full-news')

    for link in news_links:
        page_link = link.get('href')
        if link_.lower() in page_link.lower():
            continue
        else:
            new_page_link = "https://lenta.ru" + page_link
            floats.append(new_page_link)

    print(floats)
    time.sleep(3)

with open('links.txt', 'a') as file:
    for line in floats:
        file.write(f'{line}\n')