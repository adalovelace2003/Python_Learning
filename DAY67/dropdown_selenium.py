import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")

dropcountry_element = Select(driver.find_element(
    By.XPATH, '//*[@id="input-country"]'))


# dropcountry_element =Select( driver.find_element(By.XPATH,'//*[@id="input-country"]'))
# dropcountry_element.select_by_value("10")
# dropcountry_element.select_by_value("149")
#
all_options = dropcountry_element.options

for options in all_options:
    print(options.text)
    if options.text == "India":
        options.click()


time.sleep(10)
