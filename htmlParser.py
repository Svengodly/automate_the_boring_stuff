#! python3

import requests
import logging
import bs4
import webbrowser
import sys

"""Program that takes makes a google search from users input and automatically opens the browser for each of those
pages."""

# TODO: Enable users to input text via the command line.

logging.basicConfig(level=logging.CRITICAL)
print(sys.path)
# Needed to determine the uri of a Google search. There were other variables after "q", but those kept changing.
# I also noticed that the html in ME was different from the html retrieved by the 'requests' module. This is because
# Javascript running in ME, and 'requests' is not able to handle Javascript. As a workaround, I temporarily disabled
# Javascript in the developer tools by pressing Ctrl + Shift + P and searched for 'JavaScript.'
res = requests.get(f"https://www.google.com/search?q={''.join(sys.argv[1:])}")

# Check for a 200 or "OK" response from the server.
res.raise_for_status()

# Use Beautiful Soup to create a BS4 object, which enables me to filter out elements from the html document.
bs4Object = bs4.BeautifulSoup(res.text, features="html.parser")

logging.debug(bs4Object.contents)

# This returns a list of elements which are Tag Objects filtered by using a CSS selector.
# Had to take a look at the html of the search results page through dev tools to determine how each of the anchor tags
# were nested. I found that the large-texted tags were in div tags with the following two classes.
tagObjects = bs4Object.select("div.egMi0.kCrYT a")
for number in range(3):
    logging.debug(tagObjects[number])
    logging.debug(tagObjects[number].get("href"))
    webbrowser.open(f'https://www.google.com{tagObjects[number].get("href")}')

logging.debug(bs4Object)
