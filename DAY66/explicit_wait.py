# implicit wait
# explicit wait
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
# mywait = WebDriverWait(driver, 10) # Explicit wait Decalration
# mywait = WebDriverWait(driver, 10, ignored_exceptions=[' NoSuchElementException', 'ElementNotVisibleException','ElementNotSelectableException'])  # Explicit wait Decalration
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
                       Exception])  # Explicit wait Decalration
# Poll frequency  will go and poll/check  every 2 seconds  if the item is there or not

driver.get("https://www.google.com")

searchbox = driver.find_elements(By.NAME, 'q')
# print(len(searchbox))
searchbox = searchbox[0]
searchbox.send_keys("selenium")
searchbox.submit()
# time.sleep(5)
# Performance of script is very
# If element is not available within the time mentioned, still there i schance of getting exception.
searchlink = mywait.until(EC.presence_of_element_located(
    (By.XPATH, '//h3[text()="Selenium"]')))
searchlink.click()

input()
driver.quit()


