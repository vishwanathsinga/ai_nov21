from types import ClassMethodDescriptorType
import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.Ya9wndCZPIW")


soup = BeautifulSoup(page.content,'html.parser')


seven_day = soup.find(id="seven-day-forecast")


forecast_items = seven_day.find_all(class_="tombstone-container")

tonight = forecast_items[0]




week=[]
week =  tonight.find(class_="period-name")


event=[]
event = tonight.find(class_="short-desc")



temp=[]
temp = tonight.find(class_="temp")



report=[]
img = tonight.find("img")
report  = img['title']

day_tags=[]
day_tags = seven_day.select(".tombstone-container .period-name")
days = [pt.get_text() for pt in day_tags]


events = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]

temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]

reports = [d["title"] for d in seven_day.select(".tombstone-container img")]





import pandas as pd
import numpy as np

perfect = pd.DataFrame({"week":  days,
 "event":events,
  "temp":temps, 
  "report": reports })
perfect





