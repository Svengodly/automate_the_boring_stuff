#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import webbrowser
import requests
import os
import bs4
import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

url = "http://xkcd.com/"
os.makedirs("xkcd", exist_ok=True)

# while not url.endswith("#"):

pageRequest = requests.get(url)
pageRequest.raise_for_status()
# logging.debug(pageRequest.text)
pageHtml = bs4.BeautifulSoup(pageRequest.text, features='html.parser')
# logging.debug(pageHtml.select("#comic img"))
# logging.debug(pageHtml.select("br ~ a"))
# tagList = pageHtml.select("br ~ a")
# logging.debug(tagList[0].get("href"))

# This gets us the url of the page that links to the image.
imageLink = f'http:{pageHtml.select("#comic img")[0].get("src")}'
logging.debug(imageLink)

file = open(os.path.join("xkcd", os.path.basename(imageLink)), 'wb')

# The new request is needed to retrieve the page with the image by itself. I received an error everytime when trying
# to open the 'image' originally, and this was due to the fact that I was passing the 'pageRequest' response, which
# was the url linking to the entire page and not just the image. I just want the image.
for chunk in requests.get(imageLink).iter_content(2000):
    logging.debug(chunk)
    file.write(chunk)
file.close()
logging.debug(os.path.basename(imageLink))
# logging.debug(requests.get(f'https:{pageHtml.select("#comic img")[0].get("src")}'))
