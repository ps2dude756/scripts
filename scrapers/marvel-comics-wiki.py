from bs4 import BeautifulSoup
import urllib2

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

domain = "http://marvel.wikia.com"
year_start = 2000
year_end = 2013

def main():
    titles_by_year = {}
    for issue in gen_issues():
        try:
            titles = titles_by_year[issue['year']]
            try:
                title = titles[issue['title']]
                title['min_issue'] = min(title['min_issue'], issue['number'])
                title['max_issue'] = max(title['max_issue'], issue['number'])
            except KeyError:
                titles[issue['title']] = {
                    'min_issue': issue['number'],
                    'max_issue': issue['number'],
                    }
        except KeyError:
            titles_by_year[issue['year']] = {
                issue['title']: {
                    'min_issue': issue['number'],
                    'max_issue': issue['number'],
                    }
                }
    for year in titles_by_year:
        print('----' + str(year) + '----')
        titles = titles_by_year[year]
        for name in sorted(titles.keys()):
            print(
                name + ' #' + titles[name]['min_issue'] + '-' + titles[name]['max_issue']
                )
        print('')

def gen_issues():
    for year in range(year_start, year_end + 1):
            for month in MONTHS:
                url = domain + "/Category:" + str(year) + ",_" + month
                page = urllib2.urlopen(url)
                soup = BeautifulSoup(page)
                divs = soup.findAll('div', {'class': 'lightbox-caption'})
                for div in divs:
                    text = div.findNext('a').text.encode('utf-8')
                    title = text[:text.rfind(' ') - 1]
                    number = text[text.rfind('#') + 1:]
                    issue = {
                        'title': title,
                        'number': number,
                        'year': year,
                        }
                    yield issue

if __name__ == "__main__":
    main()
