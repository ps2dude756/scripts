from bs4 import BeautifulSoup
import logging
import urllib2
from lib.comic import Comic

DOMAIN = 'http://marvel.wikia.com'

def gen_comics(year, month, log_file):
    logging.basicConfig(filename=log_file)
    logger = logging.getLogger(__name__)

    url = DOMAIN + '/Category:' + str(year) + ',_' + month
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    divs = soup.findAll('div', {'class': 'lightbox-caption'})
    for div in divs:
        text = div.findNext('a').text.encode('utf-8')
        title = text[:text.rfind(' ') - 1]
        try:
            issue = int(text[text.rfind('#') + 1:])
            yield Comic(title, issue, month, year) 
        except ValueError:
            logger.warning('Error for issue ' + text)
