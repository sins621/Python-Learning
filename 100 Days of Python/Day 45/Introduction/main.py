from bs4 import BeautifulSoup

PATH = "./Day 45"

with open(f"{PATH}/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.get("href"))


# heading = soup.find(name="h1", id="name")
# print(heading.get_text())

# section_heading = soup.find(name = "h3", class_="heading")
# print(section_heading.get("class"))
name = soup.select_one(selector="#name")
# print(name)


heading = soup.select(".heading")
print(heading)