import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyperclip

naverId = ''
naverPw = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.maximize_window()
time.sleep(2)
driver.get('https:naver.com')


driver.find_element(By.CLASS_NAME, 'link_login').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="id"]').click()
pyperclip.copy(naverId)
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v')
driver.find_element(By.XPATH,'//*[@id="pw"]').click()
pyperclip.copy(naverPw)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)
driver.find_element(By.ID, 'frmNIDLogin').submit()