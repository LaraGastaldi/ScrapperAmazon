import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging

URL = 'https://www.amazon.com.br/deals'

def get_products():
    timestamp = time.time()
    browser = webdriver.Chrome()
    browser.get(URL)
    WebDriverWait(browser, 5).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')) >= 8
    )
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    a = soup.find('section', 'wrapper')
    lasts = soup.find_all('div', attrs={'data-testid': 'product-card'})
    lasts = lasts[0:8]

    lasts_length = len(lasts)
    to_return = []
    for i in lasts:
        this_product = {}
        this_product['product_name'] = i.find('span', class_='a-truncate-full a-offscreen').text
        this_product['product_offer'] = i.find('div', attrs={"data-component": 'dui-badge'}).find('span').text
        this_product['product_image'] = i.find('img', class_='a-amazon-image').get('src')
        to_return.append(this_product)

    browser.quit()
    timestamp = time.time() - timestamp
    return {
        'lasts': to_return,
        'length': lasts_length,
        'run_time': timestamp
    }

if __name__ == '__main__':
    print(get_products())