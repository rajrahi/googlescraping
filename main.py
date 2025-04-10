import json
import time

import requests
from scrap import Google_scraper
from api import get_keywords , post_feed

from  pydantic_model import AdData

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
        print(post_feed(g.get_data_from_soups()))
        print(g.get_data_from_soups())

    except Exception as e:
        print(e)


g =  Google_scraper("https://www.google.com/" , detach=False)
g.type_text(["addidas" ])
time.sleep(2)
try:
    post_feed(g.get_data_from_soups())
    print(g.get_data_from_soups())

except Exception as e:
    print(e)



# from pydantic import BaseModel
# from typing import Optional, List



# def post_feed(ad: AdData):
#     api_url = "https://4e02-2406-7400-56-ab78-6ce0-b010-bd9-1e58.ngrok-free.app/append/"  # Replace with your real URL
#     headers = {"Content-Type": "application/json"}
    
#     # Convert Pydantic model to dict
#     feed_data = ad.dict()  # or ad.model_dump() for Pydantic v2+

#     # Send as JSON
#     response = requests.post(api_url, json=feed_data, headers=headers)
    
#     return response.json() 

# class AdData(BaseModel):
#     Post_owner: str
#     Link: str
#     Ad_title: str
#     Ad_text: str
#     Direct_links: list
#     Small_links: list
#     Ad_position: int


# ad = AdData(
#     Post_owner="John Doe",
#     Link="https://example.com",
#     Ad_title="Sample Ad",
#     Ad_text="This is a sample ad text",
#     Direct_links=["https://link1.com", "https://link2.com"],
#     Small_links=["https://small1.com", "https://small2.com"],
#     Ad_position=1
# )

# print(post_feed(ad))