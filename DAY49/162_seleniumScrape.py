# from selenium import webdriver

# # start the browser
# driver = webdriver.Firefox()

# # navigate to the website
# driver.get("https://www.example.com")

# # scroll down by 1000 pixels
# javaScript = "window.scrollBy(0, 1000);"
# driver.execute_script(javaScript)

# # wait for the page to load
# driver.implicitly_wait(20)

# # get the HTML source code
# html = driver.page_source

# # print the HTML source code
# print(html)

# # close the browser
# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.example.com")


javaScript = "window.scrollBy(0, 1000);"
driver.execute_script(javaScript)


while True:
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pagination-next"))
        )
    except:
        break

html = driver.page_source

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pagination-next"))
    )
finally:
    driver.quit()
    print(html)
    with open("data.txt", "w") as file:
        file.write(html)
    
    

