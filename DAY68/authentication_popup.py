import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# url = "http://the-internet.herokuapp.com/basic_auth"
url = "http://admin:admin@the-internet.herokuapp.com/basic_auth"
driver.get(url)

time.sleep(15)