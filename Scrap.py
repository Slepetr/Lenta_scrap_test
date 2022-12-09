import requests
from bs4 import BeautifulSoup
import time
import json

floats = []
link_ = "lenta.ru"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
}

with open('links.txt') as file:
    lines = [line.strip() for line in file.readlines()]
    data_flats = []
    count = 0

    for line in lines:
        # print(line)
        q = requests.get(line, headers=headers)
        result = q.text

        soup = BeautifulSoup(result, 'lxml')

        print(q.status_code)

        title = soup.find('span', class_='topic-body__title').text.strip()
        author = soup.find('a', class_='topic-authors__author').text.strip()
        date_publish = soup.find('a', class_="topic-header__time").text.strip()
        category = soup.find('a', class_='_active').text
        text_in = soup.find('div', class_='topic-body__title-yandex').text

        time.sleep(3)
        # print(title)
        # print(author)
        # print(date_publish)
        # print(category)
        # print(text_in)

        data = {
            'Заголовок': title,
            'Категория': category,
            'Автор': author,
            'Дата и время': date_publish,
            'Текст': text_in,
            #   'Ссылка': line
        }

        count += 1
        print(f'#{count}: {line} is done!')

        data_flats.append(data)

        with open('data.json', 'w', encoding="utf-8") as json_file:
            json.dump(data_flats, json_file, indent=4, ensure_ascii=False)
