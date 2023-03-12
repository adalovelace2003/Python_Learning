import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html"
driver.get(url)


driver.switch_to.frame("packageListFrame")
driver.find_element(By.XPATH, "/html/body/main/ul/li[1]/a").click()
driver.switch_to.default_content()


driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT,"WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()
driver.switch_to.default_content()



time.sleep(10)
driver.quit()

# driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
# /html/body/main/ul/li[1]/a



