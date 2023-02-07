from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(executable_path="//usr//bin//brave-browser")
driver.get("https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/")

javaScript = "window.scrollBy(0, 1000);"
driver.execute_script(javaScript)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pagination-next"))
    )
finally:
    driver.quit()



html_source = driver.page_source
print(html_source)
driver.quit()

