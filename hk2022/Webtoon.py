from bs4 import BeautifulSoup
import requests
import lxml

req = requests.get('https://comic.naver.com/index')

bs = BeautifulSoup(req.text, 'lxml')

result = bs.find('div', class_='todayChallenge')
result = result.find('dd', class_='ellipsis_content')
result = result.find('a')
rtext = result.text
print(rtext.strip())

result = bs.find('div', class_='notice_rolling')
result = result.find('a').text
print(result.strip())

req = requests.get('https://comic.naver.com/genre/bestChallenge')

bs = BeautifulSoup(req.text, 'lxml')
result = bs.find('div', class_='ucc_msgnotice').text
print(type(result))

req = requests.get('https://comic.naver.com/index')
bs = BeautifulSoup(req.text, 'lxml')

result = bs.find('div', class_='genreRecomBox_area').find_all('h6', class_='title')

for i in result :
    print(i.text)

result = bs.find(id='realTimeRankFavorite').find_all('a')

for i in result :
    print(i.text)