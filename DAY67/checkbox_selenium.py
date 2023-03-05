import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
# driver.implicitly_wait(3)
# Select specific checkbox

try:
    # select one checkbox
    # checkbox = driver.find_element(By.XPATH,'//*[@id="female"]').click()
    # # select all the checkboxes
    checkboxes = driver.find_elements(By.XPATH,'//input[@type="checkbox" and contains(@id,"day") ]')
    # print(len(checkboxes))

    # for box in checkboxes:
        # weekname = box.get_attribute("id")
        # if weekname == 'monday' or weekname == 'sunday':
            # box.click()

    # for i in range(len(checkboxes)-2,len(checkboxes)):
        # checkboxes[i].click()

    time.sleep(2)

    # for item in checkboxes:
        # if item.is_selected():
            # item.click()    
    time.sleep(10)
except Exception as e:
    print(e)


