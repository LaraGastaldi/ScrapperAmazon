import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging

url = 'https://www.amazon.com.br/deals'

browser = webdriver.Chrome()
browser.get(url)
WebDriverWait(browser, 5).until(
    lambda d: len(d.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')) >= 8
)
soup = BeautifulSoup(browser.page_source, 'html.parser')
a = soup.find('section', 'wrapper')
lasts = soup.find_all('div', attrs={'data-testid': 'product-card'})
lasts = lasts[0:8]

with open('lasts.log', 'a') as f:
    f.write(time.strftime("[%Y-%m-%d %H:%M:%S]") + '\n')
    print(len(lasts))
    for i in lasts:
        pass
        # print(i)
browser.quit()