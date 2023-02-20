from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)
url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'
driver.get(url)
items = []
last_height = driver.execute_script('return document.body.scrollHeight')
itemTargetCount = 20
while itemTargetCount > len(items):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height == new_height
    elements = driver.find_elements(By.XPATH, "//div[@class='card-body']/h4/a")
    h4_texts = [element.text for element in elements]
    items.extend(h4_texts)
    print(h4_texts)


