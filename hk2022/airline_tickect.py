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
driver.get('https://flight.naver.com/')
body = driver.find_element(By.TAG_NAME, 'body')
body.find_elements(By.CLASS_NAME, 'searchBox_text__nUcMZ')[1].click()
body.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]').click()
body.find_element(By.CLASS_NAME, 'autocomplete_input__1vVkF').send_keys('김포')
time.sleep(1)
body.find_element(By.CLASS_NAME, 'autocomplete_search_item__2WRSw').click()
time.sleep(1)
body.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
body.find_element(By.CLASS_NAME, 'autocomplete_input__1vVkF').send_keys('제주')
time.sleep(1)
body.find_element(By.CLASS_NAME, 'autocomplete_search_item__2WRSw').click()
time.sleep(1)
body.find_element(By.CLASS_NAME, 'tabContent_option__2y4c6').click()
time.sleep(1)
# body.find_element(By.CLASS_NAME, 'day.today').click()
body.find_elements(By.CLASS_NAME, 'day')[27].click()
body.find_element(By.CLASS_NAME, 'searchBox_search__2KFn3').click()
time.sleep(10)

html = driver.page_source
bs = BeautifulSoup(html, 'lxml').find_all('div', class_='domestic_Flight__sK0eA result')

airline_list = []
start_list = []
arrive_list = []
fare_list = []
r_list = []
for i in bs :

    fare = i.find(class_='domestic_num__2roTW').text
    airline = i.find(class_='airline').text
    start = i.find(class_='route_time__-2Z1T').text
    arrive = i.find_all(class_='route_time__-2Z1T')[1].text

    airline_list.append(airline)
    start_list.append(start)
    fare_list.append(fare)
    arrive_list.append(arrive)
    rdict={'항공사':airline, '출발':start, '도착':arrive, '가격':fare}
    r_list.append(rdict)

print(r_list)