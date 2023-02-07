from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/")

grid_button = driver.find_element_by_xpath('//*[@id="list-view-toggle"]')
driver.execute_script("arguments[0].click();", grid_button)
