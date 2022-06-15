# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색

import os
import sys
import urllib.request
import json
import re
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
hddata = {'User-agent':agent}

# req = requests.get('https://blog.naver.com/PostList.naver?blogId=alanisms&categoryNo=96', headers=hddata)


client_id = "aKHNKPrX3ifTa7G4M2EK"
client_secret = "QUOsmAvsbi"

def naverSearch (search) :

    encText = urllib.parse.quote(search)
    blog_all_list = {}
    title_list = []
    description_list = []
    link_list = []

    for i in range(11) :
        start = (i*100) +1 if i < 10 else 1000
        parameter = '&display=100&sort=date&start=' + str(start)
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText +parameter# json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        p = re.compile('[^가-핳 ]')
        if(rescode==200):
            response_body = response.read()
            response_json = json.loads(response_body)
            blog_list = response_json['items']
            # print(blog_list)
            for i in blog_list :
                title_list.append(p.sub('',i['title']).strip())
                description_list.append(p.sub('',i['description']).strip())
                link_list.append(i['link'].strip())
        else:
            print("Error Code:" + rescode)
    # print(title_list)
    blog_all_list['제목'] = title_list
    blog_all_list['내용'] = description_list
    blog_all_list['주소'] = link_list
    # df = pd.DataFrame(blog_all_list)
    # df.to_csv(search+' 블로그.csv', encoding='utf-8')
    return blog_all_list

def makeCsv (dic_list, fileNm) :
    df = pd.DataFrame(dic_list)
    df.to_csv(fileNm+'.csv', encoding='utf-8')

# search = input('검색어를 입력해주세요. :')
# naverSearch()

def dataWordCloud(csv, name, fname):
    path = 'data/BMDOHYEON_ttf.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)

    text = pd.read_csv(csv+'.csv')
    text2 = ''
    for i in text[name] :
        text2 += str(i)
    text2 = re.compile('[^가-힣 ]d+').sub('', text2).strip()

    okt = Okt()

    noun_list = okt.nouns(text2)
    for t1, t2 in enumerate(noun_list):
        if len(t2) < 2:
            noun_list.pop(t1)

    count = Counter(noun_list)
    count_result = count.most_common(50)

    mask = np.array(Image.open('data/09. heart.jpg'))
    stopwords = set(STOPWORDS)

    wc = WordCloud(font_path='data/BMDOHYEON_ttf.ttf', background_color='white', max_words=2000, stopwords=stopwords,
                   mask=mask)

    wc = wc.generate(dict(count_result))
    wc.to_file(fname+'.jpg')

    plt.figure(figsize=(12, 12))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# dataWordCloud(search+' 블로그', '내용')

def naverCafe (search) :

    encText = urllib.parse.quote(search)
    cafe_all_list = {}
    title_list = []
    description_list = []
    link_list = []

    for i in range(11) :
        start = (i*100) +1 if i < 10 else 1000
        parameter = '&display=100&sort=date&start=' + str(start)
        url = "https://openapi.naver.com/v1/search/cafearticle.json?query=" + encText +parameter# json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        p = re.compile('[^가-핳 ]')
        if(rescode==200):
            response_body = response.read()
            response_json = json.loads(response_body)
            print(response_json)
            blog_list = response_json['items']
            # print(blog_list)
            for i in blog_list :
                title_list.append(p.sub('',i['title']).strip())
                description_list.append(p.sub('',i['description']).strip())
                link_list.append(i['link'].strip())
        else:
            print("Error Code:" + rescode)
    # print(title_list)
    cafe_all_list['제목'] = title_list
    cafe_all_list['내용'] = description_list
    cafe_all_list['주소'] = link_list
    print(len(title_list))
    # df = pd.DataFrame(blog_all_list)
    # df.to_csv(search+' 블로그.csv', encoding='utf-8')
    return cafe_all_list

# naverCafe('스타벅스')

def naverNews (search) :

    encText = urllib.parse.quote(search)
    News_all_list = {}
    title_list = []
    description_list = []
    link_list = []

    for i in range(11) :
        start = (i*100) +1 if i < 10 else 1000
        parameter = '&display=100&sort=date&start=' + str(start)
        url = "https://openapi.naver.com/v1/search/News.json?query=" + encText +parameter# json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        p = re.compile('[^가-핳 ]')
        if(rescode==200):
            response_body = response.read()
            response_json = json.loads(response_body)
            print(response_json)
            blog_list = response_json['items']
            # print(blog_list)
            for i in blog_list :
                title_list.append(p.sub('',i['title']).strip())
                description_list.append(p.sub('',i['description']).strip())
                link_list.append(i['link'].strip())
        else:
            print("Error Code:" + rescode)
    # print(title_list)
    News_all_list['제목'] = title_list
    News_all_list['내용'] = description_list
    News_all_list['주소'] = link_list
    print(len(title_list))
    # df = pd.DataFrame(blog_all_list)
    # df.to_csv(search+' 블로그.csv', encoding='utf-8')
    return News_all_list

