# Web Scraping with Selenium and BeautifulSoup

## Overview
This script performs web scraping using Selenium and BeautifulSoup to extract data from a webpage that requires login authentication.

## Code Explanation

### Importing Libraries
```python
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
```

- bs4 (BeautifulSoup): Used for parsing HTML content. (not really used in this demo but needed to get data off site)
- Selenium: Used for automating web browser interactions.
- By: Used for locating elements on a webpage.
- time: Used for adding delays in the script execution.

## Setting Working Directory

The idea here is if you want to export some data to a csv file you'd have a path defined. 

```python
path_out = ""
```

## Defining Web Scraping Parameters

This point to the url you want to scrape, along with the Username & Password for authentication. 

```python
url = ""
UN = ""
PW = ""
```

## Web Scraping Process

1. Initializes a Chrome WebDriver instance and navigates to the specified URL.
2. Locates the username and password input fields, enters the credentials, and submits the login form.
3. Retrieves the page source after login.
4. Parses the page source using BeautifulSoup.
5. Prints the parsed HTML content of the webpage. (this you would expand on for your project)

```python
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
soup = bs(web_data, "html.parser")
print(soup)
```

This script demonstrates how to automate the process of logging into a webpage and extracting HTML content for further processing.
