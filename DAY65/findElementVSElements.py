from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get('https://demo.nopcommerce.com/')



elements = driver.find_elements(By.LINK_TEXT,"nopCommerce-")
print(len(elements))



elements = driver.find_elements(By.LINK_TEXT,"nopCommerce")
print(len(elements))


# print(elements[0].get_attribute("href"))


input()
driver.quit()
