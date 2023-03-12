import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://mypage.rediff.com/login/dologin"
driver.get(url)

driver.find_element(By.XPATH,"/html/body/div[3]/div[5]/div[1]/form/div[2]/input[3]").click()

driver.switch_to.alert.accept()


time.sleep(5)
driver.quit()

