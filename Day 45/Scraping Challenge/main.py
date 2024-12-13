import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
PATH = "./Day 45/Scraping Challenge"

# Write your code below this line 👇
response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

movie_data = soup.find_all(name="h3", class_="title")

movie_titles = []
for movie in movie_data:
    movie_titles.append(movie.get_text())

movie_titles.reverse()

with open(f"{PATH}/movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.writelines(f"{movie}\n")