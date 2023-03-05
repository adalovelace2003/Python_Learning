# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# mywait = WebDriverWait(driver, 10,poll_frequency=2 ,ignored_exceptions=[Exception])  # Explicit wait Decalration
# driver.get("https://www.google.com")
# searchbox = driver.find_elements(By.NAME, 'q')
# searchbox = searchbox[0]
# searchbox.send_keys("selenium")
# searchbox.submit()
# searchlink = mywait.until(EC.presence_of_element_located((By.XPATH, '//h3[text()="Seleniuma"]')))
# searchlink.click()
# input()
# driver.quit()




# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# mywait = WebDriverWait(driver, 10, ignored_exceptions=[Exception])

# driver.get("https://www.google.com")

# searchbox = driver.find_elements(By.NAME, 'q')
# searchbox = searchbox[0]
# searchbox.send_keys("selenium")
# searchbox.submit()

# searchlink = mywait.until(EC.presence_of_element_located(
#     (By.XPATH, '//h3[text()="fake_item"]')))
# # This will wait for 10 seconds for the 'fake_item' element to be present on the page,
# # but since it doesn't exist, it will raise a TimeoutException which will be ignored.

# input()
# driver.quit()


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
mywait = WebDriverWait(driver, 10, ignored_exceptions=[TimeoutException])

driver.get("https://www.google.com")

searchbox = driver.find_elements(By.NAME, 'q')
searchbox = searchbox[0]
searchbox.send_keys("selenium")
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located(
    (By.XPATH, '//h3[text()="fake_item"]')))
# This will wait for 10 seconds for the 'fake_item' element to be present on the page,
# but since it doesn't exist, it will raise a TimeoutException which will be ignored.

input()
driver.quit()
