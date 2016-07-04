import argparse
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = None

class Comic:
    def __init__(self, title, issue, subtitle, publish_date):
        self._title = title
        self._issue = issue
        self._subtitle = subtitle
        self._publish_date = publish_date

    def get_title(self):
        return self._title

    def get_issue(self):
        return self._issue

    def get_subtitle(self):
        return self._subtitle

    def get_publish_date(self):
        return self._publish_date

    def __str__(self):
        try:
            issue = '#{0}'.format(int(self._issue))
        except ValueError:
            issue = self._issue

        if self._subtitle:
            return '{0} {1}: {2} ({3})'.format(self._title, issue, self._subtitle, self._publish_date) 
        else:
            return '{0} {1} ({2})'.format(self._title, issue, self._publish_date)

def main(user_name, password, filename):
    comics = parse_comics(filename)

    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    login(user_name, password)

    for i, comic in enumerate(comics):
        add_comic(i, comic)
        driver.find_element_by_link_text('Add Another Item').click()

def parse_comics(filename):
    comics = []

    with open(filename, 'r') as f:
        lines = f.read().split('\n')

    for i, line in enumerate(lines):
        comic = line.split('\t')
        try:
            comics.append(Comic(comic[0], comic[2], comic[3], comic[6]))
        except IndexError:
            pass

    return comics

def login(user_name, password):
    driver.get('https://missingmail.usps.com/')
    driver.find_element_by_id('userName').send_keys(user_name)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('sign-in-button').click()

def add_comic(index, comic):
    itemCategory = driver.find_element_by_id('itemCategory{0}'.format(index))
    Select(itemCategory).select_by_visible_text('Books, Media and Entertainment')


    itemSubcategory = driver.find_element_by_id('itemSubcategory{0}'.format(index))
    Select(itemSubcategory).select_by_visible_text('Books')

    itemItemType = itemSubcategory.find_element_by_xpath('../../..').find_element_by_id('itemItemType')
    Select(itemItemType).select_by_visible_text('Comic Book/Graphic Novel')

    driver.find_element_by_id('itemDescription{0}'.format(index)).send_keys(str(comic))
    driver.find_element_by_id('itemQuantity{0}'.format(index)).send_keys('1')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('user_name', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('filename', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    main(args.user_name, args.password, args.filename)
