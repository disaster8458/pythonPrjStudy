import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyperclip
from bs4 import BeautifulSoup
import pandas as pd
import re
import lxml
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from konlpy.tag import Okt
from collections import Counter
import urllib.request
import json
import requests

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
hddata = {'User-agent': agent}

# req = requests.get('https://blog.naver.com/PostList.naver?blogId=alanisms&categoryNo=96', headers=hddata)

def naverSearchNews(search, pgNum=10, ds='2022.05.18', de='2022.05.20'):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    title_list = []
    content_list = []
    driver.maximize_window()
    time.sleep(2)
    driver.get('https://www.naver.com/')

    driver.find_element(By.ID, 'query').send_keys(search)
    time.sleep(1)
    driver.find_element(By.ID, 'search_btn').click()
    time.sleep(1)
    menu = driver.find_elements(By.CLASS_NAME, 'menu')

    for i in menu:
        try:
            if i.text == '뉴스':
                i.click()
        except:
            break
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'btn_option._search_option_open_btn').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'txt.txt_option._calendar_select_trigger').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'btn_apply._apply_btn').click()

    url = driver.current_url

    try:
        url = url.split('ds=')
        url = url[0] + 'ds=' + ds + '&de=' + de + url[1][24:]
    except:
        1 == 1
        url = url.split('Afrom')
        url = url[0] + 'Afrom' + ds + 'to' + de

    driver.get(url)
    news_url = []

    for i in range(pgNum):
        ls = driver.find_element(By.CLASS_NAME, 'list_news').find_elements(By.CLASS_NAME, 'bx')
        for i in ls:
            for j in i.find_element(By.CLASS_NAME, 'info_group').find_elements(By.TAG_NAME, 'a'):
                if j.text == '네이버뉴스':
                    news_url.append(j.get_attribute('href'))
        time.sleep(1)
        if driver.find_element(By.CLASS_NAME, 'btn_next').get_attribute('aria-disabled') == True:
            break;
        driver.find_element(By.CLASS_NAME, 'btn_next').click()
        time.sleep(2)

    title = ''
    content = ''
    count = 0;
    for i in news_url:
        try :
            req = requests.get(i, headers=hddata)
            bs = BeautifulSoup(req.text, 'lxml')
            title += bs.find('h2', class_='media_end_head_headline').text.strip()
            content += bs.find('div', id='dic_area').text.strip()
            title_list.append(bs.find('h2', class_='media_end_head_headline').text.strip())
            content_list.append(bs.find('div', id='dic_area').text.strip())
        except :
            count += 1
            print(str(count) + '오류횟수')

    return {'title': title_list, 'content': content_list}

def naverSearchView(search, pgNum=10, ds='20220518', de='20220528'):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    title_list = []
    content_list = []
    driver.maximize_window()
    time.sleep(2)
    driver.get('https://www.naver.com/')

    driver.find_element(By.ID, 'query').send_keys(search)
    time.sleep(1)
    driver.find_element(By.ID, 'search_btn').click()
    time.sleep(1)
    menu = driver.find_elements(By.CLASS_NAME, 'menu')

    for i in menu:
        try:
            if i.text == 'VIEW':
                i.click()
        except:
            break
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'btn_option._search_option_open_btn').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'txt.txt_option._calendar_select_trigger').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'btn_apply._apply_btn').click()

    url = driver.current_url

    spOk = 0
    try:
        url = url.split('ds=')
        url = url[0] + 'ds=' + ds + '&de=' + de + url[1][24:]
    except:
        1 == 1
        spOk = 1

    if spOk == 1:
        try:
            url = driver.current_url
            url = url.split('Afrom')
            url = url[0] + 'Afrom' + ds + 'to' + de + url[1][18:]

        except:
            1 == 1
    driver.get(url)
    view_url = []
    body = driver.find_element(By.TAG_NAME, 'body')
    for a in range(pgNum):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    ls = driver.find_element(By.CLASS_NAME, 'lst_total._list_base').find_elements(By.CLASS_NAME, 'total_area')
    for i in ls:
        view_url.append(i.find_element(By.CLASS_NAME, 'api_txt_lines.total_tit._cross_trigger').get_attribute('href'))

    title = ''
    content = ''
    count = 0
    for i in view_url:
        try:
            if i[8:12] == 'blog':
                print(i[:8] + 'm.' + i[8:])
                req = requests.get(i[:8] + 'm.' + i[8:], headers=hddata)
                bs = BeautifulSoup(req.text, 'lxml')

                # print(bs.find('div', class_='se-module se-module-text se-title-text').text.strip())
                # print(bs.find('div', class_='se-main-container').text.strip())
                # title += bs.find('div', class_='se-module se-module-text se-title-text').text.strip()
                # content += bs.find('div', id='se-main-container').text.strip()
                title_list.append(bs.find('div', class_='se-module se-module-text se-title-text').text.strip())
                content_list.append(bs.find('div', class_='se-main-container').text.strip())
                print('blog')
            elif i[8:12] == 'cafe':
                driver.get(i[:8] + 'm.' + i[8:])
                time.sleep(1)
                html = driver.page_source
                bs = BeautifulSoup(html, 'lxml')
                print('cafe')
                title += bs.find('h2', class_='tit').text.strip()
                content += bs.find('div', class_='se-module se-module-text').text.strip()
                title_list.append(bs.find('h2', class_='tit').text.strip())
                content_list.append(bs.find('div', class_='se-module se-module-text').text.strip())
                driver.back()
                time.sleep(1)
        except:
            count += 1
            print(str(count) + '오류 횟수')

    return {'title': title_list, 'content': content_list}

