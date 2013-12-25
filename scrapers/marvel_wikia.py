from bs4 import BeautifulSoup
import urllib2
from lib.comic import Comic

domain = 'http://marvel.wikia.com'

def gen_comics(year, month):
    url = domain + '/Category:' + str(year) + ',_' + month
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    divs = soup.findAll('div', {'class': 'lightbox-caption'})
    for div in divs:
        text = div.findNext('a').text.encode('utf-8')
        title = text[:text.rfind(' ') - 1]
        try:
            issue = float(text[text.rfind('#') + 1:])
        except ValueError:
            print('Error for issue ' + title + ' #' + text[text.rfind('#') + 1:])
        yield Comic(title, issue, month, year) 
