import requests
import bs4
import webbrowser
""""Retrieve features page and list the most commented articles."""
# Need to make an HTTP request for the webpage

pageResponse = requests.get("https://arstechnica.com/features")

# Check response

pageResponse.raise_for_status()
# print(pageResponse.status_code)

# Let's see what we have
# print(pageResponse.text)

# Need to analyze html with Beautiful Soup
parsedPage = bs4.BeautifulSoup(pageResponse.text, features="html.parser")

# Find feature story. They can be found within list tags that have the 'tease,' 'article,' and 'top-feature' classes.
tagObjects = parsedPage.select("h2 > a")

# Going to gather a list of the names of the articles.
articleNames = []
articleLinks = []
for article in tagObjects:
    articleNames.append(article.text)
    articleLinks.append(article.get("href"))
# Next, I retrieve the number of comments tied to each article.
comments = parsedPage.select("span.comment-count-number")
commentCounts = []
for amount in comments:
    commentCounts.append(amount.text)

# Use the zip function to group the two lists together, then pass that zip tuple to the dict() function to make a
# dictionary.
countsAndLinks = list(zip(commentCounts, articleLinks))

# A dictionary that ties together the article names along with their corresponding links.
articleCommentCount = dict(zip(articleNames, countsAndLinks))

# Sort dictionary by the amount of comments per article.
sortedList = sorted(articleCommentCount.items(), key=lambda art: int(art[1][0]), reverse=True)

# Get top 5 articles by comments and open them in the browser.
for article in sortedList[:5]:
    print(f"'{article[0]}' has {article[1][0]} comments")
    webbrowser.open(article[1][1])
