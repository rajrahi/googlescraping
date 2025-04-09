import json
import time
from scrap import Google_scraper
from api import get_keywords , post_feed


limit = 1
skip = 0
while True:

    keywords = get_keywords(limit ,skip)
    print(keywords)
    skip += limit
    if "Error" in keywords:
        break

    g =  Google_scraper("https://www.google.com/" , detach=False)
    g.type_text(keywords)
    time.sleep(2)
    try:
        # post_feed(g.get_data_from_soups()[0])
        print(g.get_data_from_soups()[0])

    except Exception as e:
        print(e)