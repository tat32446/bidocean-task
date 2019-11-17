import requests                # Include HTTP Requests module
from bs4 import BeautifulSoup  # Include BS web scraping module
data=[]
import pandas as pd

pages=[]

for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anA' + str(i) + '.htm'
    pages.append(url) 

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.content, 'html.parser')
    bodyText=soup.find("div",class_="BodyText")
    list_of_artiest=bodyText.find_all('a')
    table=bodyText.find('table')
    table_rows=table.find_all('tr')
    for td in table_rows:
        artist_info=td.find('a')
        finalUrl='https://web.archive.org'+artist_info.get('href')
        Dict={'name':artist_info.get_text(),'link':finalUrl}
        data.append(Dict)
        

author=pd.DataFrame(data)
author.to_csv('author.csv')
print(author.describe())