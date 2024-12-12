from bs4 import BeautifulSoup

PATH = "./Day 45"

with open(f"{PATH}/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.prettify())
