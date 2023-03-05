import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.deadlinkcity.com/")

links = driver.find_elements(By.TAG_NAME,"a")

for link in links:
    try:
        href = link.get_attribute("href")
        request = requests.get(href)
        if request.status_code >= 400:
            print(href + "is a broken link")
        else:
            print(href + "is a valid link")
    except:
        None


print(len(links))