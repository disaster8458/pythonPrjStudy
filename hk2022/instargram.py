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

search_keyword = input('검색어를 입력해 주세요 : ')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.maximize_window()
time.sleep(2)
driver.get('https://www.instagram.com/')

naverId = '01084581240'
naverPw = 'rhrnfu^^12'

time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').click()
pyperclip.copy(naverId)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(Keys.CONTROL, 'v')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').click()
pyperclip.copy(naverPw)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(Keys.CONTROL, 'v')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(10)
# body = driver.find_element(By.TAG_NAME, 'body')
time.sleep(2)
driver.find_element(By.CLASS_NAME, 'cTBqC').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME,'XTCLo.d_djL.DljaH').send_keys(search_keyword)
time.sleep(3)
driver.find_element(By.CLASS_NAME,'-qQT3').click()
time.sleep(15)
driver.find_element(By.CLASS_NAME,'eLAPa').click()
time.sleep(5)
text_list = []
text_list2 = []
for i in range(50) :
    time.sleep(5)
    html = driver.page_source
    bs = BeautifulSoup(html, 'lxml')

    data = ''
    try :
        data = bs.find('div', class_='C7I1f X7jCj').find('div', class_='MOdxS').text.strip()
        print(data)
        text_list.append(data)
    except :
        print('본문 없음')
        text_list.append(0)

    try :
        if data :
            data2 = bs.find_all('div', class_='MOdxS')[1:]
        else :
            data2 = bs.find_all('div', class_='MOdxS')
        text_list3 = []
        for i in data2 :
            print(i.get_text())
            text_list3.append(i.get_text())
        if text_list3 :
            text_list2.append(''.join(text_list3))
        else :
            text_list2.append(0)
    except :
        print('댓글 없음')
        text_list2.append(0)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'l8mY4.feth3').click()

print(len(text_list))
print(len(text_list2))
df = pd.DataFrame({'타이틀':text_list,'댓글':text_list2})

df.to_csv('instargram2.csv', encoding='utf-8')