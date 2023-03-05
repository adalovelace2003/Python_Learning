import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")


# driver.find_element(By.LINK_TEXT, "Digital downloads").click()

links = driver.find_elements(By.XPATH,'//a')
print(len(links))

for link in links:
    print(link.texthttp://www.deadlinkcity.com/)


time.sleep(10)
