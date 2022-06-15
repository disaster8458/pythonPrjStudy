import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyperclip
from bs4 import BeautifulSoup
import re
import pandas as pd
import lxml

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.maximize_window()
time.sleep(2)
driver.get('https:youtube.com')

body = driver.find_element(By.TAG_NAME, 'body')
body.find_element(By.ID, 'search').click()
body.find_element(By.ID, 'search').send_keys('여자 아이들 미연')
time.sleep(1)
body.find_element(By.ID, 'search').send_keys(Keys.ENTER)

time.sleep(1)
body = driver.find_element(By.TAG_NAME, 'body')

for i in range(20):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

html = driver.page_source
bs = BeautifulSoup(html, 'lxml')
rs = bs.find_all('div', id='dismissible')
p = re.compile('[^a-zA-Z가-힣0-9 ]')
result_txt = ''
url_list = []
for i in rs :
    try :
        title = i.find('h3', class_='title-and-badge style-scope ytd-video-renderer')
        link = i.find('h3', class_='title-and-badge style-scope ytd-video-renderer').find('a')['href']
        url_list.append(i.find('h3', class_='title-and-badge style-scope ytd-video-renderer').find('a'))
        result_txt += title.text.strip()
    except :
        1 == 1

thnumbnail = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')
comment = []
for i in thnumbnail :
    try:
        time.sleep(1)
        i.click()
        time.sleep(2)
        for j in range(20):
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.PAGE_DOWN)

        html = driver.page_source
        bs = BeautifulSoup(html, 'lxml')

        rs = bs.find_all('yt-formatted-string', id='content-text')
        for x in rs:
            comment.append(x.text.strip())
            print(x.text)
    except :
        1 == 1

    time.sleep(1)
    driver.back()
df = pd.DataFrame({'댓글':comment})
df.to_csv('미연 댓글 모음.csv', encoding='utf-8')