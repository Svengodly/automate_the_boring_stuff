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

while not url.endswith("#"):
    logging.debug(url)
    pageRequest = requests.get(url)
    pageRequest.raise_for_status()
# logging.debug(pageRequest.text)
    pageHtml = bs4.BeautifulSoup(pageRequest.text, features='html.parser')
# logging.debug(pageHtml.select("#comic img"))
# logging.debug(pageHtml.select("br ~ a"))
    tagList = pageHtml.select("ul.comicNav a")
# logging.debug(tagList[0].get("href"))

# This gets us the url of the page that links to the image.
    try:
        imageLink = f'http:{pageHtml.select("#comic img")[0].get("src")}'

    except IndexError:
        print("Could not obtain image. Index Error")
        url = f"http://xkcd.com/{tagList[1].get('href')}"
        continue
    else:
        try:
            imagePage = requests.get(imageLink)
        except requests.exceptions.InvalidURL:
            print("Could not obtain image. Invalid URL")
            url = f"http://xkcd.com/{tagList[1].get('href')}"
            continue
        logging.debug(imagePage)
        imagePage.raise_for_status()
        logging.debug(imageLink)

        file = open(os.path.join("xkcd", os.path.basename(imageLink)), 'wb')

        # The new request is needed to retrieve the page with the image by itself. I received an error everytime
        # when trying to open the 'image' originally, and this was due to the fact that I was passing the 'pageRequest'
        # response, which was the url linking to the entire page and not just the image. I just want the image.
        for chunk in imagePage.iter_content(10000):
            file.write(chunk)
        file.close()
        # logging.debug(os.path.basename(imageLink))
        url = f"http://xkcd.com/{tagList[1].get('href')}"
# logging.debug(requests.get(f'https:{pageHtml.select("#comic img")[0].get("src")}'))
