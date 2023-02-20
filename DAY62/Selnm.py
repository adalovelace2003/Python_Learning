from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

try:
    # driver.find_element("id","small-searchterms").send_keys("Hello")
    # driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()
    # driver.find_element("class","search-box-button").click()

    # links = driver.find_elements(By.CLASS_NAME,"item-box")
    # print(links)
    # print(len(links))

    Link = driver.find_elements(By.TAG_NAME,"a")
    print(Link)
    print(len(Link))
    


except:
    print("Error Occured")



input("Press any key")
driver.quit()
