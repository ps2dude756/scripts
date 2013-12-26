#!/usr/bin/python2

import argparse
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
    'December',
]

def main(start_year, end_year, output_file, log_file):
    f = open(output_file, 'w')
    
    for year in range(start_year, end_year + 1):
        titles = {}
        for month in MONTHS:
            for comic in gen_comics(year, month, log_file):
                try:
                    title = titles[comic.title]
                    title['max'] = max(title['max'], comic.issue)
                    title['min'] = min(title['min'], comic.issue)
                except KeyError:
                    titles[comic.title] = {
                        'max': comic.issue,
                        'min': comic.issue,
                    }
        for title, info in sorted(titles.items()):
            f.write(
                title + ' #' + str(info['min']) + '-' + str(info['max']) + '\n'
            )

def create_args():
    parser = argparse.ArgumentParser(
        description='Find all Marvel comics produced between the given years'
    )
    parser.add_argument(
        '--start_year',
        action='store',
        nargs=1,
        default=[2000],
        type=int,
        help='the year to start scanning from',
    )
    parser.add_argument(
        '--end_year',
        action='store',
        nargs=1,
        default=[2013],
        type=int,
        help='the year to stop scanning at',
    )
    parser.add_argument(
        '--output_file',
        action='store',
        nargs=1,
        default=['./marvel_comics.txt'],
        type=str,
        help='file to store results in',
    )
    parser.add_argument(
        '--log_file',
        action='store',
        nargs=1,
        default=['./marvel_comics.log'],
        type=str,
        help='file to store log messages in',
    )
    return parser.parse_args()

if __name__ == '__main__':
    args = create_args()
    main(
        args.start_year[0],
        args.end_year[0],
        args.output_file[0],
        args.log_file[0]
    )
