from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/")
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(20)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(10)


html = driver.page_source
driver.quit()
# Print and save the HTML source code
print(html)
with open("data.txt", "w") as file:
    file.write(html)
    

    