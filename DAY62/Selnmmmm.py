import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("Ada Lovelace" + Keys.ENTER)

time.sleep(10)
# input()

driver.quit();


