#base for SolData pull
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#set wd
path_out = ""

#webscrape
url = ""

UN = ""
PW = ""


#web scrape
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

username = driver.find_element(By.NAME, "email") 
password = driver.find_element(By.NAME, "password")

username.send_keys(UN)
password.send_keys(PW)

time.sleep(2)

submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_button.click()

time.sleep(5)

web_data = driver.page_source
soup =bs(web_data, "html.parser")
print(soup)
