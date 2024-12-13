import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find(name="a", class_="storylink")
article_text = article_tag.get_text()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").get_text()

print(
    f"""{article_text}
{article_link}
{article_upvote.split(" ")[0]}"""
)
