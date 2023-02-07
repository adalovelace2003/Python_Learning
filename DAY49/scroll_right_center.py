from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Hello")

# Get the width and height of the page
width = driver.execute_script("return document.body.offsetWidth")
height = driver.execute_script("return window.innerHeight")

# Scroll to the right center of the page
right_center = "window.scrollTo(0, document.body.scrollHeight);"
driver.execute_script(right_center)

# Quit the browser