from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://google.com")
try:
    # element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")
    # time.sleep(50)
    try:
        lucky_button = driver.find_element(By.XPATH, "//*[contains(@value, 'I'm Feeling Lucky')]")
    except:
        lucky_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[4]/center[1]/input[2]")
    # element.send_keys("Hello" + Keys.ENTER)
    lucky_button.click()
# //*[contains(@id,st)]
# this will select both start and stop
# //*[starts=with(@id,st)]
# //*[@id='start' or @id='stop']

except Exception as e:
    print(e)

input()
driver.quit()