# naverNews('스타벅스')

def naverNews (search) :

    encText = urllib.parse.quote(search)
    News_all_list = {}
    title_list = []
    description_list = []
    link_list = []

    for i in range(11) :
        start = (i*100) +1 if i < 10 else 1000
        parameter = '&display=100&sort=date&start=' + str(start)
        url = "https://openapi.naver.com/v1/search/News.json?query=" + encText +parameter# json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        p = re.compile('[^가-핳 ]')
        if(rescode==200):
            response_body = response.read()
            response_json = json.loads(response_body)
            print(response_json)
            blog_list = response_json['items']
            # print(blog_list)
            for i in blog_list :
                title_list.append(p.sub('',i['title']).strip())
                description_list.append(p.sub('',i['description']).strip())
                link_list.append(i['link'].strip())
        else:
            print("Error Code:" + rescode)
    # print(title_list)
    News_all_list['제목'] = title_list
    News_all_list['내용'] = description_list
    News_all_list['주소'] = link_list
    print(len(title_list))
    # df = pd.DataFrame(blog_all_list)
    # df.to_csv(search+' 블로그.csv', encoding='utf-8')
    return News_all_list

# naverNews('스타벅스')

def naverShop (search) :

    encText = urllib.parse.quote(search)

    title_list = []
    link_list = []
    lprice_list = []
    hprice_list = []

    for i in range(11) :
        start = (i*100) +1 if i < 10 else 1000
        parameter = '&display=100&sort=date&start=' + str(start)
        url = "https://openapi.naver.com/v1/search/shop.json?query=" + encText +parameter# json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        p = re.compile('[^가-핳 ]')
        if(rescode==200):
            response_body = response.read()
            response_json = json.loads(response_body)
            print(response_json)
            blog_list = response_json['items']
            # print(blog_list)
            for i in blog_list :
                title_list.append(p.sub('',i['title']).strip())
                link_list.append(i['link'].strip())
                lprice_list.append(i['lprice'])
                hprice_list.append(i['hprice'])
        else:
            print("Error Code:" + rescode)
    # print(title_list)
    shop_all_list = {'title':title_list, 'link':link_list, 'lprice':lprice_list, 'hprice':hprice_list}
    # print(len(title_list))
    # df = pd.DataFrame(blog_all_list)
    # df.to_csv(search+' 블로그.csv', encoding='utf-8')
    return shop_all_list

# naverShop('라면')

# r_list = naverSearch('스타벅스')
# makeCsv(r_list, '스타벅스 블로그')
# print(r_list)
df = pd.read_csv('스타벅스 블로그.csv')
blog_url_list = []
for i in list(df['주소']) :
    i = i.replace('https://', 'https://m.')
    blog_url_list.append(i)


def blog_content (url_list) :
    content = []
    for i in url_list:
        try :
            req = requests.get(i, headers=hddata)
            bs = BeautifulSoup(req.text, 'lxml')
            text = bs.find('div', class_='se-main-container').text.strip()
            print(text)
            content.append(text)
        except :
            print('오류')
            # content.append('오류'+i)
    return content

def dataWordCloud2 (text_list, name):
    path = 'data/BMDOHYEON_ttf.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)

    text2 = ''
    for i in text_list :
        text2 += str(i)
    text2 = re.compile('[^가-힣 ]d+').sub('', text2).strip()
    okt = Okt()

    noun_list = okt.nouns(text2)
    for t1, t2 in enumerate(noun_list):
        if len(t2) < 2:
            noun_list.pop(t1)

    count = Counter(noun_list)
    count_result = count.most_common(50)

    mask = np.array(Image.open('data/09. heart.jpg'))
    stopwords = set(STOPWORDS)
    stopwords.add('said')

    wc = WordCloud(font_path='data/BMDOHYEON_ttf.ttf', background_color='white', max_words=2000, stopwords=stopwords,
                   mask=mask)

    wc = wc.generate(dict(count_result))
    wc.to_file(name+'.jpg')

    plt.figure(figsize=(12, 12))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# content_list = blog_content(blog_url_list)
# dataWordCloud2(content_list, '스타벅스')
# print(content_list)