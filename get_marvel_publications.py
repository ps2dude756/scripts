#!/usr/bin/python2

import argparse
import os
from scrapers.marvel_wikia import gen_comics
from lib.comic import Comic

DEFAULT_START_YEAR = 2000
DEFAULT_END_YEAR = 2013
DEFAULT_OUTPUT_FILE = './output/marvel_comics.txt'
DEFAULT_LOG_FILE = './output/marvel_comics.log'

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
    try:
        os.remove(output_file)
    except OSError:
        pass
    try:
        os.remove(log_file)
    except OSError:
        pass

    f = open(output_file, 'w')
    
    for year in range(start_year, end_year + 1):
        f.write('----{0}----\n'.format(str(year)))
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
                '{0} #{1}-{2}\n'.format(
                    title, 
                    str(info['min']), 
                    str(info['max'])
                )
            )

def create_args():
    parser = argparse.ArgumentParser(
        description='Find all Marvel comics produced between the given years'
    )
    parser.add_argument(
        '--start_year',
        action='store',
        nargs=1,
        default=[DEFAULT_START_YEAR],
        type=int,
        help='the year to start scanning from',
    )
    parser.add_argument(
        '--end_year',
        action='store',
        nargs=1,
        default=[DEFAULT_END_YEAR],
        type=int,
        help='the year to stop scanning at',
    )
    parser.add_argument(
        '--output_file',
        action='store',
        nargs=1,
        default=[DEFAULT_OUTPUT_FILE],
        type=str,
        help='file to store results in',
    )
    parser.add_argument(
        '--log_file',
        action='store',
        nargs=1,
        default=[DEFAULT_LOG_FILE],
        type=str,
        help='file to store log messages in about issues that could not be ' \
            'parsed properly',
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
