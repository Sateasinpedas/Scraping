from bs4 import BeautifulSoup
import requests
import pandas as pd

url = ('https://simak.ui.ac.id/reguler.html')

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table', class_= 'tablepress tablepress-id-33').find('tbody').find_all('tr')

major_list = []

for row in rows:
    temp = {}
    temp['Program Studi'] = row.find_all('td')[0].text
    temp['Peminat SIMAK 2021'] = row.find_all('td')[7].text    
    major_list.append(temp)    

df = pd.DataFrame(major_list)
df.to_excel('major-list-simak.xlsx',index=False)
df.to_csv('major-list-simak.xlsx',index=False)