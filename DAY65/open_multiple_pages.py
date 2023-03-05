from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get('https://google.com')
driver.get('https://youtube.com')

driver.back()

driver.refresh()

driver.forward()

input()
driver.quit()

