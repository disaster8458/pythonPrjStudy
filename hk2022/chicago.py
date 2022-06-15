from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
import lxml

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
hddata = {'User-agent':agent}
url = 'https://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'

req = requests.get(url, headers=hddata)

soup = BeautifulSoup(req.text, 'lxml').find_all('div', class_='sammy')

rank = []
main_menu = []
cafe_name = []
url_list = []

for i in soup :
    rank2 = i.find('div', class_='sammyRank').text
    menu = i.find('div', class_='sammyListing').find('b').text
    cafe = i.find('div', class_='sammyListing').text.split('\n')[1]
    url = i.find('div', class_='sammyListing').find('a')['href']
    if 'https://' not in url :
        url = 'https://www.chicagomag.com/' + url
    rank.append(rank2)
    main_menu.append(menu)
    cafe_name.append(cafe)
    url_list.append(url)

r_data = {'homepage':[],'price':[],'phone':[],'address':[]}
r_data['rank'] = rank
r_data['main_menu'] = main_menu
r_data['cafe_name'] = cafe_name
r_data['url_list'] = url_list

df = pd.DataFrame({'rank':rank, 'cafe': cafe_name, 'menu':main_menu, 'url':url_list})

# df.to_csv('chicago_sandwiches.csv', encoding='utf-8')



for i in url_list :
    req1 = requests.get(i, headers=hddata)

    soup1 = BeautifulSoup(req1.text, 'lxml')
    rdata = soup1.find('p', class_='addy').text

    price = rdata.split('.')[0].replace('\n','')
    url = rdata.split(' ')[-1]
    tel = rdata.split(' ')[-2].replace(',','')
    address = ' '.join(rdata.split(' ')[1: -2]).replace(',','')
    r_data['price'].append(price)
    r_data['homepage'].append(url)
    r_data['phone'].append(tel)
    r_data['address'].append(address)
    print(rdata)


# df = pd.DataFrame({'rank':rank, 'cafe': cafe_name, 'menu':main_menu, 'url':url_list, 'homepage':r_data['homepage'],
#                    'price':r_data['price'], 'phone':r_data['phone'], 'address':r_data['address']})
# df.to_csv('chicago_sandwiches.csv', encoding='utf-8')