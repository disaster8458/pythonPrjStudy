import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyperclip
from bs4 import BeautifulSoup
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.maximize_window()
time.sleep(2)
driver.get('https://play.google.com/store/apps/details?id=com.towneers.www')

time.sleep(1)
body = driver.find_element(By.TAG_NAME, 'body')
body.send_keys(Keys.PAGE_DOWN)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
test = body.find_elements(By.CLASS_NAME, 'VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.QDwDD.DiOXab.VxpoF')
for i in test:
    if i.get_attribute('aria-label') == '평가 및 리뷰 자세히 알아보기' :
        i.click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'odk6He').click()
body = driver.find_element(By.TAG_NAME, 'body')
for i in range(10):
    body.send_keys(Keys.PAGE_DOWN)

html = driver.page_source
bs = BeautifulSoup(html, 'lxml')
content = bs.find_all('div', class_='h3YV2d')
print(content)