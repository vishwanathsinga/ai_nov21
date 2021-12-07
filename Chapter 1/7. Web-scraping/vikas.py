import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.Ya9wndCZPIW")


soup = BeautifulSoup(page.content,'html.parser')


seven_day = soup.find(id="seven-day-forecast")


forecast_items = seven_day.find_all(class_="tombstone-container")

tonight = forecast_items[0]


period=[]
period=  tonight.find(class_="period-name")


short_desc=[]
short_desc = tonight.find(class_="short-desc")



temp=[]
temp = tonight.find(class_="temp")



desc=[]
img = tonight.find("img")
desc  = img['title']

period_tags=[]
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]


short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]

temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]

descs = [d["title"] for d in seven_day.select(".tombstone-container img")]



import pandas as pd
import numpy as np


weather = pd.DataFrame({"period": periods,"short_desc":short_descs,"temp":temps,"desc":desc})

weather