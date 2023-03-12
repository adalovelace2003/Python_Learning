import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/ul/li[3]/button").click()

alertwindow = driver.switch_to.alert

print(alertwindow.text) 


alertwindow.send_keys("Welcome")
# alertwindow.accept()
alertwindow.dismiss()


time.sleep(5)
driver.quit()

