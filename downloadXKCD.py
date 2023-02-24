#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import webbrowser
import requests
import os
import bs4
import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

url = "http://xkcd.com/"
#os.makedirs("xkcd", exist_ok=True)

# while not url.endswith("#"):

pageRequest = requests.get(url)
pageRequest.raise_for_status()
logging.debug(pageRequest.text)
pageHtml = bs4.BeautifulSoup(pageRequest.text, features='html.parser')
logging.debug(pageHtml.select("#comic img"))
