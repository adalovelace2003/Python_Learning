# implicit wait
# explicit wait
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.implicitly_wait(10)
# this is applicabble for all the places where synchronization error occurs.
# it will not wait for the maximum time
# as soon as the element is available , it will go and execute the next statement.

driver.get("https://www.google.com")

searchbox = driver.find_elements(By.NAME, 'q')
# print(len(searchbox))
searchbox = searchbox[0]
searchbox.send_keys("selenium")
searchbox.submit()

# time.sleep(5)
# Performance of script is very
# If element is not available within the time mentioned, still there i schance of getting exception.


selenium = driver.find_element(By.XPATH, '//h3[text()="Selenium"]')
selenium.click()

input()
driver.quit()
