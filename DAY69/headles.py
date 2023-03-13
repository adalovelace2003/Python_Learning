import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)

# url = "https://demo.nopcommerce.com"
url = "https://www.google.com"
driver.get(url)

cookies = driver.get_cookies()
print(len(cookies))
# print(cookies)

for c in cookies:
    print(c.get('name'), ":", c.get('value'))

driver.add_cookie({"name": "Mycookie", "value": "12345"})
cookies = driver.get_cookies()
for c in cookies:
    print(c.get('name'), ":", c.get('value'))

time.sleep(10)
driver.quit()





