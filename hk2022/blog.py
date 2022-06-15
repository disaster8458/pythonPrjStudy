from bs4 import BeautifulSoup
import requests
import re
import lxml

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
hddata = {'User-agent':agent}

# req = requests.get('https://blog.naver.com/PostList.naver?blogId=alanisms&categoryNo=96', headers=hddata)
req = requests.get('https://m.blog.naver.com/alanisms/222721879170', headers=hddata)

soup = BeautifulSoup(req.text, 'lxml')

title = soup.find('div', class_='se-module se-module-text se-title-text').text.strip()

content = soup.find_all('div', class_='se-component se-text se-l-default')

contentList = []
for i in content :
    contentList.append(i.text.strip())

# print(' '.join(contentList))
p = re.compile('[^A-Za-z가-힣0-9 ]+').sub('', ' '.join(contentList))
# m = p.match(' '.join(contentList))
print(p)