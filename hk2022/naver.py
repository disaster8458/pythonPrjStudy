from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
hddata = {'User-agent':agent}

rank = []
title = []
date2 = []
point = []
for i in range(1,25) :
    num = '0' + str(i) if i < 10 else i
    date = '202205' + str(i).zfill(2)

    req = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date='+date, headers=hddata)

    soup = BeautifulSoup(req.text, 'lxml').find('table', class_='list_ranking').find('tbody')

    tr = soup.find_all('tr')

    for j in tr:
        try:
            print(j.find('img')['alt'])
            print(j.find('td', class_='title').text.strip())
            print(j.find('td', class_='point').text.strip())
            rank.append(j.find('img')['alt'])
            title.append(j.find('td', class_='title').text.strip())
            point.append(j.find('td', class_='point').text.strip())
            date2.append(date)
        except:
            print('error')

df = pd.DataFrame({'date':date2,'rank':rank,'title':title, '평점':point})

df.to_csv('movieRank.csv', encoding='utf-8')