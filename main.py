import requests
from bs4 import BeautifulSoup
import lxml

response = requests
with open("website.html", encoding='utf-8') as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, 'lxml.parser')
print(soup.title)
print(soup.title.string)
print(soup.prettify())
print(soup.a)
print(soup.p)
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
for tag in all_anchor_tags:
    print(tag.get_text())
    print(tag.get("href"))
heading = soup.find(name="h1",id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.get("class"))

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

h3_heading = soup.find_all("h3", class_="heading")
print(h3_heading)
soup.find_all("a")

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)
