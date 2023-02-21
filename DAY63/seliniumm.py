from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# self element
# text_msg = driver.find_element(By.XPATH,"(//a[normalize-space()='NLC India L'])[1]/self::a").text
# print(text_msg)

# parent element
# text_msg = driver.find_element(By.XPATH,"(//a[normalize-space()='NLC India L'])[1]/parent::td").text
# print(text_msg)

# ancestir element
# childs = driver.find_elements(By.XPATH,"//a[contains(text(),'NLC India L')]/ancestor::tr/child::td")
# for child in childs:
    # print(child.text)

# descendant element
# childs = driver.find_elements(By.XPATH,"//a[contains(text(),'NLC India L')]/ancestor::tr/descendant::*")
# print(len(childs))

#followings element
# childs =driver.find_elements(By.XPATH,"//a[contains(text(),'NLC India L')]/ancestor::tr/following::tr")
# print(len(childs))

#preceeding element
# childs =driver.find_elements(By.XPATH,"//a[contains(text(),'NLC India L')]/ancestor::tr/preceeding::tr")
# print(len(childs))

#preceeding-sibling element
childs = driver.find_elements(By.XPATH, "//a[contains(text(),'NLC India L')]/ancestor::tr/preceding-sibling::*")
print(len(childs))

# childs = driver.find_element(By.XPATH,"//a[contains(text(),'NLC India L')]/ancestor::tr")
# print(childs.text) #NLC India L A 78.00 81.70 + 4.74
input("Press Enter")
driver.quit()




