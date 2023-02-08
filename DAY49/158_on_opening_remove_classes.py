from selenium import webdriver

# Start the browser
driver = webdriver.Firefox()

# Navigate to the website
driver.get("https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/")

driver.implicitly_wait(20)

# Remove the class from the body element
element = driver.find_element_by_tag_name("body")
classes = element.get_attribute("class")
classes = classes.replace("map-view", "")
driver.execute_script("arguments[0].setAttribute('class', '" + classes + "')", element)

# Render the updated page
driver.implicitly_wait(20)

# Close the browser
# driver.quit()
