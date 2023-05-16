import threading
import openpyxl
from webinit_ import initBrowser
from login import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from single_page import single_page
from thread_asking import thread_asking
from url.mobilax import mobilax_urls
import os

## spliting urls into arrays for threading

url_splits = []
url_splits = []
threads = []
items = []


##thread_amount = thread_asking()
thread_amount = 5
category_pages = [line.strip() for line in mobilax_urls]
split_size = len(category_pages) // thread_amount
remainder = len(category_pages) % thread_amount


start = 0
for i in range(thread_amount):
    chunk_size = split_size + (1 if i < remainder else 0)
    url_split = category_pages[start:start+chunk_size]
    url_splits.append(url_split)
    start += chunk_size


init_driver = login(initBrowser(True))
WebDriverWait(init_driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "app-price")))
cookies = init_driver.execute_script("return document.cookie")
init_driver.quit()
for i, url_array in enumerate(url_splits) :
    thread = threading.Thread(target=single_page, args=(i, url_array, items, cookies.split(';')[1]))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
