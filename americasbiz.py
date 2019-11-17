import requests                # Include HTTP Requests module
from bs4 import BeautifulSoup  # Include BS web scraping module
import json
import pandas as pd
data=[]
Dict={}


pages=[]

for i in range(1, 16):
    url = 'https://americasbiz.net/bid_opportunities/2019/11/' + str(i).zfill(2) + '/state/46/'
    pages.append(url) 


for item in pages:
    r = requests.get(item)         # Sends HTTP GET Request
    print(r.status_code)            # ---> Print HTML status code <---
    soup = BeautifulSoup(r.text, "html.parser") # Parses HTTP Response
    table = soup.find('table')
    if table is not None:
        table_rows = table.find_all('tr')
        for tr in table_rows:
            td_list=tr.find_all('td')
            for td in td_list:
                print(td.text)
                print(tr.children)
            for childs in tr.children:
                print(childs.get_text())
                links = tr.find_all('a')
                for link in links:
                    Dict = {'name': link.get_text(), 'url':link.get('href')}
                    if(len(Dict.keys())>1):
                        data.append(Dict)
bid_info=pd.DataFrame(data)
bid_info.to_csv('bid_info.csv') 
print('Your File is ready in project directory:bid_info.csv')












