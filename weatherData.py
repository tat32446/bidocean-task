import requests                # Include HTTP Requests module
from bs4 import BeautifulSoup  # Include BS web scraping module
data=[]
import pandas as pd


page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
##print(tonight.prettify())

for tonight in forecast_items:
    period=tonight.find(class_="period-name").get_text()
    short_desc=tonight.find(class_="short-desc").get_text()
    temperature=tonight.find(class_="temp").get_text()
    
    img=tonight.find('img')
    description=img['title']
    Dict={}
    Dict={'period':period,'short_desc':short_desc,
    'temperature':temperature,'description':description}
    data.append(Dict)

weather = pd.DataFrame(data)
weather.to_csv('weather.csv')
print(weather.head())

