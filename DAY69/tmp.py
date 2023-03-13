import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

url = "https://www.google.com"
driver.get(url)













time.sleep(10)
driver.quit()