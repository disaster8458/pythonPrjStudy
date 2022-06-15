from bs4 import BeautifulSoup
import requests
import json
import lxml

req = requests.get('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EB%B9%84%EC%8A%A4%ED%8F%AC%ED%81%AC&pagingIndex=1&pagingSize=80&productSet=total&query=%EB%B9%84%EC%8A%A4%ED%8F%AC%ED%81%AC&sort=rel&timestamp=&viewType=list')

bs = BeautifulSoup(req.text, 'lxml')

result = bs.find('ul', class_='list_basis').find_all('a', class_='basicList_link__1MaTN')

# for i in result :
#     print(i.text)
# "products":{"list":
#
items = req.text.split('{"item":')

for i in range(1, len(items)-1) :
    item = items[i].split('productTitle":"')
    print(item[1].split('"')[0])