def csvSave (fNm, dic_list):
    print(1)
    df = pd.DataFrame(dic_list)
    df.to_csv(fNm + '.csv', encoding='utf-8')

# votedEarlyNews = naverSearchNews('김은혜', 20)
# csvSave('사전투표전 김은혜 뉴스', votedEarlyNews)

# votedEarlyView = naverSearchView('김은혜', 15)
# csvSave('사전투표전 김은혜 View', votedEarlyView)

# votedNews = naverSearchNews('김은혜', 20, '2022.05.29', '2022.06.01')
# csvSave('사전투표후 김은혜 뉴스', votedNews)
#
# votedView = naverSearchView('김은혜', 15, '20220529', '20220601')
# csvSave('사전투표후 김은혜 View', votedView)

# votedNews = naverSearchNews('오영훈', 20, '2022.05.20', '2022.06.01')
# csvSave('오영훈 뉴스', votedNews)
#
# votedView = naverSearchView('제주지사', 15, '20220520', '20220601')
# csvSave('오영훈 View', votedView)

def dataWordCloud(csv, name, fname, exceptList):
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
    dict_count = dict(count_result)
    mask = np.array(Image.open('data/korea.png'))
    stopwords = set(STOPWORDS)
    print(dict_count)
    for i in exceptList :
        try :
            del dict_count[i]
        except :
            1 == 1

    wc = WordCloud(font_path='data/BMDOHYEON_ttf.ttf', background_color='white', max_words=2000, stopwords=stopwords,
                   mask=mask)

    wc = wc.generate_from_frequencies(dict_count)
    wc.to_file(fname+'.jpg')

    plt.figure(figsize=(12, 12))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    # plt.show()

# dataWordCloud('사전투표전 김은혜 뉴스', 'title', '사전투표전 김은혜 뉴스제목', ['김은혜', '김동연'])
# dataWordCloud('사전투표전 김은혜 뉴스', 'content', '사전투표전 김은혜 뉴스', ['김은혜', '김동연'])
# dataWordCloud('사전투표전 김은혜 View', 'title', '사전투표전 김은혜 View제목', ['김은혜', '김동연'])
# dataWordCloud('사전투표전 김은혜 View', 'content', '사전투표전 김은혜 View', ['김은혜', '김동연'])
# dataWordCloud('사전투표후 김은혜 뉴스', 'title', '사전투표후 김은혜 뉴스제목', ['김은혜', '김동연'])
# dataWordCloud('사전투표후 김은혜 뉴스', 'content', '사전투표후 김은혜 뉴스', ['김은혜', '김동연'])
# dataWordCloud('사전투표후 김은혜 View', 'title', '사전투표후 김은혜 View제목', ['김은혜', '김동연'])
# dataWordCloud('사전투표후 김은혜 View', 'content', '사전투표후 김은혜 View', ['김은혜', '김동연'])
