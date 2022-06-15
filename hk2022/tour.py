import requests
import pandas as pd
from bs4 import BeautifulSoup
import lxml
import naverApi

keyid = '1X+3iAzHbeYpq9wOi0StP/WhGEaPM7GvfknN3angVGJGQ5Uw9z8Sxuvy3/of4ggk+wjRqaDKnjKuaRAG09nTwQ=='

url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/searchFestival'

params ={'serviceKey' : keyid, 'numOfRows' : 1000, 'pageNo' : '1', 'MobileOS' : 'ETC', 'MobileApp' : 'AppTest' }

response = requests.get(url, params=params)
# print(response.text)

bs = BeautifulSoup(response.text, 'lxml')
fdata = bs.find_all('item')
flist = []
for i in fdata :
    try :
        title = i.find('title').text
        add = i.find('addr1').text
        sdate = i.find('eventstartdate').text
        edate = i.find('eventenddate').text
        mapx = i.find('mapx').text
        mapy = i.find('mapy').text
        fdict = {'축제명':title, '주소':add, '시작일':sdate, '종료일':edate, '위도':mapy, '경도':mapx }
        flist.append(fdict)
    except :
        print('오류')

# naverApi.makeCsv(flist, '전국축제현황')