from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# configure the webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # run in headless mode to hide the browser window
driver = webdriver.Chrome(options=options)

# navigate to the test site
driver.get('https://www.example.com')

# wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))

# scrape the page content
title = driver.title
heading = driver.find_element(By.TAG_NAME, 'h1').text
paragraphs = driver.find_elements(By.TAG_NAME, 'p')

print(f'Title: {title}')
print(f'Heading: {heading}')
print('Paragraphs:')
for p in paragraphs:
    print(p.text)

# close the webdriver
driver.quit()