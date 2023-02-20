from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

driver.find_elements()
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("usernametest")
driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("passtest")
# 
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("username")
# 
driver.find_element(By.CSS_SELECTOR,"[id=email]").send_keys("passowrd")
# 
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("Username")
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("Username123")




input("Press enter")
