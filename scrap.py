import requests
from bs4 import BeautifulSoup
import datetime

# Get day of Today
dt = datetime.datetime.today()
dayToString = str(dt.day)

# Construct HTML Page
file = open("main.html", "w", encoding="utf-8")
file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awesomes websites of the day</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="header">
        <h1 class="header__title">Awesome websites of the day</h1>
    </header>
    <section class="block-list">
        <h2 class="block-list__title">From awwwards.com</h2>
        <ul class="block-list__items">
''')

# Scrap from awwwards.com
page = requests.get(f'https://www.awwwards.com/websites/nominees/')
soupdata = BeautifulSoup(page.content, "html.parser")
results = soupdata.find_all("li", class_="col-3 js-collectable")

for result in results:
    postDate = result.find("div", class_="content").find("div", class_="box-right")
    postDateFirst = postDate.text.split(",", 1)[0]
    postDay = postDateFirst.rsplit(' ', 1)[1]
    
    if dayToString == postDay:
        title = result.find("h3")
        link = result.find("a", class_="js-visit-item")
        file.write(f'''<li class="block-list__item"><a class="block-list__item-link" href="{link['href']}" target="_blank">{title.text}</a></li>''')

file.write('''
        </ul>
    </section>
    <section class="block-list">
        <h2 class="block-list__title">From cssdesignawards.com</h2>
        <ul class="block-list__items">
''')

# Scrap from cssdesignawards.com
page = requests.get(f'https://www.cssdesignawards.com/wotd-award-nominees')
soupdata = BeautifulSoup(page.content, "html.parser")
results = soupdata.find_all("article", class_="single-project")

for result in results:
    postDate = result.find("span", class_="sp__meta__date")
    postDay = postDate.text.rsplit(" ", 1)[1]
    
    if dayToString == postDay:
        title = result.find("h3", class_="single-project__title").find("a")
        link = result.find("a", class_="sp__project-link")
        file.write(f'''<li class="block-list__item"><a class="block-list__item-link" href="{link['href']}" target="_blank">{title.text}</a></li>''')

file.write('''
        </ul>
    </section>
</body>
</html>''')
