from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
# try:
# searchbox = driver.find_element(By.XPATH, "//*[@id='small-searchtermsa']")
# print(searchbox.is_displayed())
# except:
# print("False")

try:
    male_radio = driver.find_element(By.XPATH, '//*[@id="gender-male"]')
    female_radio = driver.find_element(By.XPATH, '//*[@id="gender-female"]')

    male_radio.click()

    print(male_radio.is_selected())
    female_radio.click()
    print(male_radio.is_selected())
except:
    print("Error")


input()

driver.quit()
