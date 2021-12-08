import requests
from bs4 import BeautifulSoup

page = requests.get("https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c")
soup = BeautifulSoup(page.content,'html.parser')
soup.prettify()



list =soup.find("div" ,class_="LocationPageTitle")

print(list)


