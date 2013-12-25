#!/usr/bin/python2

from scrapers.marvel_wikia import gen_comics
from lib.comic import Comic

MONTHS = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]

def main():
    for month in MONTHS:
        for comic in gen_comics(2002, month):
            print(comic.title + ' #' + str(comic.issue))

if __name__ == '__main__':
    main()
