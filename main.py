from datetime import date, datetime, timedelta
import feedparser
import aws
from configparser import ConfigParser


print('starting...')

config_file = aws.get_config()
config = ConfigParser()
config.read_string(config_file)

for blog in config.sections():
    feed = feedparser.parse(config[blog]['url'])

    entry_count = len(feed['entries'])
    print(entry_count, ' entries found for ', blog)
    yesterday = date.today() - timedelta(days=1)
    print('selecting articles published on ', yesterday)
    for feed in feed['entries']:
        published = feed['published']
        published_datetime = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %z')
        published_date = date(published_datetime.year, published_datetime.month, published_datetime.day)
        if date.today() > published_date >= yesterday:
            href = feed['links'][0]['href']
            print('entry ', href, ' on ', published)
            aws.send_daily('PV Cycling', published_date.strftime('%a, %b %d %Y'), href)

print('done.')
