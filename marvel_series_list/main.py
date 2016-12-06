import json
import requests
import time
from bs4 import BeautifulSoup

r = requests.get('http://marvel.com/comics/series')
soup = BeautifulSoup(r.text, 'html.parser')

comics_tables = soup.find_all(lambda tag: tag.has_attr('data-filter-az-staticresults'))
comics_lis = comics_tables[0].find_all(lambda tag: tag.name == 'li')
comics_strings = [comic_li.find_all(lambda tag: tag.name == 'a')[0].text for comic_li in comics_lis]

comics = []
for comic in comics_strings:
    title = ' ('.join(comic.split(' (')[:-1])

    date_range = comic.split(' (')[-1][:-1]

    try:
        start_year = date_range.split(' - ')[0]
        end_year = date_range.split(' - ')[1]
    except IndexError:
        start_year = date_range
        end_year = date_range

    comics.append({
        'title': title,
        'start_year': start_year,
        'end_year': end_year
    })

with open('output.txt', 'w') as f:
    f.write(json.dumps({
        'date': time.time(),
        'comics': comics
    }))
