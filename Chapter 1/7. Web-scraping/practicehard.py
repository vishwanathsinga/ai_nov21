import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YbD61L2ZPIU")

soup = BeautifulSoup(page.content, "html.parser")

div = soup.find(id="seven-day-forecast",class_="panel")

panel = soup.find_all("div",class_="tombstone-container")

sam = panel[1]
print(sam.text)


'''
container = soup.find_all("p",class_="period-name")

john = container[1]
print(john.prettify())'''




